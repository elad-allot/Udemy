import json

# json_file = open('friends_json.txt', 'r')
# file_content = json.load(json_file)
# json_file.close()
with open('friends_json.txt', 'r') as json_file:
    file_content = json.load(json_file)


print(file_content['friends'])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]


with open('cars.json', 'w') as json_file:
    json.dump(cars, json_file, indent=True)

