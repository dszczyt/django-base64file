# -*- coding: utf-8 -*-
from django.db import models

class Avatar(models.Model):
    username = models.CharField(max_length=255)
    picture = models.FileField(upload_to="tests/uploads")

    def __unicode__(self):
        return self.username

