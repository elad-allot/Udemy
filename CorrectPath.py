

def CorrectPath(strr):
    x_dict = {'r': 1, 'l': -1, 'u': 0, 'd': 0}
    y_dict = {'r': 0, 'l': 0, 'u': -1, 'd': 1}
    qm = 0
    directions = list(strr)
    x, y = 0, 0
    for i in directions:
        try:
            x = x + x_dict[i]
            y = y + y_dict[i]
        except KeyError:
            qm += 1
        if not (0 <= x < 5 and 0 <= y < 5):
            raise ValueError("out of bounds!")

    for i in range(len(directions)):
        if directions[i] not in x_dict.keys():
            if y < 4:
                directions[i] = 'd'
                y += 1
            else:
                directions[i] = 'r'
                x += 1
    return directions


print(CorrectPath("r?d?drdd"))


