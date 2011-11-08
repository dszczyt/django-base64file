# -*- coding: utf-8 -*-
from django.test import TestCase

from StringIO import StringIO
from django.core.files import File

class Base64FileTest(TestCase):
    def test_upload_with_file(self):
        result = self.client.post(
            '/upload/',
            {
                'username': 'test',
                'picture': File(
                    StringIO("TEST"),
                    name="test.txt",
                ),
            }
        )
