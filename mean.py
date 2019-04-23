def algo(n, a, h, sd):
    while True:
        get_input(n, a, h, sd)


def get_input(n, a, h, sd):
    value = input("Enter next value: ")
    try:
        mean(n, a, h, sd, int(value))
    except ValueError as e:
        print(e)


def mean(n, a, h, sd, value):
    print(value)
