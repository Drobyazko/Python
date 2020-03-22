"""
Дано значення температури в градусах Цельсія. Вивести температуру в градусах Фаренгейта.
The temperature in degrees Celsius is given. Display the temperature in degrees Fahrenheit.
"""

def in_put_for_a():
    a = input("Enter your a.\na is a number: ")
    if a.isdigit():
        return a
    else: return in_put_for_a()

def main():
    a = int(in_put_for_a())
    answer = (a * 9/5) + 32
    return print(str(a)+" degrees Celsius = " + str(answer) + "degrees Fahrenheit")

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))