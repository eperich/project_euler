import sympy as sym

num = int(input("Enter a number:"))

i = 2

while i < num:
    if num % i == 0:
        factor = int(num / i)
        if sym.isprime(factor):
            print(factor)
            break
    i += 1

