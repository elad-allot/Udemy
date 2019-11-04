# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}

# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')

# ---- Do not change the code above ----


# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    def has_per():
        if user('role') == 'admin':
            return func()
    return has_per()


a = check_permission(delete_database)

print(a())

# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
