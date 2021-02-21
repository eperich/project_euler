a1 = 1
a2 = 2

a = [1, 2]

a_n = 2
i = 2
while a_n < 4000000:
    a.append(a[i - 1] + a[i - 2])
    a_n = a[i]
    i += 1

total = 0
for i in a:
    if i % 2 == 0:
        total += i

print(total)
