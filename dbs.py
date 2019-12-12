#!/opt/allot/clearsee/python/bin/python2.7
import os
import random
from datetime import date, datetime
import re

BOT_FILE_PATH = "/home/dbadmin/elad"
BOT_FILE = "bots"


def write_new_line(line, open_file):
        try:
                open_file.write('%s\n' % line)
        except:
                print("Bad File")


def create_MAC():
    return [random.randint(0x00, 0x7f),
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]


def MAC_pretty_print(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))


def ran_date():
        start_dt = date.today().replace(day=1, month=1).toordinal()
        end_dt = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_dt, end_dt))
        return random_day


def create_IP():
        ip = str(random.randint(1, 255)) + '.' + str(random.randint(1, 255)) + '.' +\
             str(random.randint(1, 255)) + '.' + str(random.randint(1, 255))
        return ip


def get_OS():
        return random.choice(['Windows', 'Ubuntu', 'Android', 'IOS', 'Arch Linux'])


def create_army(army_size):
        bots = []
        for i in range(army_size):
                bot = {}
                bot['IP'] = create_IP()
                bot['MAC'] = MAC_pretty_print(create_MAC())
                bot['OS'] = get_OS()
                bot['last_ping'] = ran_date()
                bot['is_alive'] = random.choice([True, False])
                bots.append(bot)
        return bots


def save(bot_list):
        bot_num = 1
        try:
                bf = open(os.path.join(BOT_FILE_PATH, BOT_FILE), 'w')
                for bot in bot_list:
                        write_new_line('BOT Number %s:' % bot_num, bf)
                        write_new_line('\tIP: %s' % bot['IP'], bf)
                        write_new_line('\tMAC: %s' % bot['MAC'], bf)
                        write_new_line('\tOS: %s' % bot['OS'], bf)
                        write_new_line('\tlast_ping: %s' % str(bot['last_ping']), bf)
                        write_new_line('\tis_alive: %s' % str(bot['is_alive']), bf)
                        bot_num += 1
        finally:
                bf.close()


def load():
        bots = []
        try:
                f = open(os.path.join(BOT_FILE_PATH, BOT_FILE), 'r')
                next_line = f.readline()
                while next_line:
                        if re.match(r"BOT Number \+?\d+:", next_line):
                                bot = {}
                                for i in range(6):
                                        next_line = next_line.replace('\t', '').replace('\n', '')
                                        temp_bot = next_line.split(': ')
                                        if any(temp_bot[0] in names for names in ['IP', 'MAC', 'OS', 'last_ping',
                                                                                  'is_alive']):
                                                bot[temp_bot[0]] = temp_bot[1]
                                        next_line = f.readline()
                                bots.append(bot)
        finally:
                f.close()
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
                        print ('%s: %s' %(key, val,))
                bot_num += 1


def main():
        save(create_army(2))
        display()
        add([{'IP': create_IP(), 'MAC': create_MAC(), 'OS': get_OS()},
             {'IP': create_IP(), 'MAC': create_MAC(), 'OS': get_OS()},
             {'IP': create_IP(), 'MAC': create_MAC(), 'OS': get_OS()}])
        print '&'*125
        display()


if __name__ == "__main__":
        main()
