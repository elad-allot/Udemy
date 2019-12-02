# def change_possibilities(amount, denominations):
#     options = []
#     if amount < 0:
#         return
#     else:
#         for coin in denominations:
#             # if
#             pass
#
#
#     return 0
#

#
# a = (95, 'asd')
# print(a)
# print(a[0])


def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin

            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    print(ways_of_doing_n_cents)
    return ways_of_doing_n_cents[amount]


print(change_possibilities_bottom_up(4, (1, 2, 3)))
