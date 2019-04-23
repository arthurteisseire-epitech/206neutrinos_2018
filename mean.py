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
    print_all(n, a, h, sd)
    return n, a, h, sd


def print_all(n, a, h, sd):
    print("\tNumber of values:\t%d" % n)
    print("\tStandard deviation:\t%.2f" % sd)
    print("\tArithmetic mean:\t%.2f" % a)
    print("\tRoot mean square:\t%.2f")
    print("\tHarmonic mean:\t\t%.2f" % h)
    print("")
