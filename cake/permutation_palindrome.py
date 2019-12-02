



def has_palindrome_permutation(the_string):
    letter_dict = {}
    for i in range(len(the_string)):
        letter_dict[the_string[i]] = (letter_dict.get(the_string[i]) or 0) + 1
    odd = 0
    print(letter_dict)
    for k in letter_dict:
        if letter_dict.get(k) % 2 == 1:
            odd += 1

    return 0 <= odd <= 1

print (has_palindrome_permutation("aabbccd"))