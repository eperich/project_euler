def palindrome_check(number):
    num_string = str(number)
    num_len = len(num_string)
    i = 0
    j = num_len - 1
    middle = int(num_len / 2)
    check = False
    while i + 1 <= middle:
        first_half = num_string[i]
        last_half = num_string[j]
        if first_half == last_half:
            if i + 1 == middle:
                check = True
                break
            else:
                i = i + 1
                j = j - 1
        else:
            check = False
            break
    return check


palindrome_list = []
for x in range(1, 1000):
    for y in range(1, 1000):
        product = x * y
        if palindrome_check(product):
            palindrome_list.append(product)

max_palindrome = max(palindrome_list)
print(max_palindrome)
