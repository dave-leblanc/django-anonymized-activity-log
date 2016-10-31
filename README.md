This django app intended for writing highly detailed anonymized HTTP logs to database

Features:
- DB router for writing logs to another database.
- support for processing of Extra data into logs
- Filters for ignoring some queries by URL, HTTP methods and response codes.
- Saving anonymous activity as fake user.
- Autocreation log DB (for postgresql)

Based largely on: https://github.com/scailer/django-user-activity-log


Install:

$ pip install django-anonymous-activity-log

settings.py:


```python
INSTALLED_APPS = (
    ...
    'anonymized_activity_log',
)

MIDDLEWARE_CLASSES = (
    ...
    'anonymized_activity_log.middleware.ActivityLogMiddleware',
)

# For writing log to another DB

DATABASE_ROUTERS = ['anonymized_activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'anonymized_activity_log': 'logs'}

# If you set up DATABASE_APPS_MAPPING, but don't set related value in
# DATABASES, it will created automatically using "default" DB settings
# as example.
DATABASES = {
    'logs': {
        ...
    },
}

# Create DB automatically (for postgres, and may be mysql).
# We create log database automatically using raw SQL in pre_migrate signal.
# You must insure, that DB user has permissions for creation databases. 
# Tested only for postgresql
ACTIVITYLOG_AUTOCREATE_DB = False

# App settings

# Log actions by non-logged in users?
ACTIVITYLOG_ANONYMOUS = True

# Only this methods will be logged
ACTIVITYLOG_METHODS = ('POST', 'GET')

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
ACTIVITYLOG_STATUSES = (200, )

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
# ACTIVITYLOG_EXCLUDE_STATUSES = (302, )

# URL substrings, which ignores
ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )
```

$ python manage.py migrate & python manage.py migrate --database=logs

If you use ACTIVITYLOG_AUTOCREATE_DB migrations to logs database 
will be run automatically.
