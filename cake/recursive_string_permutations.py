def get_permutations(string):

    # Generate all permutations of the input string
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last )

    permutations = set()

    for permutation_of_all_chars_except_last  in permutations_of_all_chars_except_last :
        print("permutation_of_all_chars_except_last %s" % permutation_of_all_chars_except_last)
        print("range %s" % range(len(permutation_of_all_chars_except_last) + 1))
        for position in range(len(permutation_of_all_chars_except_last) + 1):
            permutation = (permutation_of_all_chars_except_last [:position] + last_char  + permutation_of_all_chars_except_last [position:])
            permutations.add(permutation)
    return permutations


print(get_permutations("abc"))
