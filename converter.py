from typing import Literal


def integer(number: float) -> int:
    return int(number)


def breakline(number: int = 1) -> Literal[1]:
    print((number - 1) * "\n")
    return 1


units = [
    "Millimetre(mm)",
    "Centimetre(cm)",
    "Metre(m)",
    "Kilometre(km)",
    "Inch(in)",
    "Foot(ft)",
    "Yard(yd)",
    "Mile(mi)",
]

value = {
    (0, 1): 0.1,
    (0, 2): 0.001,
    (0, 3): 0.000001,
    (0, 4): 0.0393701,
    (0, 5): 0.00328084,
    (0, 6): 0.00109361,
    (0, 7): 0.000000621371,
    (1, 0): 10,
    (1, 2): 0.01,
    (1, 3): 0.00001,
    (1, 4): 0.3937,
    (1, 5): 0.0328084,
    (1, 6): 0.0109361,
    (1, 7): 0.00000621371,
    (2, 0): 1000,
    (2, 1): 100,
    (2, 3): 0.001,
    (2, 4): 39.37,
    (2, 5): 3.28,
    (2, 6): 1.094,
    (2, 7): 0.000621371,
    (3, 0): 1000000,
    (3, 1): 100000,
    (3, 2): 1000,
    (3, 4): 39370.1,
    (3, 5): 3280.84,
    (3, 6): 1093.61,
    (3, 7): 0.62137119224,
    (4, 0): 25.4,
    (4, 1): 2.54,
    (4, 2): 0.0254,
    (4, 3): 0.0000254,
    (4, 5): 12,
    (4, 6): 0.0277778,
    (4, 7): 0.0000157828,
    (5, 0): 304.8,
    (5, 1): 30.48,
    (5, 2): 0.3048,
    (5, 3): 0.0003048,
    (5, 4): 12,
    (5, 6): 0.333334,
    (5, 7): 0.000189394,
    (6, 0): 914.4,
    (6, 1): 91.44,
    (6, 2): 0.9144,
    (6, 3): 0.0009144,
    (6, 4): 36,
    (6, 5): 3,
    (6, 7): 0.000568182,
    (7, 0): 1609344000,
    (7, 1): 160934.4,
    (7, 2): 1609.344,
    (7, 3): 1.60934,
    (7, 4): 63360,
    (7, 5): 5280,
    (7, 6): 1760,
}

if __name__ == "__main__":
    index = 1
    for unit in units:
        print(f"{index}. {unit}")
        index += 1

    breakline(2)

    unit = int(input("From Index: ")) - 1
    convert = int(input("To Index: ")) - 1
    number = integer(float(input("Number To Convert: ")))

    breakline()

    if unit == convert:
        print(f"{number} {units[unit]} = {number} {units[unit]}")

    unitRange = range(len(units))
    if unit in unitRange and convert in unitRange:
        converted = integer(number * value[(unit, convert)])
        print(f"{number} {units[unit]} = {converted} {units[convert]}")
