# -*- coding: utf-8 -*-

from setuptools import setup

DESCRIPTION = """
This django app intended for writing highly detailed anonymized HTTP logs to database

Features:
  - DB router for writing logs to another database.
  - Filters for ignoring some queries by URL, HTTP methods and response codes.
  - Saving anonymous activity as fake user.

More: https://github.com/dave-leblanc/django-anonymous-activity-log

Based largely on: https://github.com/scailer/django-user-activity-log
"""

setup(
    name='django-anonymized-activity-log',
    version='0.0.17',
    author='Dave LeBlanc',
    author_email='iam@daveleblanc.tech',

    include_package_data=True,
    packages=[
        'anonymized_activity_log',
        'anonymized_activity_log.migrations',
    ],

    url='https://github.com/dave-leblanc/django-anonymized-activity-log',
    license='MIT license',
    description='Anonymous HTTP logging.',
    long_description=DESCRIPTION,

    install_requires=[
    ],

    classifiers=(
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
