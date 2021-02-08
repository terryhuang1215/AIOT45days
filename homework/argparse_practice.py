import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-name')
parser.add_argument('-ID')
args = parser.parse_args()
print("Name:", args.name)
print("ID:", args.ID)
