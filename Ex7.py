import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)


# print(lottery_numbers)

players_count = {p['name']: 100 ** len(p['numbers'].intersection(lottery_numbers)) for p in players}
print(players_count)


winning_number = max(players_count.values())
winning_player = [p for p,n in players_count.items() if winning_number == n]

for p in winning_player:
    print('%s won %s' % (p, winning_number,))

# for p in players_count.items():
#     print('%s won %s' % (p[0], p[1]))



