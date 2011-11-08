# -*- coding: utf-8 -*-
from django.test import TestCase

from StringIO import StringIO
from django.core.files import File
from os.path import dirname, abspath, join, exists
from base64file.utils import Base64File

class Base64FileTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upload_with_file(self):
        response = self.client.post(
            '/upload/',
            {
                'username': 'test',
                'picture': File(
                    StringIO("TEST"),
                    name="test.txt",
                ),
            },
            follow = False,
        )
        self.assertEqual(response.status_code, 302)

    def test_upload_with_base64_data(self):
        response = self.client.post(
            '/upload/',
            {
                'username': 'test',
                'picture': Base64File(
                    StringIO("TEST"),
                    name="test.txt",
                ).base64(),
            },
            follow = False,
        )
        self.assertEqual(response.status_code, 302)

