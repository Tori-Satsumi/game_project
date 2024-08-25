import time
from string import ascii_letters, digits

comb = ascii_letters + digits

past = time.now()
for i in comb:
    for h in comb:
        for j in comb:
            for k in comb:
                print(i, h, j, k)
                