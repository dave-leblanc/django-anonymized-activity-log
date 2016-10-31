# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.conf import settings
from django.utils.module_loading import import_string as _load
from django.core.exceptions import DisallowedHost, ObjectDoesNotExist
from django.http import HttpResponseForbidden
from .models import ActivityLog
from . import conf

import hashlib


def get_ip_address(request):
    for header in conf.IP_ADDRESS_HEADERS:
        addr = request.META.get(header)
        if addr:
            return addr.split(',')[0].strip()


def get_extra_data(request, response, body):
    if not conf.GET_EXTRA_DATA:
        return
    return _load(conf.GET_EXTRA_DATA)(request, response, body)


class ActivityLogMiddleware:
    def process_request(self, request):
        self._write_log(request)
        try:
            x = True
        except DisallowedHost:
            return HttpResponseForbidden()

    def process_response(self, request, response):
        the_record = self._get_log(request)
        miss_log = []
        if conf.STATUSES:
            miss_log.append(response.status_code not in conf.STATUSES)

        if conf.EXCLUDE_STATUSES:
            miss_log.append(response.status_code in conf.EXCLUDE_STATUSES)

        if any(miss_log):
            the_record.delete()
            return

        the_record.response_code = response.status_code
        the_record.extra_data = get_extra_data(request, response, getattr(request, 'saved_body', ''))
        the_record.save()

        return response

    def _write_log(self, request):
        miss_log = [
            not (conf.ANONYMOUS or request.user.is_authenticated()),
            request.method not in conf.METHODS,
            any(url in request.path for url in conf.EXCLUDE_URLS)
        ]

        if any(miss_log):
            return

        if getattr(request, 'user', None) and request.user.is_authenticated():
            user_str = str(str(request.user.pk) + settings.SECRET_KEY).encode('utf-8')
        elif getattr(request, 'session', None):
            user_str = str(str(0) + settings.SECRET_KEY).encode('utf-8')
        else:
            return

        user = hashlib.md5(user_str).hexdigest()
        if request.method in ('GET', 'POST'):
            request_vars = json.dumps(getattr(request, request.method).__dict__)
        else:
            request_vars = None

        activity_log = ActivityLog(
            user=user,
            request_url=request.build_absolute_uri()[:255],
            request_method=request.method,
            ip_address=get_ip_address(request),

            session_id=request.session.session_key,

            request_path=request.path,
            request_query_string=request.META["QUERY_STRING"],
            request_vars=request_vars,
            request_secure=request.is_secure(),
            request_ajax=request.is_ajax(),
            request_meta=request.META.__str__(),
        )
        if request.user.is_authenticated():
            activity_log.requestUser = request.user

        activity_log.save()
        request.META['activity_log_id'] = activity_log.pk

    def _get_log(self, request):
        try:
            return ActivityLog.objects.get(pk=request.META['activity_log_id'])
        except ObjectDoesNotExist:
            return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Fix the issue with the authorization request
        the_record = self._get_log(request)
        if the_record:
            the_record.view_function = view_func.__name__
            the_record.view_doc_string = view_func.__doc__
            the_record.view_args = json.dumps(view_kwargs)

            the_record.save()
