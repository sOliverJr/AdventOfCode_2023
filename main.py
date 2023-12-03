import datetime
import importlib

day = datetime.datetime.today().day

if day < 10:
    path = 'Day0' + str(day) + '.day0' + str(day)
else:
    path = 'Day' + str(day) + '.day' + str(day)

print('--- Day ' + str(day) + ' ---')

print("Part 1: ", end="")
importlib.import_module(path + '_part1')

print("Part 2: ", end="")
importlib.import_module(path + '_part2')
