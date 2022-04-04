from django.contrib import admin
from input_portal.models import current_leaderboard, alltime_leaderboard
# Register your models here.

admin.site.register(current_leaderboard)
admin.site.register(alltime_leaderboard)
