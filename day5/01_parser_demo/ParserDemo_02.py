from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('echo')

args = parser.parse_args()
print(args.echo)

