#!/opt/allot/clearsee/python/bin/python2.7

from datetime import datetime
import dbs
import conn as c
import getpass
import argparse

CONN = None


def pars_args():
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-u", "--username", help="Username.", type=str, default=None)
    parser.add_argument("-p", "--password", help="Password.", type=str, default=None)

    # Parse arguments
    args = parser.parse_args()

    return args


def commit():
    CONN.run_sql("COMMIT;")


def create_db():
    create_db = """CREATE DATABASE IF NOT EXISTS botsbotsbots;"""
    CONN.run_sql(create_db)


def create_tables():
    create_tbl = """CREATE TABLE IF NOT EXISTS botsbotsbots.bots (
                        IP char(15),
                        MAC char(20),
                        OS char(100),
                        last_ping date,
                        is_alive binary);"""
    CONN.run_sql(create_tbl)


def clear(is_clear):
    if is_clear:
        drop_db = """DROP DATABASE IF EXISTS botsbotsbots;"""
        CONN.run_sql(drop_db)


def init_db(is_clear=False):
    clear(is_clear)
    create_db()
    create_tables()


def save(bot_list):
    base_query = "INSERT INTO botsbotsbots.bots (IP, MAC, OS, last_ping, is_alive) VALUES (%s,%s,%s,%s,%s);"
    for bot in bot_list:
        CONN.run_sql(base_query, (bot['IP'], bot['MAC'], bot['OS'], str(bot['last_ping']), bot['is_alive'], ))
        commit()


def load():
    bots = []
    query = """SELECT IP, MAC, OS, last_ping, is_alive FROM botsbotsbots.bots;"""
    rows = CONN.run_sql(query)
    for row in rows:
        bot = {'IP': row[0], 'MAC': row[1], 'OS': row[2], 'last_ping': row[3], 'is_alive': row[4]}
        bots.append(bot)
    return bots


def add(new_bots):
    for nb in new_bots:
        nb['last_ping'] = datetime.today().strftime('%Y-%m-%d')
        nb['is_alive'] = True
    save(new_bots)


def display():
    my_bots = load()
    bot_num = 1
    for bot in my_bots:
        print ('Bot Num: %s ' % bot_num)
        for key, val in bot.iteritems():
            print ('\t%s: %s' % (key, val,))
        bot_num += 1


def init(username=None, password=None):
    global CONN
    try:
        if not username and not password:
            username = raw_input("Enter DB Username: ")
            password = getpass.getpass("%s Enter Password: " % username)
        CONN = c.Conn(username, password)
        # CONN = conn.Conn('root', 'Allot123!')
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        print("Incorrect Username or password, Please try again.")
        print e.message
        init()


def main():
    args = pars_args()
    init(args.username, args.password)
    init_db(is_clear=True)
    save(dbs.create_army(2))
    display()
    add([{'IP': '123.123.123.123', 'MAC': '0f:2f:20:6a:83:48', 'OS': 'Android'},
         {'IP': '10.150.8.11', 'MAC': '0d:18:4a:36:6a:30', 'OS': 'Windows'},
         {'IP': '10.152.125.52', 'MAC': '4c:3d:13:12:ad:d3', 'OS': 'Ubuntu'}])
    print '&' * 125
    display()
    while True:
        continue



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as err:
        print ("Abort!")
