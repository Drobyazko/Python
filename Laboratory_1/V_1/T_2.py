"""
Дійсні числа a і b уводяться з клавіатури. Для a обчислити відсоток b від цього числа.
The numbers a і b are taken away from the keyboard. For a, calculate the number b of the whole number.
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

def main():
    a = int(in_put_for_a())
    b = int(in_put_for_b())
    answer = (b/a)*100
    return print(answer)

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))