from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('echo', help='echo the string you use here')

args = parser.parse_args()
print(args.echo)

