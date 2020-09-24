#!/usr/bin/python

import sys
import argparse
import random
import myFile

usage = 'usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]'
fulluse = "usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\nGenerate a secure, memorable " \
          "password using the XKCD method\n\noptional arguments:\n    -h, --help            show this help message " \
          "and exit\n    -w WORDS, --words WORDS\n                          include WORDS words in the password (" \
          "default=4)\n    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n                    " \
          "      (default=0)\n    -n NUMBERS, --numbers NUMBERS\n                          insert NUMBERS random " \
          "numbers in the password\n                          (default=0)\n    -s SYMBOLS, --symbols SYMBOLS\n       " \
          "                   insert SYMBOLS random symbols in the password\n                          (default=0) "

def main(argv):
    parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method', \
            epilog="https://www.xkcd.com/936/")

    parser.add_argument('-w', '--words', dest="WORDS", type=int, default=4, help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', dest="CAPS", type=int, default=0, help='capitalize the first letter of CAPS random words'\
    '                          (default=0)')
    parser.add_argument('-n', '--numbers', dest="NUMBERS", type=int, default=0, help='insert NUMBERS random numbers in the password'\
    '                          (default=0)')
    parser.add_argument('-s', '--symbols', dest="SYMBOLS", type=int, default=0, help='insert SYMBOLS random symbols in the password'\
    '                          (default=0)')

    try:
        args = parser.parse_args()
        print(generate(args.WORDS, args.CAPS, args.NUMBERS, args.SYMBOLS))
    except IOError:
        print(usage)

def generate(w, c, n, s):
    if w < 0:
        w = 0
    if c > w:
        c = w
    if c < 0:
        c = 0
    if n < 0:
        n = 0
    if s < 0:
        s = 0

    r_list = random.sample(myFile.my_word_list, k=w-c)
    c_list = [i.capitalize() for i in random.choices(myFile.my_word_list, k=c)]
    n_list = [str(i) for i in random.choices(myFile.my_num_list, k=n)]
    s_list = random.choices(myFile.my_special_list, k=s)

    full_list = random.sample(r_list + c_list + n_list + s_list, w+n+s)

    pw = ''.join(full_list)
    return pw


if __name__ == "__main__":
   main(sys.argv[1:])