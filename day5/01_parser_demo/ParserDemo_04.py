from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', help='display a square of a given number')

args = parser.parse_args()
print(args.square**2)

