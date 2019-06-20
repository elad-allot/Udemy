
from files_project.file_opperations import read_file, save_to_file

a = read_file('cars.txt')

save_to_file(a, 'bla.txt')

print(a)
