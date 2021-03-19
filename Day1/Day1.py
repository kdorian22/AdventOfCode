text = open("/Users/kennydorian/Desktop/Indy/AdventOfCode/Day1/Day1.txt", "r")
list = text.readlines()
text.close()
list = [int(x.replace('//n', '')) for x in list]

def part1():
    for num in list:
        for num2 in list:
            if num != num2:
                if num + num2 == 2020:
                    return num, num2, num*num2, num+num2

def part2():
    for num in list:
        for num2 in list:
            for num3 in list:
                if num != num2 and num2 != num3:
                    if num + num2 + num3 == 2020:
                        return num, num2, num3, num*num2*num3, num+num2+num3
                        
print('Part1', part1())
print('Part2', part2())
