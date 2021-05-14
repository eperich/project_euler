def sum_of_squares(num):
    i = 1
    square_sum = 0
    while i < num + 1:
        square_sum += i ** 2
        i += 1

    return square_sum


def square_of_sum(num):
    i = 1
    total_sum = 0
    while i < num + 1:
        total_sum += i
        i += 1
    square = total_sum ** 2
    return square


max_num = 100
s1 = sum_of_squares(max_num)
s2 = square_of_sum(max_num)
diff = abs(s1 - s2)
print(diff)
