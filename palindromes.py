import string


def is_palindromes(sentence):
    """
    A method that returns whether or not a sentence or phrase is a palindrome
    :param sentence: String
    :return: True/False
    """
    if len(sentence) < 1:
        return True
    elif ' ' in sentence:
        return is_palindromes(sentence.replace(' ', ''))
    elif sentence[0].lower() == sentence[-1].lower():
        return is_palindromes(sentence[1:-1])
    else:
        return False

import string
def is_palindrome_loop(sentence):
    s = sentence.replace(' ', '').lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    print(s)
    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            return False
    return True

print(is_palindromes('Abc deffedcba'))
print(is_palindrome_loop('Abc deffedcba'))

b = "asdasd? asdasd. asdasd#$#@#asdasddfrgdfghf!!!@@#sdfsdffdsfds#@@!!!fhgfdgrfddsadsa#@#$#dsadsa .dsadsa ?dsadsa"
print(is_palindrome_loop(b))
print(is_palindromes(b))

