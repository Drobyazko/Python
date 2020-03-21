"""
Скласти програму переведення радіанної міри кута в градуси, хвилини і секунди.
Compile a program to translate the radial angle measure into degrees, minutes and seconds.
"""


def change():
    one = switch_to_change(input("Enter 1 to get Minutes to seconds,\n2 to get Radial to degrees\nand 0 to Finish: "))
    if one == "Minutes to seconds":
        t = input("Enter Minutes: ")
        return correct_t(t)
    elif one == "Radial to degrees":
        s = input("Enter Number: ")
        return correct_s(s)
    elif one == "Finish":
        print("The End")
    else:
        return change()

def main_for_T(t):
    y = t * 60
    answer_t = str(str(t) + " minutes = " + str(y) + " seconds")
    return print(answer_t)

def main_for_S(s):
    z = s * 180/3.14
    answer_s = str(str(s) + " rad = " + str(z) + " deg")
    return print(answer_s)

def correct_s(s):
    if s.isdigit():
        s = int(s)
        return main_for_S(s)
    else:
        s = input("Change your enter: ")
        correct_s(s)

def correct_t(t):
    if t.isdigit():
        t = int(t)
        return main_for_T(t)
    else:
        t = input("Change your enter: ")
        correct_t(t)

def main():
     return change()

def switch_to_change(argument):
    switcher = {
        "0": "Finish",
        "1": "Minutes to seconds",
        "2": "Radial to degrees"
    }
    one = switcher.get(argument)
    return one

non = 1
while non != 0:
    main()
    non = int(input("Enter 1 to continue: "))