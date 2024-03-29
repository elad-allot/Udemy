lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = []

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

def createPlayer(name, numbers):
    if type(numbers) is set:
        return{'name': name,
               'numbers': numbers}
    else:
        return None


players.append(createPlayer('Elad', {3, 9, 39, 2, 6}))

players.append(createPlayer('Sivan', {2, 6, 26, 3, 9}))

for p in players:
    intersections = p['numbers'].intersection(lottery_numbers)
    print('%s got %s right!' % (p['name'], len(intersections),))
