int_list = [1, 7, 0, 4]



def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise ValueError("need at lease 2 ")
    
    before = 1
    after = 1
    new_list_forward = [1] * len(int_list)
    new_list_backward = [1] * len(int_list)
    for i in range(1, len(int_list)):
        before = before * int_list[i -1]
        new_list_forward[i] = before
    for i in range(len(int_list) - 1, 0, -1):
        after = after * int_list[i]
        new_list_backward[i-1] = after
    for i in range(len(int_list)):
        new_list_forward[i] = new_list_backward [i] * new_list_forward[i]

    return new_list_forward

print(get_products_of_all_ints_except_at_index(int_list))


