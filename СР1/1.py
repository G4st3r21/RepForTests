import csv

shipsstr = input()
good_word = input()
ships = [i for i in shipsstr.split(' - ')]

impostors = []
with open('suitable_crew.csv', encoding="utf8") as csvfile:
    pirates = csv.reader(csvfile, delimiter=',', quotechar='"')

    for i in pirates:
        if (i[2] not in ships) and (good_word not in i[-1].lower()) and (i[0] != 'id'):
            impostors.append(i[1])

print(*impostors, sep='\n')
