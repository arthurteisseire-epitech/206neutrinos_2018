import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="number of values")
    parser.add_argument("a", type=int, help="arithmetic mean")
    parser.add_argument("h", type=int, help="harmonic mean")
    parser.add_argument("sd", type=int, help="standard deviation")
    args = parser.parse_args()
    return args
