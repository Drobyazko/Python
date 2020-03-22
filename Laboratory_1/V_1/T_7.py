"""
Користувач уводить суму вкладу в банк і річний відсоток. Знайти суму вкладу через 5 років (розглянути два способи нарахування відсотків)
The user enters the amount of the deposit into the bank and the annual interest. Find your deposit amount in 5 years (consider two ways to calculate interest)
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
    answer_1 = a+a*(b/100)*5
    # Простий відсоток
    answer_2 = round(a*(1+b/100)**5,2)
    # Складний відсоток
    return print(str(answer_1)+"\n"+str(answer_2))

non = 1
while non == 1:
    main()
    non = int(input("Enter 1 to continue: "))