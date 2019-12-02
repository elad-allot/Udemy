



def max_duffel_bag_value_bad(cake_tuples, weight_capacity):
    # Calculate the maximum value we can carry

    # return -1
    bag_weight = [0] * (weight_capacity+1)
    bag_weight[0] = 1
    bag_worth = [0] * (weight_capacity+1)

    for cake in cake_tuples:

        for weight in range(cake[0], weight_capacity):

            weight_left = weight - cake[0]

            bag_weight[weight] += bag_weight[weight_left]
            bag_worth[weight] += int(weight/cake[0]) * cake[1]

    print(bag_weight)
    print(bag_worth)
    return max(bag_worth)
    # return



def you_tube_solv(cake_tuples, weight_capacity):
    pass



def max_duffel_bag_value(cake_tuples, weight_capacity):
    pass

print(max_duffel_bag_value([(2, 15), (3, 90), (7, 160)], 20))
