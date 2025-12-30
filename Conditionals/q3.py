## Roll a dice 10 times using random.randint() and count how many times you get 6

import random

random.seed(6)
six = 0
for i in range(10):
    r = random.randint(1, 6)
    # print(r)
    if(r == 6):
        six += 1

print(f"Six: {six}")
