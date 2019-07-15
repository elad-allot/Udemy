

def is_palindromes(sentence):
    if len(sentence) < 1:
        return True
    elif ' ' in sentence:
        return is_palindromes(sentence.replace(' ', ''))
    elif sentence[0].lower() == sentence[len(sentence) - 1].lower():
        return is_palindromes(sentence[1:len(sentence) - 1])
    else:
        return False





