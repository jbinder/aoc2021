def d02(input_file, action_map):
    with open(input_file) as file:
        pos = {'x': 0, 'y': 0}
        aim = 0

        for line in file:
            command_segments = line.split(" ")
            command = command_segments[0]
            value = int(command_segments[1])
            changes = action_map[command](value, aim)
            pos['x'] += changes[0]
            pos['y'] += changes[1]
            aim += changes[2]

        return pos['x'] * pos['y']


action_map_1 = {'forward': lambda v, a: (v, 0, 0), 'up': lambda v, a: (0, -v, 0), 'down': lambda v, a: (0, v, 0)}
action_map_2 = {'forward': lambda v, a: (v, a * v, 0), 'up': lambda v, a: (0, 0, -v), 'down': lambda v, a: (0, 0, v)}


test_data = {'input_test.txt': (150, 900), 'input.txt': (1727835, 1544000595)}
for file in test_data.keys():
    print(d02(file, action_map_1) == test_data[file][0])
    print(d02(file, action_map_2) == test_data[file][1])
