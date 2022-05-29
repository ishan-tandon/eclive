from django.shortcuts import render
from django.views.generic import (TemplateView)
from input_portal.models import current_leaderboard, team_leaderboard, results_racecodes, results_info, results_data, sprint_data, alltime_leaderboard
# Create your views here.

def AboutView(request):
    race_results_list = results_racecodes.objects.order_by('-year','-round_no')
    results_dict = {'races': race_results_list}
    return render(request, 'about.html', context = results_dict)

class DraggableView(TemplateView):
    template_name = 'drag.html'

class EmbedView(TemplateView):
    template_name = 'embed.html'

def LeaderView(request):
    current_leaderboard_list = current_leaderboard.objects.order_by('-points','rank_override')
    leaderboard_dict = {'cl_table' : current_leaderboard_list}
    return render(request, 'leaderboard.html', context = leaderboard_dict)

def TeamLeaderView(request):
    team_leaderboard_list = team_leaderboard.objects.order_by('-points','rank_override')
    leaderboard_dict = {'tl_table' : team_leaderboard_list}
    return render(request, 'teamleaderboard.html', context = leaderboard_dict)

def AllTimeStatsView(request):
    href_list=['races', 'wins', 'podiums', 'poles', 'mostzeros', 'sprintkings', 'points']
    selected_list=['unselected', 'unselected', 'unselected', 'unselected', 'unselected', 'unselected', 'unselected']
    alltimestats_list = alltime_leaderboard.objects.order_by('-championships', '-wins', '-podiums', '-points')
    stats_dict = {'stat_table' : alltimestats_list, 'h': href_list, 's': selected_list}
    return render(request, 'alltimestats.html', context = stats_dict)

def AllTimeStatsViewO(request, orderBy):
    href_list=['../races', '../wins', '../podiums', '../poles', '../mostzeros', '../sprintkings', '../points']
    selected_list=['unselected', 'unselected', 'unselected', 'unselected', 'unselected', 'unselected', 'unselected']
    if orderBy == "races":
        alltimestats_list = alltime_leaderboard.objects.order_by('-races', '-wins', '-podiums', '-points')
        i=0
    elif orderBy == "wins":
        alltimestats_list = alltime_leaderboard.objects.order_by('-wins', '-podiums', '-points')
        i=1
    elif orderBy == "podiums":
        alltimestats_list = alltime_leaderboard.objects.order_by('-podiums', '-wins', '-points')
        i=2
    elif orderBy == "poles":
        alltimestats_list = alltime_leaderboard.objects.order_by('-poles', '-wins', '-podiums', '-points')
        i=3
    elif orderBy == "mostzeros":
        alltimestats_list = alltime_leaderboard.objects.order_by('-most_zeros', '-wins', '-podiums', '-points')
        i=4
    elif orderBy == "sprintkings":
        alltimestats_list = alltime_leaderboard.objects.order_by('-sprint_king', '-wins', '-podiums', '-points')
        i=5
    elif orderBy == "points":
        alltimestats_list = alltime_leaderboard.objects.order_by('-points', '-wins', '-podiums')
        i=6
    else:
        return render (request, 'noorder.html')
    href_list[i] = ".."
    selected_list[i] = "selected"
    stats_dict = {'stat_table' : alltimestats_list, 'h': href_list, 's': selected_list}
    return render(request, 'alltimestats.html', context = stats_dict)

def ResultsView(request, racecode):
    R = results_racecodes.objects.filter(racecode= racecode)
    if (len(R) == 0):
        return render (request, 'noresult.html')
    r = results_info.objects.filter(racecode__racecode= racecode)
    D = results_data.objects.filter(racecode__racecode= racecode).order_by('pos')
    if R[0].sprint == 0:
        results_dict={"year": R[0].year, "rn": R[0].round_no, "country": R[0].country, "name": R[0].race_name, "shikulu": r[0].shikulu, "pole": r[0].pole, "eotd": r[0].eotd, "mz": r[0].most_zeros, "nz": r[0].no_zeros, "co": r[0].col_one, "ct": r[0].col_two, "p1": D[0], "p2": D[1], "p3":D[2], "pr":D[3:]}
        return render (request, 'results.html', context = results_dict)
    else:
        S = sprint_data.objects.filter(racecode__racecode= racecode).order_by('pos')
        results_dict={"year": R[0].year, "rn": R[0].round_no, "country": R[0].country, "name": R[0].race_name, "shikulu": r[0].shikulu, "pole": r[0].pole, "eotd": r[0].eotd, "mz": r[0].most_zeros, "nz": r[0].no_zeros, "co": r[0].col_one, "ct": r[0].col_two, "p1": D[0], "p2": D[1], "p3":D[2], "pr":D[3:], "s1": S[0], "sr": S[1:], "sk": r[0].sprint_king}
        return render (request, 'sprintresults.html', context = results_dict)
