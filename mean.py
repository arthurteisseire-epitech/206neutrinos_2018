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
    print(value)
    return n, a, h, sd
