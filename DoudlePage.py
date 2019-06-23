# # num = list(range(10))
# #
# # print(num)
# #
# # doubled_num = [n*2 for n in num]
# #
# # print(doubled_num)
# #
# #
# # phrase = [f'I am {age} years old' for age in doubled_num]
# #
# # print(phrase)
# #
# # names = ['Elad', 'Sagi', 'Malvina']
# #
# # named_phrase = [f'{name} is {age} years old' for name, age in names]
# #
# # print(named_phrase)
# #
# # dict = {"bla": 2, "bla2": 3}
# #
# # print(dict)
# #
# #
# # bla = [n.upper() for n in names]
# #
# # print(bla)
# # k
# #
# #
# # def createObject():
# #     x = object()
# #     print(x)
# #     return x
# #
# # x = object()
# # y = createObject()
# # print(y)
# #
# #
# #
# #
# #
# #
# # for n in range(2, 10):
# #   for x in range(2, n):
# #     if n % x == 0:
# #       print(n, 'equals', x, '*', n//x)
# #       break
# #   else:
# #     # loop fell through without finding a factor
# #     print(n, 'is a prime number')
# #
# #
# # def add_two(x, y):
# #     return x + y
# #
# # print(add_two(5,4))
# #
# # print((lambda x, y: x + y)(12, 56))
# #
# # add = (lambda x, y: x + y)
# #
# #
# # def who(data, ident):
# #     return ident(data)
# #
# # def my_ident(data):
# #     return data['name']
# #
# # data = {'name': 'Elad'}
# #
# #
# # def bla():
# #     return 'blablabla'
# #
# # x = bla
# #
# # print(x())
# #
# #
# # print(my_ident(data))
# #
# # print(who(data, my_ident))
# #
# #
# #
# #
# # """
# # We’ve looked at dictionaries as able to represent what _something_ is. For example, this dictionary represents a student:
# # """
# #
# # my_student = {
# #   'name': 'Rolf Smith',
# #   'grades': [70, 88, 90, 99]
# # }
# #
# # """
# # If we want to calculate the average grade of the student, we could create a function to do so:
# # """
# #
# # def average_grade(student):
# #   return sum(student['grades']) / len(student['grades'])
# #
# # """
# # However, there is a flaw with this. This function is separate and unrelated from the student (e.g. in a professional program, they could even be in different files), but it depends on the student variable having a particular structure:
# #
# # * The `student` must be a dictionary; and
# # * There must be a `grades` key that must be a list or tuple, so that we can use `sum()` and `len()` on them.
# #
# # It would be great if we could have something inside our dictionary that would return the average grade. That means the function would live in the same place as the data, and then it’s easier to see whether the data we require has changed or not.
# #
# # Something /like/ this:
# # """
# #
# #
# # my_student = {
# #   'name': 'Rolf Smith',
# #   'grades': [70, 88, 90, 99],
# #   'average': 0 # something here to calculate
# # }
# #
# # """
# # It would be fantastic if we could do this, and naturally the `'average'` would have to change when then `'grades` changes. It must be a function.
# #
# # *There’s no way to do this in a dictionary*.
# #
# # Sorry!
# #
# # We must use objects for this. We can begin by thinking of objects as things that can store both data and functions that relate to that data.
# #
# # Here’s that (incorrect) dictionary in object format:
# # """
# #
# # class Student:
# #   def __init__(self, new_name, new_grades):
# #     self.name = new_name
# #     self.grades = new_grades
# #
# #   def average(self):
# #     return sum(self.grades) / len(self.grades)
# #
# # """
# # Scary syntax! Don’t worry—what it does is close to the same.
# #
# # When you have that class, you can create objects using it. Let’s do that first and then explain exactly what is happening:
# # """
# #
# # student_one = Student('Rolf Smith', [70, 88, 90, 99])
# # student_two = Student('Jose', [50, 60, 99, 100])
# #
# # """
# # To create a new object, we use the class name as if it were a function call: `Student()`.
# #
# # Inside the brackets, we put arguments that will map to the `__init__` method in the `Student` class.
# #
# # `Student('Rolf Smith', [70, 88, 90, 99])` maps to `__init__(self, new_name, new_grades)`.
# #
# # What you end up with is a /thing/ that has two properties, `name` and `grades`.
# # """
# #
# # print(student_one.name)
# # print(student_two.name)
# #
# # """
# # Inside the `__init__` method, we use `self.name` and `self.grades`. `self` is the current object, so when we assign values we modify only the “current object”.
# # """
# #
# # Student('Rolf Smith', [70, 88, 90, 99])
# #
# # def __init__(self, new_name, grades):
# #  self.name = new_name
# #  self.grades = new_grades
# #
# # """
# # When you do this, `self` is the new object you are creating. You can assign it to a variable:
# # """
# #
# # student_one = Student('Rolf Smith', [70, 88, 90, 99])
# #
# # """
# # As you do that more, every object is a different `self`,  with differently assigned properties depending on what you passed to the `Student()` /constructor/ call.
# # """
# #
# # # Properties
# #
# # """
# # Cool, so now we have the objects, both of which have different properties:
# # """
# #
# # student_one = Student('Rolf Smith', [70, 88, 90, 99])
# # student_two = Student('Jose', [50, 60, 99, 100])
# #
# # """
# # These are _similar_ to our dictionaries, in that the dictionaries also store values:
# # """
# #
# # d_student_one = {
# #   'name': 'Rolf Smith',
# #   'grades': [70, 88, 90, 99]
# # }
# # d_student_two = {
# #   'name': 'Jose',
# #   'grades': [50, 60, 99, 100]
# # }
# #
# # """
# # To access them:
# #
# # ```
# # student_one.name
# # student_one.grades
# #
# # student_two.name
# # student_two.grades
# #
# # d_student_one['name']
# # d_student_one['grades']
# #
# # d_student_two['name']
# # d_student_two['grades']
# # ```
# # """
# #
# # # Methods
# #
# # """
# # > A method is a function which lives in a class.
# #
# # The `average()` method in the Student () class also has access to `self`, the current object. When we call the method:
# # """
# #
# # print(student_one.average())
# #
# # """
# # What is really happening in the background is:
# # """
# #
# # print(Student.average(student_one))
# #
# # """
# # As you can see, `student_one` is passed as the first argument (and that is what `self` is in the method definition):
# # """
# #
# # def average(self):
# #   return sum(self.grades) / len(self.grades)
# #
# # """
# # So again, because `self` is `student_one`, `self.grades` is `student_one.grades`.
# #
# # Thus:
# #
# # * The sum of `self.grades` is the sum of `[70, 88, 90, 99]`: 347.
# # * The length of `self.grades` is 4.
# #
# # The result will be `86.75`.
# # """
# #
# # x = average
# #
# # print(x())
# # # Recap
# #
# # """
# # Just to recap, the class is very similar to the dictionary but it allows us to include methods as well that have access to the properties of the object we created.
# #
# # Classes also gives us a bunch more functionality, we’ll look at that in the coming videos!
# # """
# #
# #
# # class Garage:
# #     def __init__(self):
# #         self.cars = []
# #
# #     def __len__(self):
# #         return len(self.cars)
# #
# #     def __delitem__(self, key):
# #         self.cars[key]
# #
# #     def __getitem__(self, key):
# #         return self.cars[key]
# #
# #     def __setitem__(self, key, value):
# #         self.cars[key] =  value
# #
# #
# # ford = Garage()
# # ford.cars.append('Fiesta')
# # ford.cars.append('Focus')
# #
# # print(ford.cars)
# # print(len(ford))
# # print(ford[1])
# # ford[1] = 'bla'
# # print(ford[1])
# #
# # for car in ford:
# #     print(car)
# #
# #
# # class Student:
# #     def __init__(self, name, school):
# #         self.name = name
# #         self.school = school
# #         self.marks = []
# #
# #     def average(self):
# #         return sum(self.marks) / len(self.marks)
# #
# #
# # anna = Student("Anna", "Oxford")
# #
# # """
# # Imagine you’ve got a class like the above, and you want to create a similar class with some extra functionality. For example, a student that not only has marks but also a salary—a `WorkingStudent`:
# # """
# #
# # class WorkingStudent:
# #     def __init__(self, name, school, salary):
# #         self.name = name
# #         self.school = school
# #         self.marks = []
# #         self.salary = salary
# #
# #     def average(self):
# #         return sum(self.marks) / len(self.marks)
# #
# #
# # rolf = WorkingStudent("Rolf", "MIT", 15.50)
# #
# # """
# # However you can see there’s a lot of duplication between our `Student` and `WorkingStudent` classes. Instead, we may choose to make our `WorkingStudent` extend the `Student`. It keeps all the same functionality, but we can add more.
# # """
# #
# # class WorkingStudent(Student):
# #     def __init__(self, name, school, salary):
# #         super().__init__(name, school)
# #         self.salary = salary
# #
# #
# # rolf = WorkingStudent("Rolf", "MIT", 15.50)
# # rolf.marks.append(57)
# # rolf.marks.append(99)
# # print(rolf.average())
# #
# # """
# # By the way, notice how the `average()` function doesn’t take any inputs other than `self`. There’s nothing in the brackets.
# #
# # In those cases, and if you think it makes sense, we can make it into a property, just like `marks` and `salary`.
# #
# # All we have to do is:
# # """
# #
# # class Student:
# #     def __init__(self, name, school):
# #         self.name = name
# #         self.school = school
# #         self.marks = []
# #
# #     @property
# #     def average(self):
# #         return sum(self.marks) / len(self.marks)
# #
# # """
# # Now the `average()` function can be used as if it were a property instead of a method; like so:
# # """
# #
# # jose = Student("Jose", "Stanford")
# # jose.marks.append(80)
# # jose.marks.append(90)
# # print(jose.average)
# #
# # """
# # You can do that with any method that doesn’t take any arguments. But remember, this method only returns a value calculated from the object’s properties. If you have a method that does things (e.g. save to a database or interact with other things), it can be better to stay with the brackets.
# #
# # Normally:
# #
# # * Brackets: this method does things, performs actions.
# # * No brackets: this is a value (or a value calculated from existing values, in the case of `@property`).
# # """
# #
# #
# # class bla:
# #     @classmethod
# #     def hi(self):
# #         print(self)
# #
# #     def __str__(self):
# #         return "Hello"
# #
# # b = bla()
# # b.hi()
# #
# #
# # class Bla:
# #     pass
# #
# # b = Bla()
# #
# # print(isinstance(b, Bla))
# #
# #
# #
# #
# #
# # def power_of_two():
# #     n = 1
# #     user_input = input('Please enter a number: ')
# #     try:
# #         n = float(user_input)
# #     except ValueError:
# #         print('Your input was invalid. Using default value 0')
# #         return 0
# #     finally:
# #         n_square = n ** 2
# #         return n_square
# #
# #
# # x = power_of_two()
# # print(x)
# #
# #
# # if bol:
# #     x = 1
# # if !bol:
# #     x = x + 1
# # else:
# #     z = 3
# # print(x)
# # print (z)
#
#
# import json
#
#
#
# json_str = """{
#     "bla": [
#         {
#             "n": 1,
#             "m": 2
#         },
#         {
#             "x": 5,
#             "y": 9
#         }
#     ]
# }
# """
#
# x = json.load(json_str)
#
# print(x)
#
#
#
#
#
#
#
#
#
#
# import csv
#
# def csv_writ(row):
#     csv_file = open('csv_file.csv', 'a', newline='')
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(row)
#     csv_file.close()
#
# for i in range(5):
#     for j in range(10):
#         for k in range(13):
#             csv_writ((i, j, k))
#
#
#
# my_list = []
#
# def add_to_list(r):
#     my_list.append(r)
#
# print(my_list)
#
# add_to_list({'bla':3 , 'blas3': 5})
#
# print(my_list)

