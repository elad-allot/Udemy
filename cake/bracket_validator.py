def is_valid(code):
    if not code:
        return True
    open_ps = []
    checker = {')': '(', '}': '{', ']': '['}
    for i in range(len(code)):
        if code[i] in ('(', '{', '['):
            open_ps.append(code[i])
        if code[i] in (')', '}', '}'):
            if checker[code[i]] != open_ps.pop():
                return False
    return True


print(is_valid(''))

# checker = {')': '(', '}': '{', ']': '['}
#
# print(checker)
