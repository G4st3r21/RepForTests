import sqlite3

con = sqlite3.connect(input())
first, second = input(), input()
cur = con.cursor()
rez = cur.execute(f"SELECT latitude, longitude FROM Island
                    WHERE {first} AND {second}").fetchall()

for elem in rez:
    print(*elem)

con.close()