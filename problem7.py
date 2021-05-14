primes = [2, 3, 5, 7, 11, 13]

i = 14
while len(primes) < 10001:
    div_list = []
    n = 0

    while n < len(primes):
        division = i / primes[n]
        if division.is_integer():
            indicator = 0
            break
        else:
            indicator = 1
        div_list.append(indicator)
        n = n + 1

    if len(div_list) == len(primes):
        primes.append(i)
    i = i + 1


print(primes[10000])
