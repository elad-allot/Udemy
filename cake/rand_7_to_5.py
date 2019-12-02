import random


def rand7():
    return random.randint(1, 7)


def rand5():
    my_num = 7
    while my_num > 5:
        my_num = rand7()
        print(my_num)
    return my_num


# print (7/5)
# print (5/7)
print(rand5())