def get_closing_paren(sentence, opening_paren_index):
    # Fid the position of the matching closing parenthesis
    if len(sentence) + 1 < opening_paren_index:
        return -1

    counter = 1
    for i in range (opening_paren_index + 1, len(sentence)):
        if sentence[i] == '(':
            counter += 1
        elif sentence[i] == ')':
            counter -= 1

        if counter == 0:
            return i
    return -1


print(get_closing_paren('()(()', 2))