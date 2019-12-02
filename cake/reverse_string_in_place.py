# import unittest


list_of_chars = ['a', 'b', 'c', 'f', 'a', 'w', 'q']

def reverse(list_of_chars):
    end_of = len(list_of_chars) - 1
    start_of = 0
    while start_of < end_of:
        # cup = list_of_chars[start_of]
        list_of_chars[start_of], list_of_chars[end_of] = list_of_chars[end_of],  list_of_chars[start_of]
        # list_of_chars[end_of] = cup
        end_of -= 1
        start_of += 1

    return list_of_chars

print(reverse(list('rat the ate cat the')))


