from django.shortcuts import render
from django.views.generic import (TemplateView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class DraggableView(TemplateView):
    template_name = 'drag.html'

class LeaderView(TemplateView):
    template_name = 'leaderboard.html'
