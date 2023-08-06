# PeymaanEsi

# Calculate Prime Factor Of 'n'

import math

def lpf(n):
    
    for i in range(2, int(math.sqrt(n)) + 1):

        while n % i == 0:

            n //= i

            print(i)

lpf(600851475143)