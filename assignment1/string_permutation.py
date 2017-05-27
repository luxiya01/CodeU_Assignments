import string
import collections

def string_permutation(str1, str2):
    """Checks whether str1 and str2 are permutations of 
    each other. Note that the function is case insensitive. """

    if not ((str.isalpha(str1) or str1 == "") 
            and (str.isalpha(str2) or str2 == "")):
        raise ValueError("The inputs strings shall only consist of English alphabets")
    str1 = str1.lower()
    str2 = str2.lower()
    inputs = collections.defaultdict(lambda: 0)
    for c in str1: 
        inputs[c] += 1
    for c in str2: 
        inputs[c] -= 1
    return all(c == 0 for c in inputs.values())
