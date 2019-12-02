import time
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def find_rotation_point_long(words):
    if not words:
        raise ValueError("no list")

    if len(words) < 2:
        return 0

    for i in range(1, len(words)):
        if words[i - 1] > words[i]:
            return i

    return 0



def find_rotation_point(words):
    if not words:
        raise ValueError("no list")

    if len(words) < 2:
        return 0
    s_range = 0
    # m_range = int(len(words) / 2)
    e_range = len(words) - 1
    while s_range + 1 < e_range:
        m_range = s_range + int((e_range - s_range) / 2)
        if words[m_range] > words[e_range]:
            s_range = m_range
            # m_range = int((e_range - s_range) / 2)
        elif words[s_range] > words[m_range]:
            e_range = m_range
            # m_range = int((m_range - s_range) / 2)
        else:
            return s_range
    return e_range

    # pass


# actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
#                               'undulate', 'xenoepist', 'asymptote',
#                               'babka', 'banoffee', 'engender',
#                               'karpatka', 'othellolagkage'])

actual = find_rotation_point(['w', 'z', 'a', 'b', 'c', 'd'])

print(actual)