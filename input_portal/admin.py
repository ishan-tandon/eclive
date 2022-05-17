from django.contrib import admin
from input_portal.models import current_leaderboard, alltime_leaderboard, team_leaderboard, results_racecodes, results_info, results_data, sprint_data
# Register your models here.

admin.site.register(current_leaderboard)
admin.site.register(alltime_leaderboard)
admin.site.register(team_leaderboard)
admin.site.register(results_racecodes)
admin.site.register(results_info)
admin.site.register(results_data)
admin.site.register(sprint_data)
