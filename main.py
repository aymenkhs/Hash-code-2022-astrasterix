import argparse

import input
import output

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="""name of file can be 'a' or 'b' or 'c' or 'd' or 'e'""")
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.file not in ('a','b','c','d','e'):
        raise ValueError("argument file (-f) must be equal to 'a' or 'b' or 'c' or 'd' or 'e'")
    
    # code our solution here

if __name__ == '__main__':
    main()