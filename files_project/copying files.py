
friends_list = []
for i in range(3):
    friends_list.append(input("Enter  a Close by Friend:"))

file = open("people.txt", 'r')
friends_file = file.read()
file.close()


close_friends = ''
for friend in friends_list:
    if friend in friends_file:
        close_friends += friend + '\n'

file = open('nearby_friends.txt', 'w')
file.write(close_friends)
file.close()


