from random import seed
from random import random
from random import randint

length = 200
print(str(length))
for x in range(0, length):
    i = x+1
    d = randint(1, 60)
    t = randint(1, 1440-d-10)
    p = round(random()*99, 3)
    print(str(i) + " " + str(t) + " " + str(d) + " " + str(p))
