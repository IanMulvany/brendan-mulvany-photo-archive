import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(
    description="list the contents of a directory",
    epilog="we hope you enjoyed using this utility!",
)

# Add the arguments
my_parser.add_argument(
    "Path", metavar="path", type=str, action="store", help="directory to be listed"
)
my_parser.add_argument(
    "-l", "--long", action="store_true", help="enable long listing of contents"
)
my_parser.add_argument(
    "-v", "--version", action="version", help="version number of this script"
)

# Execute the parse_args method
args = my_parser.parse_args()
args.version = 3

input_path = args.Path

if not os.path.isdir(input_path):
    print("this path does not exist")
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size = os.stat(os.path.join(input_path, line)).st_size
        line = "%10d %s" % (size, line)
    print(line)

print("mischeif managed! again")
