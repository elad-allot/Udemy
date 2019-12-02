int_list = [1, 2, 3, 7, 5, 6, 7, 8, 9, 11, 10, 12]

def find_dup(int_list):
    dict = {}
    for new_key in int_list:
        v = dict.get(new_key)
        if not v:
            dict[new_key] = 1
        else:
            return new_key


def find_dup2(int_list2):
    if len(int_list2) < 2:
        raise ValueError("at lease 2")
    int_list2.sort()
    print(int_list2)
    for i in range(1,len(int_list2)):
        if int_list2[i] == int_list2[i - 1]:
            return int_list2[i]




print(find_dup2(int_list))