def triangle_number(num):
    i = num
    triangle_num = 0
    while i > 0:
        triangle_num += i
        i -= 1
    return triangle_num


target_num_of_factors = 477
print(triangle_number(2079))
print(triangle_number(7))
natural_num = 2
triangle_num = 1
num_factors = 2
while True:
    num_factors = 2
    triangle_num += natural_num
    n = 2
    for n in range(2, int(triangle_num / 2)):
        if triangle_num % n == 0:
            num_factors += 2
    if num_factors >= target_num_of_factors:
        print(natural_num)
        print(triangle_num)
        print(num_factors)
        break
    else:
        natural_num += 1
