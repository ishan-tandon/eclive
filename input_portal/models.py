from django.db import models

# Create your models here.
class current_leaderboard(models.Model):
    abbr = models.CharField(max_length = 4, unique = True)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    driver_no = models.IntegerField()
    team_name = models.CharField(max_length = 64)
    team_color = models.CharField(max_length = 7)
    points = models.FloatField()
    rank_override = models.IntegerField()

    def __str__(self):
        return str(self.driver_no) + "current leaderboard model"


class alltime_leaderboard(models.Model):
    abbr = models.CharField(max_length = 4, unique = True)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    driver_no = models.IntegerField()
    points = models.FloatField()
    races = models.IntegerField()
    points = models.IntegerField()
    wins = models.IntegerField()
    podiums = models.IntegerField()
    poles = models.IntegerField()
    most_zeros = models.IntegerField()
    seasons = models.IntegerField()

    def __str__(self):
        return str(self.driver_no) + "alltime leaderboard model"
