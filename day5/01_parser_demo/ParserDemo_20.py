from argparse import ArgumentParser
from getpass import getpass

parser = ArgumentParser(description='Password Hiding Demo')
parser.add_argument('username', help='provide username')

args = parser.parse_args()

# request to enter password and hide entered characters
args.password = getpass('Password:')

print('username:', args.username)
print('password:','*'*len(args.password))
