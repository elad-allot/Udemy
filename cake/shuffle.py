import random


def shuffle (shuffle_list):
    # # print(len(shuffle_list))
    # print("shuffle_list %s" % shuffle_list)
    # if new_list is None:
    #     new_list = []
    #
    # if len(shuffle_list) > 1:
    #     rand_num = get_random(0, len(shuffle_list) )
    #     return shuffle(shuffle_list[:rand_num] + shuffle_list[rand_num + 1:], new_list.append(shuffle_list[rand_num]))
    # else:
    #     print("last one %s" % new_list)
    #     return new_list.append(shuffle_list[0])
    new_list = []
    while len(shuffle_list):
        ran_num = get_random(0, len(shuffle_list))
        new_list.append(shuffle_list[ran_num])
        shuffle_list = shuffle_list[:ran_num] + shuffle_list[ran_num + 1:]
    return new_list

def get_random(floor, ceiling):
    # print("floor %s" % floor)
    # print("ceiling %s" % ceiling)
    return random.randrange(floor, ceiling)


print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))





