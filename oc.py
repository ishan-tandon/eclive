def func(a,b,c,d,e):
    A = sum([abs(a-x) for x in [3,10,4,13,6,5,8,4,3,3,3,2,2,20,4,5,9]]) / 17
    B = sum([abs(b-x) for x in [4,5,3,4,5,3,5,3,4,18,4,3,3,4,2,3,14]]) / 17
    C = sum([abs(c-x) for x in [18,4,2,2,4,2,1,2,20,2,20,4,5,2,5,6,1]]) / 17
    D = sum([abs(d-x) for x in [1,2,1,6,2,20,5,19,5,4,1,19,6,6,3,2,2]]) / 17
    E = sum([abs(e-x) for x in [2,3,20,20,3,4,2,20,2,1,18,5,4,3,8,4,3]]) / 17
    return [a,b,c,d,e], (A+B+C+D+E)

from itertools import permutations
l = list(permutations(range(2, 7)))
min = 100
minlist=[0,0,0,0,0]
for i in l:
    iterlist, val = func(i[0],i[1],i[2],i[3],i[4])
    if val < min:
        minlist = iterlist
        min = val

print (min, minlist)
