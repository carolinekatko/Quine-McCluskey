# FILE: main.py
# Caroline Katko
# main program for the Quine McCluskey implementation

import sys
from quineMcCluskey import quine_McCluskey
from utils import *

def main():
    equation_list = []
    letters = []
    equation_file = sys.argv[1]

    with open(equation_file) as f:
        for line in f:
            equation_list.append(line.strip())

    letters = get_letters_in_equation(equation_list) 
    equation_binary = convert_all_terms_to_binary(equation_list)
    quine_McCluskey_terms = quine_McCluskey(equation_binary)
    equation_letters = convert_all_binary_to_letters(quine_McCluskey_terms, letters)
    print("The minimized circuit is:")
    for i in range(len(equation_letters)):
        print(equation_letters[i])

if __name__ == "__main__":
    main()