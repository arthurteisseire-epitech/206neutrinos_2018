import argparse


def positive_int(n):
    n = int(n)
    if n < 0:
        raise argparse.ArgumentTypeError("n and sd must be positive int")
    return n


def non_null_positive_int(n):
    n = int(n)
    if n <= 0:
        raise argparse.ArgumentTypeError("n and sd must be positive int")
    return n


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=positive_int, help="number of values")
    parser.add_argument("a", type=int, help="arithmetic mean")
    parser.add_argument("h", type=non_null_positive_int, help="harmonic mean")
    parser.add_argument("sd", type=positive_int,  help="standard deviation")
    args = parser.parse_args()
    return args
