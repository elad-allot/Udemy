#!/opt/allot/clearsee/python/bin/python2.7
import mysql.connector
from datetime import datetime
import dbs #, conn as c

CONFIG = {'user': 'root',
          'host': '127.0.0.1',
          'password': 'SimilarWeb!'
          }

cnx = mysql.connector.connect(**CONFIG)

cur = cnx.cursor()


def commit():
    cur.execute("COMMIT;")


def create_db():
    create_db = """CREATE DATABASE IF NOT EXISTS botsbotsbots;"""
    cur.execute(create_db)


def create_tables():
    create_tbl = """CREATE TABLE IF NOT EXISTS botsbotsbots.bots (
                        IP char(15),
                        MAC char(20),
                        OS char(100),
                        last_ping date,
                        is_alive binary);"""
    cur.execute(create_tbl)


def clear(is_clear):
    if is_clear:
        drop_db = """DROP DATABASE IF EXISTS botsbotsbots;"""
        cur.execute(drop_db)


def init_db(is_clear=False):
    clear(is_clear)
    create_db()
    create_tables()


def save(bot_list):
    base_query = "INSERT INTO botsbotsbots.bots (IP, MAC, OS, last_ping, is_alive) VALUES (%s,%s,%s,%s,%s);"
    for bot in bot_list:
        cur.execute(base_query, (bot['IP'], bot['MAC'], bot['OS'], str(bot['last_ping']), bot['is_alive'], ))
    commit()


def load():
    bots = []
    query = """SELECT IP, MAC, OS, last_ping, is_alive FROM botsbotsbots.bots;"""
    cur.execute(query)
    row = cur.fetchone()
    while row:
        bot = {'IP': row[0], 'MAC': row[1], 'OS': row[2], 'last_ping': row[3], 'is_alive': row[4]}
        bots.append(bot)
        row = cur.fetchone()
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


def main():
    # init()
    # query = """SELECT IP, MAC, OS, last_ping, is_alive FROM botsbotsbots.bots;"""
    # a = CONNV.execute(query)
    # print (a)
    init_db(is_clear=True)
    save(dbs.create_army(10))
    display()
    to_add = [{'IP': dbs.create_IP(), 'MAC': dbs.create_MAC(), 'OS': dbs.get_OS()},
              {'IP': dbs.create_IP(), 'MAC': dbs.create_MAC(), 'OS': dbs.get_OS()},
              {'IP': dbs.create_IP(), 'MAC': dbs.create_MAC(), 'OS': dbs.get_OS()}]
    # add([{'IP': '123.123.123.123', 'MAC': '0f:2f:20:6a:83:48', 'OS': 'Android'},
    #      {'IP': '10.150.8.11', 'MAC': '0d:18:4a:36:6a:30', 'OS': 'Windows'},
    #      {'IP': '10.152.125.52', 'MAC': '4c:3d:13:12:ad:d3', 'OS': 'Ubuntu'}])
    add(to_add)
    print '&' * 125
    display()


if __name__ == "__main__":
    main()
