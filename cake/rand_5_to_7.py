import random


def rand5():
    return random.randint(1, 5)


def rand7():
    temp_sum = 0
    for i in range(7):
        temp_sum += rand5()
    return int(temp_sum/5)



for i in range(1,8):
    print (5/i)


# words_to_counts = [0] * 7
# print(words_to_counts)
#
# for i in range(100000):
#     res = rand7()
#     words_to_counts[res] += 1
#
# print(words_to_counts)
#
#
