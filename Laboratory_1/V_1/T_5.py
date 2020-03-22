"""
Користувач уводить ціни 1 кг цукерок і 1 кг печива. Знайти вартість: а) однієї покупки з 300 г цукерок і 400 г печива; б) трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок.
The user enters prices of 1 kg of candy and 1 kg of cookies. Find the cost of: a) one purchase of 300 g of candy and 400 g of cookies; b) three purchases, each with 2 kg of cookies and 1 kg of 800 g of candy.
"""

def in_put_for_a():
    a = input("Enter price of 1 kg of candy.\na is a number: ")
    if a.isdigit():
        return a
    else:
        print("Mistake")
        return in_put_for_a()
# a = price of 1 kg of candy

def in_put_for_b():
    b = input("Enter price of 1 kg of cookies.\na is b number: ")
    if b.isdigit():
        return b
    else:
        print("Mistake")
        return in_put_for_b()
# b = price of 1 kg of cookies

def main():
    a = int(in_put_for_a())
    b = int(in_put_for_b())
    answer_1 = round(0.3*a + 0.4*b,1)
    answer_2 = round(3*(2*a + 1.8*b),1)
    return print("Вартість однієї покупки з 300 г цукерок і 400 г печива: " + str(answer_1) + "\n" + "Вартість трьох покупок, кожна з 2 кг печива і 1 кг 800 г цукерок: " + str(answer_2) + "\n")

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))