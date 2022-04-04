from django.shortcuts import render
from django.views.generic import (TemplateView)
from input_portal.models import current_leaderboard, team_leaderboard
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class DraggableView(TemplateView):
    template_name = 'drag.html'

def LeaderView(request):
    current_leaderboard_list = current_leaderboard.objects.order_by('-points','rank_override')
    leaderboard_dict = {'cl_table' : current_leaderboard_list}
    return render(request, 'leaderboard.html', context = leaderboard_dict)

def TeamLeaderView(request):
    team_leaderboard_list = team_leaderboard.objects.order_by('-points','rank_override')
    leaderboard_dict = {'tl_table' : team_leaderboard_list}
    return render(request, 'teamleaderboard.html', context = leaderboard_dict)
