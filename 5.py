# PeymaanEsi

# What is the smallest positive number that is evenly divisible by all of the numbers from to ?

from math import sqrt

n = 1

while True:

    for i in range(2, 21):
        
        if n % i == 0:
            # print(n, '%', i)
            continue
        else:
            # print(n, '!%', i)
            n += 1
            break
    else:
        print(n)
        break
    
