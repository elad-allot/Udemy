import json

json_file = open('friends_json.txt', 'r')
file_content = json.load(json_file)
json_file.close()

print(file_content['friends'])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]


json_file = open('cars.json', 'w')
json.dump(cars, json_file)

