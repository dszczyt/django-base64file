# -*- coding: utf-8 -*-
from django.core.files import File
import base64

class Base64File(File):
    @classmethod
    def from_data(cls, data):
        pass

    def base64(self):
        return "data:%s;filename:%s;base64,%s" % (
            "",
            self.name,
            base64.b64encode(self.read()),
        )

