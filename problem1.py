max_num = int(input("Enter a maximum:"))

i = 0
total = 0
while i < max_num:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1

print(total)
