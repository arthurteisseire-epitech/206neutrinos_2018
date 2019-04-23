from math import sqrt


def algo(n, a, h, sd):
    while True:
        n, a, h, sd = get_input(n, a, h, sd)


def get_input(n, a, h, sd):
    value = input("Enter next value: ")
    if value == "END":
        raise Exception
    try:
        return mean(n, a, h, sd, int(value))
    except ValueError as e:
        print(e)
        return n, a, h, sd


def mean(n, a, h, sd, value):
    n += 1
    h = n / ((1 / value) + ((n - 1) / h))
    exisquare = (n - 1) * (pow(sd, 2) + pow(a, 2))
    rms = sqrt((exisquare + pow(value, 2)) / n)
    a = (a * n + value) / (n + 1)
    sd = sqrt((n / (n + 1)) * (pow(sd, 2) + (pow(value - a, 2) / (n + 1))))
    print_all(n, a, h, sd, rms)
    return n, a, h, sd


def print_all(n, a, h, sd, rms):
    print("\tNumber of values:\t%d" % n)
    print("\tStandard deviation:\t%.2f" % sd)
    print("\tArithmetic mean:\t%.2f" % a)
    print("\tRoot mean square:\t%.2f" % rms)
    print("\tHarmonic mean:\t\t%.2f" % h)
    print("")
