def d021():
    with open("input.txt") as file:
        pos = {'x': 0, 'y': 0}
        pos_map = {'forward': (1, 0), 'up': (0, -1), 'down': (0, 1)}

        for line in file:
            command_segments = line.split(" ")
            command = command_segments[0]
            value = int(command_segments[1])
            pos['x'] += pos_map[command][0] * value
            pos['y'] += pos_map[command][1] * value

        print(f"result: {pos['x'] * pos['y']}")


def d022():
    with open("input.txt") as file:
        pos = {'x': 0, 'y': 0}
        aim = 0
        action_map = {'forward': lambda v, a: (v, a * v, 0), 'up': lambda v, a: (0, 0, -v), 'down': lambda v, a: (0, 0, v)}

        for line in file:
            command_segments = line.split(" ")
            command = command_segments[0]
            value = int(command_segments[1])
            changes = action_map[command](value, aim)
            pos['x'] += changes[0]
            pos['y'] += changes[1]
            aim += changes[2]

        print(f"result: {pos['x'] * pos['y']}")


d021()
d022()
