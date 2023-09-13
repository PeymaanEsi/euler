# PeymaanEsi

# What is the 10001 st prime number?

c = 1

n = 2

while c != 10002:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
        else:
            continue
    else:
        print(n)
        c += 1
    n += 1