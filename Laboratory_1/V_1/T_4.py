"""
Користувач уводить три числа. Збільшити перше число в два рази, друге числа зменшити на 3, третє число звести в квадрат і потім знайти суму нових трьох чисел.
The user enters three numbers. Increase the first number twice, reduce the second numbers by 3, reduce the third number to a square and then find the sum of the new three numbers.
"""

def in_put_for_a():
    a = input("Enter your a.\na is a number: ")
    if a.isdigit():
        return a
    else: return in_put_for_a()

def in_put_for_b():
    b = input("Enter your b.\na is b number: ")
    if b.isdigit():
        return b
    else: return in_put_for_b()

def in_put_for_c():
    c = input("Enter your c.\na is c number: ")
    if c.isdigit():
        return c
    else: return in_put_for_c()

def main():
    a = int(in_put_for_a())
    b = int(in_put_for_b())
    c = int(in_put_for_c())
    answer = a*2 + b - 3 + c*c
    return print("answer " + str(answer))

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))