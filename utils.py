# FILE: utils.py
# Caroline Katko
# helper functions for the Quine McCluskey implementation

from collections import defaultdict
import itertools
import sys

# differs_by_one
# returns true if two strings differ by one character
def differs_by_one(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count == 1

# is_one_diff_remaining
# returns true if there are two or more strings that differ by one
def is_one_diff_remaining(a_list):
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            if differs_by_one(a_list[i], a_list[j]):
                return True  
    return False

# create_map
# returns a map of terms to their ancestors
def create_map(a_list):
    the_map = defaultdict(list)
    for i in range(len(a_list)):
        the_map[a_list[i]].extend(determine_ancestry(a_list[i]))
    return the_map

# replace_with_dash
# returns a string with all characters that are different between two strings replaced with a dash
def replace_with_dash(string1, string2):
    new_string = ""
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            new_string += "-"
        else:
            new_string += string1[i]
    return new_string

# remove_duplicates
# returns a list with all duplicates removed
def remove_duplicates(a_list):
    return list(dict.fromkeys(a_list))

# determine_ancestry
# returns a list of all possible ancestors of a term
def determine_ancestry(term):
    dash_count = 0
    for char in term:
        if char == "-":
            dash_count += 1
    ancestors = ["" for x in range(2**dash_count)]
    for char in term:
        if char == "-":
            ancestors = [x + "0" for x in ancestors] + [x + "1" for x in ancestors]
        else:
            ancestors = [x + char for x in ancestors]
    return remove_duplicates(ancestors)

# combine_terms
# returns a list of all terms after they have all been combined
def combine_terms(a_list):
    while is_one_diff_remaining(a_list):
        things_to_add = []
        things_to_remove = []
        for i in range(len(a_list)):
            for j in range(i + 1, len(a_list)):
                if differs_by_one(a_list[i], a_list[j]):
                    things_to_add.append(replace_with_dash(a_list[i], a_list[j]))
                    things_to_remove.append(a_list[i])
                    things_to_remove.append(a_list[j])
        a_list = [x for x in a_list if x not in things_to_remove]
        a_list.extend(things_to_add)
        a_list = remove_duplicates(a_list)
    return a_list

# find_minimum_combination
# returns a list of all the terms that make up the minimum combination
def find_minimum_combination(ancestors_map, terms_list, original_terms_list):
    final_answer = []
    for element in range(1, len(terms_list) + 1):
        found_flag = False
        for combo in itertools.combinations(terms_list, element):
            temp_list = []
            for term in combo:
                temp_list.extend(ancestors_map[term])
            temp_set = set(temp_list)
            if temp_set == set(original_terms_list):
                final_answer = list(combo)
                found_flag = True
                break
        if found_flag:
            break
    return final_answer

# convert_term_to_binary
# returns a binary string of a term
def convert_term_to_binary(term):
    term = list(term)
    binary_term = []
    negative_flag = False
    for i in range(len(term)):
        if term[i] == "-":
            negative_flag = True
            continue
        if negative_flag:
            term[i] = "0"
        else:
            term[i] = "1"
        binary_term.append(term[i])
        negative_flag = False
    return "".join(binary_term)

# convert_all_terms_to_binary
# returns a list of all the terms converted to binary
def convert_all_terms_to_binary(equation_list):
    equation_binary = []
    for i in range(len(equation_list)):
        equation_binary.append(convert_term_to_binary(equation_list[i]))
    return equation_binary

# get_letters_in_equation
# returns a list of all the letters in an equation
def get_letters_in_equation(equation_list):
    letters = []
    term = equation_list[0]
    for char in term:
        if char != "-":
            letters.append(char)
    return letters

# convert_binary_term_to_letters
# returns a string of all the letters in a binary term
def convert_binary_term_to_letters(binary_string, letters_in_original):
    new_binary_term = []
    for i in range(len(binary_string)):
        if binary_string[i] == "1":
            new_binary_term.append(letters_in_original[i])
        if binary_string[i] == "0":
            new_binary_term.append("-" + letters_in_original[i])
    return "".join(new_binary_term)

# convert_all_binary_to_letters
# returns a list of all the binary terms converted to letters
def convert_all_binary_to_letters(equation_binary, letters_in_original):
    equation_letters = []
    for i in range(len(equation_binary)):
        equation_letters.append(convert_binary_term_to_letters(equation_binary[i], letters_in_original))
    return equation_letters

def check_for_file():
    if len(sys.argv) != 2:
        print("Usage: python main.py <equation_file>")
        sys.exit(1)