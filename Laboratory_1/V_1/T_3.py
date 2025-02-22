"""
Катети прямокутного трикутника уводяться з клавіатури. Обчислити довжину гіпотенузи, периметр і площу цього трикутника. Відповідь дати з точністю до 10 знаків після коми.
The rectangular triangle catheters are entered from the keyboard. Calculate the length of the hypotenuse, the perimeter, and the area of this triangle. Answer up to 10 decimal places.
"""
from math import sqrt

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
    hyp = round(sqrt(a * a + b * b),10)
    perimeter = round(hyp + a + b,10)
    area = round((a * b)/2,10)
    return print("Гипотенуза "+str(hyp)+"\n"+"Периметр "+str(perimeter)+"\n"+"Площадь "+str(area))

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))