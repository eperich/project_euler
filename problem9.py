def check_sum(num1, num2, num3):
    num_sum = num1 + num2 + num3
    check = False
    if num_sum == 1000:
        check = True

    return check


b = 1
c = 2
check1000 = False
while b < 999:
    while c < 999:
        a2 = c ** 2 - b ** 2
        a = a2 ** (1 / 2)
        if a.is_integer():
            check1000 = check_sum(a, b, c)
            if check1000:
                print(a * b * c)
                break
            else:
                c += 1
        else:
            c += 1

    if check1000:
        break
    else:
        b += 1
        c = b + 1


