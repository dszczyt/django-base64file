# -*- coding: utf-8 -*-
from django.core.files import File
import base64, mimetypes

class Base64File(File):
    @classmethod
    def from_data(cls, data):
        pass

    def base64(self):
        mimetype = mimetypes.guess_type(self.name)[0] or "text/plain"
        return "data:%s;filename:%s;base64,%s" % (
            mimetype,
            self.name,
            base64.b64encode(self.read()),
        )

