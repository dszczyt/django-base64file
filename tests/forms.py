# -*- coding: utf-8 -*-
from django import forms
from .models import Avatar
from base64file.field import Base64FileField

class AvatarForm(forms.ModelForm):
    picture = Base64FileField()

    class Meta:
        model = Avatar

