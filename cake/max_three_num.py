list_of_ints = [-10, -10, 1, 3, 2]
# list_of_ints = [11, 2, 3, 4, 5, 6]

def max_three(list_of_ints):
    max_p1 = 0
    max_p2 = 0
    min_n1 = 0
    min_n2 = 0
    third = 0

    for curr_num in list_of_ints:
        if curr_num < 0:  # negative
            if curr_num <= min_n2:
                min_n2 = curr_num
            if curr_num <= min_n1:
                min_n2 = min_n1
                min_n1 = curr_num
        else:  # positive
            if curr_num >= third:
                third = curr_num
            if curr_num >= max_p2:
                third = max_p2
                max_p2 = curr_num
            if curr_num >= max_p1:
                third = max_p2
                max_p2 = max_p1
                max_p1 = third

    return max(max_p1 * max_p2 * third, max_p1 * min_n1 * min_n2)

# print (max_three(list_of_ints))


for i in range(len(list_of_ints)):
    # print ("i: %s" % i)
    # print (list_of_ints[i])
    print (list_of_ints[(i * -1) -1])