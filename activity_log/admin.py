# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'request_method', 'request_url',
                    'response_code', 'datetime')
    date_hierarchy = 'datetime'
    list_filter = ('request_method', 'response_code')
    search_fields = ('user', 'request_url')


admin.site.register(models.ActivityLog, LogAdmin)
