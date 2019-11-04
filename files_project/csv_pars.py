

csv_file = open('csv_data.txt', 'r')
lines = csv_file.readlines()
csv_file.close()

lines = [line.strip() for line in lines[1:]]  # line slicing


print(lines)




