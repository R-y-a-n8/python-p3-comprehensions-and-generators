#!/usr/bin/env python3

def return_evens(sequence):
    """Return a list of all even elements in the given sequence of integers."""
    return [n for n in sequence if n % 2 == 0]

def make_exclamation(sentences):
    """Return a list of sentences with exclamation marks at the end."""
    return [sentence + "!" for sentence in sentences]
