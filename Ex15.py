# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

csv_file = open('csv_file.txt', 'r')
csv_lines = csv_file.readlines()
csv_file.close()


csv_lines = [row.strip().split(',') for row in csv_lines]

parsed_clubs_list = [({'club': r[0], 'city': r[1], 'country': r[2]}) for r in csv_lines]

# for r in csv_lines:
#     parsed_clubs_list.append({'club': r[0], 'city': r[1], 'country': r[2]})


json_file = open('json_file.txt', 'w')
json.dump(parsed_clubs_list, json_file)
json_file.close()




