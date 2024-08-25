import time
from string import ascii_letters, digits

comb = ascii_letters + digits

past = time.time()
for i in comb:
    for h in comb:
        for j in comb:
            for k in comb:
                ...
now = time.time()
print(now - past)