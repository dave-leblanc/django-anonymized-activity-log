from django.conf import settings

from anonymized_activity_log.middleware import get_encryption_function

def anonymize_user(request):
    if getattr(request, 'user', None) and request.user.is_authenticated():
        user_str = str(str(request.user.pk) + settings.SECRET_KEY).encode('utf-8')
    else:
        user_str = str(str(0) + settings.SECRET_KEY).encode('utf-8')

    anonymize = get_encryption_function()
    return anonymize(user_str)
