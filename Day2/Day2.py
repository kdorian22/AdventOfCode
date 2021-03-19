text = open("/Users/kennydorian/Desktop/Indy/AdventOfCode/Day2/Day2.txt", "r")
list = text.readlines()
passwords = []
for row in list:
    row = row.split(' ')
    rowDict = {}
    rowDict.update(min = int(row[0].split('-')[0]), max = int(row[0].split('-')[1]))
    rowDict.update(letter = row[1].replace(':', ''))
    rowDict.update(string = row[2].replace('\n', ''))
    passwords.append(rowDict)

def part1():
    tot = 0
    for p in passwords:
        if p['max'] >= p['string'].count(p['letter']) >= p['min']:
            tot += 1
    return tot
print(part1())

def part2():
    tot = 0
    for p in passwords:
        if (p['string'][p['min']-1] == p['letter']) ^ (p['string'][p['max']-1] == p['letter']):
            tot += 1
    return tot
print(part2())
