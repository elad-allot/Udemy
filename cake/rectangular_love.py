def find_rectangular_overlap_bad(rect1, rect2):
    # Calculate the overlap between the two rectangles

    #case rect2 lower
    if rect1['left_x'] > rect2['left_x'] and rect1['bottom_y'] > rect2['bottom_y']:
        return find_rectangular_overlap(rect2, rect1)

    new_rect = dict()
    new_rect['left_x'] = rect2['left_x']
    new_rect['bottom_y'] = rect2['bottom_y']

    new_rect['width'] = rect1['width'] - rect2['left_x']
    new_rect['height'] = rect1['height'] - rect2['height']

    return new_rect


def is_point_greater(p1, p2):
    """
    if p1 >= p2 True
    else False
    :param p1:(x,y) tuple
    :param p2:(x,y) tuple
    :return: bool
    """
    return p1[0] >= p2[0] and p1[1] >= p2[1]


def find_rectangular_overlap(rect1, rect2):
    if rect1['left_x'] > rect2['left_x'] and rect1['bottom_y'] > rect2['bottom_y']:
        return find_rectangular_overlap(rect2, rect1)
    p11 = (rect1['left_x'], rect1['bottom_y'])
    p12 = (rect1['left_x'] + rect1['width'], rect1['bottom_y'] + rect1['height'])
    p21 = (rect2['left_x'], rect2['bottom_y'])
    p22 = (rect2['left_x'] + rect2['width'], rect2['bottom_y'] + rect2['height'])

    # Case outside
    if is_point_greater(p21, p12):
        return {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}
    #case partial
    elif is_point_greater(p21, p11) and is_point_greater(p22, p12):
        new_rect = dict()

        new_rect['left_x'] = rect2['left_x']
        new_rect['bottom_y'] = rect2['bottom_y']

        new_rect['width'] = p12[0] - p21[0]
        new_rect['height'] = p12[1] - p21[1]

        return new_rect
    #case inside
    elif is_point_greater(p21, p11) and is_point_greater(p12, p21):
        return rect2


rect1 = {
    'left_x': 1,
    'bottom_y': 1,
    'width': 2,
    'height': 2,
}
rect2 = {
    'left_x': 4,
    'bottom_y': 6,
    'width': 3,
    'height': 6,
}
expected = {
    'left_x': None,
    'bottom_y': None,
    'width': None,
    'height': None,
}
actual = find_rectangular_overlap(rect1, rect2)
print(actual)

# a = (1,2,3,4)
# print("%s" % (a,))