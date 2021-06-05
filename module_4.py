import math

print('(1)')
x = 1
for x in range(1, 6):
    print(x)
    x += 1

print()

print('(2)')
print(3 + 4)
print()
print('(3)')
print(math.pi + math.sqrt(2))
print()
print('(4)')
print(math.sin(math.pi / 6) + math.cos(math.pi / 6))
print()

print('(5)')
x = input('Enter first value: ')
y = input('Enter second value: ')
z = input('Enter third value: ')

print(str(x).ljust(6), str(y).ljust(6), str(z).ljust(6))
print()

print('(6)')
radius = int(input('Enter radius: '))
area = math.pi * (radius ** 2)
print(area)
print()

print('(7)')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(max([x, y]))
print()

print('(8)')
val_1 = input('Enter T or F: ')
val_2 = input('Enter T or F: ')
inputs = [val_1, val_2]
i = 0
while i < len(inputs):
    if inputs[i] == 'T':
        inputs[i] = 1
    else:
        inputs[i] = 0
    i += 1

print(not (inputs[0] and inputs[1]))
print()

int_sum = 0
for n in range(1, 11):
    int_sum += n
print('(9)')
print(int_sum)
print()

int_sum_2 = 0
n = 1
while n < 11:
    int_sum_2 += n
    n += 1
print('(10)')
print(int_sum_2)

