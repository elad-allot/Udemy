def diff_words(str1, str2):

    if not str1 or not str2:
        return str1.split() + str2.split()

    set1 = set(str1.split())
    set2 = set(str2.split())

    s1 = set1.difference(set2)
    s2 = set2.difference(set1)
    return s1.union(s2)


print(diff_words("a b c d", "a b c e"))
