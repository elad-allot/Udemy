

my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()


print(file_content)


user_input = input('what is youre name?')

my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_input)
my_file_writing.close()
