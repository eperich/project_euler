primes = [2, 3, 5, 7, 11, 13]
multiples = []
highest_prime = 200000
for n in primes:
    x = 2
    while n * x < highest_prime:
        multiple_n = n * x
        primes_less = [i for i in primes if i < n]
        add_multiple = True
        for prime in primes_less:
            if (multiple_n / prime).is_integer():
                add_multiple = False
        if add_multiple:
            multiples.append(multiple_n)
        x += 1

i = 14
if i in multiples:
    i += 1

while max(primes) < highest_prime:
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
        prime_second_highest = primes[len(primes) - 2]
        x = prime_second_highest + 1
        while i * x < highest_prime:
            multiple_i = i * x
            primes_less = [j for j in primes if j < i]
            #add_multiple = True
            #for prime in primes_less:
                #if (multiple_i / prime).is_integer():
                    #add_multiple = False
            #if add_multiple:
                #multiples.append(multiple_i)
            x += 1
    i = i + 1

primes.pop(len(primes) - 1)
print(sum(primes))
