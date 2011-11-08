#!/usr/bin/env python
import sys
from os.path import dirname, abspath, join, exists
from shutil import rmtree
from optparse import OptionParser

from django.conf import settings #, global_settings

if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',

            'tests',
        ],
        ROOT_URLCONF='tests.urls',
        DEBUG=False,
        SITE_ID=1,
    )

from django.test.simple import DjangoTestSuiteRunner

def runtests(*test_args, **kwargs):
    if 'south' in settings.INSTALLED_APPS:
        from south.management.commands import patch_for_test_db_setup
        patch_for_test_db_setup()

    if not test_args:
        test_args = ['tests']
    parent = dirname(abspath(__file__))

    uploads_dir = join(parent, "tests/uploads")
    if exists(uploads_dir):
        rmtree(uploads_dir)
    sys.path.insert(0, parent)
    test_runner = DjangoTestSuiteRunner(verbosity=kwargs.get('verbosity', 1), interactive=kwargs.get('interactive', False), failfast=kwargs.get('failfast'))
    failures = test_runner.run_tests(test_args)
    if exists(uploads_dir):
        rmtree(uploads_dir)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--failfast', action='store_true', default=False, dest='failfast')

    (options, args) = parser.parse_args()

    runtests(failfast=options.failfast, *args)
