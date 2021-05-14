def divisible(number):
    i = 2
    div = False
    while i < 21:
        quotient = number / i
        if quotient.is_integer():
            if i == 20:
                div = True
                break
            else:
                i += 1
        else:
            div = False
            break
    return div


num = 2520
while True:
    div_ans = divisible(num)
    if div_ans:
        print(num)
        break
    else:
        num += 1
