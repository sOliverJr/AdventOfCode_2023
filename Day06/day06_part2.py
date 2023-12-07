
input = {'time': 42686985, 'distance': 284100511221341}

output = 0

for i in range(input['time']):
    speed = i
    distance = speed * (input['time'] - i)
    if distance > input['distance']:
        output += 1

print(output)
