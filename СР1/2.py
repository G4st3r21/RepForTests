import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
rez = cur.execute("""SELECT latitude, longitude FROM Island
                    WHERE height BETWEEN 125 AND 300 """).fetchall()

for elem in rez:
    print(*elem)

con.close()