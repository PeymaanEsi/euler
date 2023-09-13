# PeymaanEsi

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

a = b = 0

for i in range(101):
    a += (i * i)
    b += i
print((b * b) - a)