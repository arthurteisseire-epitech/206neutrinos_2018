def algo(n, a, h, sd):
    while True:
        mean(n, a, h, sd)


def mean(n, a, h, sd):
    value = input("Enter next value: ")
    try:
        value = int(value)
    except ValueError as e:
        print(e)
