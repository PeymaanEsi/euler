# PeymaanEsi

# Get Sum Of Even Fibbonacci Numbers Below 4,000,000.

# ُShow Fibbonaci Series Under 'n'.

def fib(n):

    a, b = 0, 1
    
    while a < n:
    
        yield a
    
        a, b = b, a+b
    
fibs = fib(4000000)

# Reduce Elements To Even Numbers.

evens = [x for x in fibs if x % 2 == 0]

print(sum(evens))
