"""
Дійсні числа a і b уводяться з клавіатури. Для a обчислити відсоток b від цього числа.
The numbers a і b are taken away from the keyboard. For a, calculate the number b of the whole number.
"""

def in_put_for_a():
    a = input("Enter your a.\na is a number: ")
    correct(a)
    return a

def in_put_for_b():
    b = input("Enter your b.\na is b number: ")
    correct(b)
    return b

def correct(x):
    if x.isdigit():
        return x
    else: return in_put_for_a()

def main():
    a = int(in_put_for_a())
    b = int(in_put_for_b())
    answer = (b/a)*100
    return print(answer)

non = 1
while non != 0:
    main()
    non = int(input("Enter 1 to continue: "))