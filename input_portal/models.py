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
        return self.first_name + " " + self.last_name

class team_leaderboard(models.Model):
    team_name = models.CharField(max_length = 32, unique = True)
    driver_name = models.CharField(max_length = 128)
    team_color = models.CharField(max_length = 7)
    points = models.FloatField()
    rank_override = models.IntegerField()

    def __str__(self):
        return str(self.team_name)


class alltime_leaderboard(models.Model):
    abbr = models.CharField(max_length = 4, unique = True)
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    driver_no = models.IntegerField()
    points = models.FloatField()
    races = models.IntegerField()
    wins = models.IntegerField()
    podiums = models.IntegerField()
    sprints = models.IntegerField()
    sprint_king = models.IntegerField()
    sprint_medals = models.IntegerField()
    poles = models.IntegerField()
    most_zeros = models.IntegerField()
    seasons = models.IntegerField()
    championships = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class results_racecodes(models.Model):
    racecode = models.CharField(max_length = 5, unique = True)
    year = models.IntegerField()
    round_no = models.IntegerField()
    track_png = models.CharField(max_length = 24)
    country = models.CharField(max_length = 32)
    race_name = models.CharField(max_length = 128)
    sprint = models.IntegerField()

    def __str__(self):
        return self.racecode

class results_info(models.Model):
    racecode = models.ForeignKey(results_racecodes, on_delete=models.CASCADE)
    shikulu = models.CharField(max_length = 24)
    pole = models.CharField(max_length = 65)
    eotd = models.CharField(max_length = 65)
    sprint_king = models.CharField(max_length = 65)
    most_zeros = models.CharField(max_length = 65)
    no_zeros = models.IntegerField()
    col_one = models.CharField(max_length = 7)
    col_two = models.CharField(max_length = 7)

    def __str__(self):
        return str(self.racecode)

class results_data(models.Model):
    racecode = models.ForeignKey(results_racecodes, on_delete=models.CASCADE)
    pos = models.IntegerField()
    estimator = models.CharField(max_length = 4)
    team_color = models.CharField(max_length = 7)
    grid = models.CharField(max_length=2)
    score = models.IntegerField()
    pts = models.FloatField()

    def __str__(self):
        return str(self.racecode) + "_" + self.estimator

class sprint_data(models.Model):
    racecode = models.ForeignKey(results_racecodes, on_delete=models.CASCADE)
    pos = models.IntegerField()
    estimator = models.CharField(max_length = 4)
    team_color = models.CharField(max_length = 7)
    grid = models.CharField(max_length=2)
    score = models.IntegerField()
    pts = models.FloatField()

    def __str__(self):
        return str(self.racecode) + "_" + self.estimator
