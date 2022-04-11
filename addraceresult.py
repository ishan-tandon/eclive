import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estimation_app.settings')

import django
django.setup()

from input_portal.models import results_racecodes, results_info, results_data, current_leaderboard, team_leaderboard

def fullname_extractor(input_abbr):
    t = current_leaderboard.objects.get(abbr = input_abbr)
    return t.first_name + " " + t.last_name

def color_extractor(input_abbr):
    t = current_leaderboard.objects.get(abbr = input_abbr)
    return t.team_color

rc = input("Race Code:\t")
round_no = int(input("Round No.:\t"))
country = input("Country:\t")
racename = input("Race Name:\t")
year = 2022

trackpng = "trackpng_" + rc[0:3] + ".png"
shikulu = "shikulu_" + rc[0:3] + ".jpg"

pole_fn = fullname_extractor(input("Pole:\t"))

eotd_fn = fullname_extractor(input("EotD:\t"))

mz = input("Most Zeros:\t")
mz_fn = fullname_extractor(mz)

nz = int(input("No. of Zeros:\t"))

col1 = input("Color 1:\t")
col2 = input("Color 2:\t")

print("Review Race Information:")
print("Race Code:", rc)
print("Round No.:", round_no)
print("Country:", country)
print("Race Name:", racename, year)
print("\nPole:", pole_fn)
print("EotD:", eotd_fn)
print("Most Zeros:", mz_fn)
print("\n",trackpng,"\n",shikulu,"\n",col1,col2)

cont = input("Type YES to confirm:\t")

trc = results_racecodes(racecode = rc, year = year, round_no = round_no, track_png = trackpng, country = country, race_name = racename)
trc.save()
tri = results_info(racecode = trc, shikulu = shikulu, pole = pole_fn, eotd = eotd_fn, most_zeros = mz_fn, no_zeros = nz, col_one = col1, col_two = col2)
tri.save()

n = int(input("No. of Estimators: "))
order=[]

for i in range(n):
    r = input("abbr score for pos " + str(i+1) + ":\t").strip().split()
    row = [rc, i+1, r[0], color_extractor(r[0]), float(r[1])]
    order.append(row)

cont = input("Type YES to confirm:\t")

pointslist=[25,18,15,12,10,8,6,4,2,1,0,0,0,0,0,0,0,0,0,0]

for i in order:
    if i[2] == mz:
        x = 1
    else:
        x = 0
    t = results_data(racecode = trc, pos = i[1], estimator = i[2], team_color = i[3], score = i[4], pts = (pointslist[i[1]-1] + x))
    u = current_leaderboard.objects.get(abbr = i[2])
    w = current_leaderboard.objects.get(team_color = i[3])
    u.points += t.pts
    w.points += t.pts
    u.save()
    w.save()
    t.save()