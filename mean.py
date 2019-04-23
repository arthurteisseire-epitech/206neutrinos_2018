from math import sqrt


def algo(n, a, h, sd):
    while True:
        n, a, h, sd = get_input(n, a, h, sd)


def get_input(n, a, h, sd):
    value = input("Enter next value: ")
    try:
        return mean(n, a, h, sd, int(value))
    except ValueError as e:
        print(e)
        return n, a, h, sd


def mean(n, a, h, sd, value):
    n += 1
    a = (a * (n - 1) + value) / n
    sd = sqrt(pow(a, 2) / (n - 1))
    print_all(n, a, h, sd, 0)
    return n, a, h, sd


def print_all(n, a, h, sd, rms):
    print("\tNumber of values:\t%d" % n)
    print("\tStandard deviation:\t%.2f" % sd)
    print("\tArithmetic mean:\t%.2f" % a)
    print("\tRoot mean square:\t%.2f" % rms)
    print("\tHarmonic mean:\t\t%.2f" % h)
    print("")
