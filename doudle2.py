# x = 300
# y = 300
#
# print(id(x))
# print(id(y))
#
# print(x is y)
#
# print("$DATE$")

a = 'asdasdasd asd asd asd asda'
df = 'asdasdasd asd asd asd asda'


print (a)
# print(['NaN' for x in st if x == ''])
a = ["nan" if x == '' else x for x in a]
print (a)


print(df.replace(r'^\s*$', 'nan', regex=True))