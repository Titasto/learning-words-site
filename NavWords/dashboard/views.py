from django.shortcuts import render
from django.views.generic import TemplateView


class DashBoard(TemplateView):
    template_name = 'base.html'
    extra_context = {'title': 'JustLearning'}
