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
    print_all(n, a, h, sd)
    return n, a, h, sd


def print_all(n, a, h, sd):
    print("\tNumber of values:\t%d" % n)
    print("\tStandard deviation:\t%d" % sd)
    print("\tArithmetic mean:\t%d" % a)
    print("\tRoot mean square:\t0")
    print("\tHarmonic mean:\t\t%d" % h)
    print("")
