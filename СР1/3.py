import sqlite3
import csv

bdfile = input()
strk = input().split(' ')
 
Bay = strk[0].strip()
day = int(strk[1])

con = sqlite3.connect(bdfile)
cur = con.cursor()

days = cur.execute(f"SELECT * FROM Bays \
    WHERE title like '{Bay}' AND date = {day}").fetchall()

end = []
for i in days:
    flow = cur.execute(f"SELECT * FROM Flows \
    WHERE id = {i[2]}").fetchall()
    wind = cur.execute(f"SELECT * FROM Winds \
    WHERE id = {i[3]}").fetchall()
    force = flow[0][-1] * flow[0][-2] + wind[0][-1] * 2
    end.append([i[-1], flow[0][1], wind[0][1], force])
end.sort()

with open('which_way.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in end:
        writer.writerow(i)
