# PeymaanEsi

# Find the largest palindrome made from the product of two 3-digit numbers.

# Check if a number is palindrome.

def is_palindrome(n):

    temp = n

    reverse = 0

    while temp != 0:

        reverse = reverse * 10 + temp % 10

        temp //= 10

    return(n == reverse)

# Palindrome numbers list.

palindromes = []

for i in range(999, 0, -1):

    for j in range(999, 0, -1):

        # print(i, '*', j)

        if is_palindrome(i * j):

            palindromes.append(i * j)

print(max(palindromes))