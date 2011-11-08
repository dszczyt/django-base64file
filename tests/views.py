# -*- coding: utf-8 -*-
from django.views.generic import CreateView
from .forms import AvatarForm

class AvatarCreateView(CreateView):
    form_class = AvatarForm
    success_url = '/'

