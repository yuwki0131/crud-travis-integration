# -*- coding: utf-8 -*-

import mysql.connector

if __name__ == '__main__':
    print("db connection test")
    conn = mysql.connector.connect(
        user='crudapp',
        password='passwd',
        host='localhost',
        port='3307',
        database='crudapp')
    cur = conn.cursor()
    print("db connected")

    cur.execute('insert into users (name) values ("test")')

    cur.execute("select * from users;")
    row = cur.fetchone()

    # output
    print("db: " + str(row))

    cur.close
    conn.close
    print("db test exit")
    exit(0)
