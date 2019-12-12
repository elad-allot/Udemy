#!/opt/allot/clearsee/python/bin/python2.7


import mysql.connector


class Conn:
    def __init__(self, username, password, host='127.0.0.1'):
        self.config = {'user': username,
                       'host': host,
                       'password': password}
        # self.cnx = mysql.connector.connect(**self.config)
        self.cnx = None
        self.cur = None

    def is_alive(self):
        return self.cnx.is_connected()

    def reconnect(self):
        self.cnx = mysql.connector.connect(**self.config)

    def run_sql(self, q, att=None):
        self.cur = self.cnx.cursor()
        self.cur.execute(q, att)
        if self.cur.with_rows:
            return self.cur.fetchall()

    def commit(self):
        self.cur.execute("COMMIT;", None)

    def __enter__(self):
        self.cnx = mysql.connector.connect(**self.config)
        return self.cnx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cnx.close()
