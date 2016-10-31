# -*- coding: utf-8 -*-

def make_extra_data(request, response, body):
    return str(request.META)
