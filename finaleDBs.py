#!/opt/allot/clearsee/python/bin/python2.7

import conn
import getpass

USERS = {}


def db_conn():
    """Returns an active DB connections. Remember to close it."""
    try:
        return conn.Conn('root', 'Allot123!')
    except Exception as err:
        print err.message


def setup_db():
    """SQLs that create the schema."""
    db = """CREATE DATABASE IF NOT EXISTS msgs;"""

    tbl1 = """CREATE TABLE IF NOT EXISTS msgs.users(
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(128),
                email VARCHAR(512),
                password VARCHAR(256),
                PRIMARY KEY (id)
                );"""

    tbl2 = """CREATE TABLE IF NOT EXISTS msgs.comments(
                comment_id INT NOT NULL AUTO_INCREMENT,
                user_id INT NOT NULL,
                comment VARCHAR(4096),
                PRIMARY KEY (comment_id),
                FOREIGN KEY (user_id) REFERENCES users(id)
                );"""
    con = db_conn()
    con.run_sql(db)
    con.run_sql(tbl1)
    con.run_sql(tbl2)
    print("DB is set")


def load_users():
    """Loads all users into a local dict."""
    con = db_conn()
    query = """SELECT 
                id,
                name,
                email,
                password
               FROM msgs.users;"""
    query_result = con.run_sql(query)
    for row in query_result:
        USERS[row[2]] = (row[0], row[1], row[3])


def login():
    """Attempts to login according to known users."""
    while not logedin():
        print("Incorrect username or password, Please try again")
        login()


def logedin():
    username = raw_input("login as:")
    password = getpass.getpass("%s Enter Password: " % username)
    try:
        return USERS[username][2] == password
    except KeyError:
        print('User %s does not exist' % username)
        logedin()




def register():
    """Registers a new user."""
    pass


def comment(user_id, comment):
    """Inserts a comment into the comments table."""
    pass


def main():
    # con = db_conn()
    # print (con.is_alive())
    # print (con.run_sql("""SHOW VARIABLES LIKE "%version%";"""))
    setup_db()
    load_users()
    print(USERS)
    login()

if __name__ == "__main__":
    main()
