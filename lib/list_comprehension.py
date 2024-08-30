#!/usr/bin/env python3

def return_evens(num_list):
    '''Returns a list of all even elements from the given list of integers.'''
    return [x for x in num_list if x % 2 == 0]

def make_exclamation(sentence_list):
    '''Returns a list of sentences with an exclamation mark at the end of each sentence.'''
    return [sentence + '!' for sentence in sentence_list]