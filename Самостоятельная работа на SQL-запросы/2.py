import sqlite3

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
con = sqlite3.connect(input())
first = input()
second = input()
cur = con.cursor()
rez = cur.execute(f'SELECT latitude, longitude FROM Island WHERE {first} AND {second}').fetchall()
for elem in rez:
    print(*elem)

con.close()
