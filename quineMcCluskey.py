# FILE: quineMcCluskey.py
# Caroline Katko
# Quine McCluskey implementation

from utils import *

# quine_McCluskey
# takes in a list of binary terms and returns a list of the terms that make up the minimum combination
def quine_McCluskey(binary_list):
    final_terms_list = combine_terms(binary_list)
    terms_and_ancestors_map = create_map(final_terms_list) 
    return find_minimum_combination(terms_and_ancestors_map, final_terms_list, binary_list)
