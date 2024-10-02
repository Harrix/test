import itertools

for x, y, z, w in itertools.product([0, 1], repeat=4):
    t = int(((x <= y) and (z == (not w)))<=(x == (x or z)))
    print(x, y, z, t, w)



for x, y, z in itertools.product([0, 1], repeat=3):
    t = int(z and (y == (not x)))
    print(x, y, z, t)

ААААААААААААААААААААААААааааааааааааааааааааааааааааааааааааааааааааааааааааааа!!!
