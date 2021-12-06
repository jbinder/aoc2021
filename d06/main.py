from collections import deque


def d06(file_name, num_days):
    fish_per_timer = deque([get_input(file_name).count(str(x)) for x in range(9)])
    for x in range(num_days):
        fish_per_timer[7] += fish_per_timer[0]
        fish_per_timer.rotate(-1)
    return sum(fish_per_timer)


def get_input(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()[0].split(',')


test_data = {'input_test.txt': (5934, 26984457539), 'input.txt': (383160, 1721148811504)}
for file in test_data.keys():
    result1 = d06(file, 80)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d06(file, 256)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
