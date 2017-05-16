import string 

def string_permutation(str1, str2):
    if str.isalpha(str1 and str2):
        str1 = str1.lower()
        str2 = str2.lower()
        result = True
        inputs = {x: 0 for x in string.ascii_lowercase} 
        for c in str1: 
            inputs[c] += 1
        for c in str2: 
            inputs[c] -= 1
        for c in inputs.keys():
            if inputs[c] != 0:
                result = False
                break
        return result
    else: 
        raise ValueError("The inputs strings shall only consist of English alphabets")

