import datetime
import os

day = datetime.datetime.today().day

if day < 10:
    file_path = os.getcwd() + '/Day0' + str(day) + '/day0' + str(day)
else:
    file_path = os.getcwd() + '/Day0' + str(day) + '/day0' + str(day)

print('--- Day ' + str(day) + ' ---')

print("Part 1: ", end="")
os.system('python3 ' + file_path + '_part1.py')

print("Part 2: ", end="")
os.system('python3 ' + file_path + '_part2.py')
