# PeymaanEsi

# Get Sum Of Multiplies Of 3 Or 5 Under 1000.

sum = 0

for i in range(1000):

    if i % 3 == 0 or i % 5 == 0:

        sum += i

else:

    print(sum)