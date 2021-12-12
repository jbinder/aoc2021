import numpy as np


def d12(file_name, revisit_allowed):
    data = np.array([x.split('-') for x in get_input(file_name)])
    area = {}
    for d in data:
        if d[0] not in area.keys():
            area[d[0]] = []
        if d[1] not in area.keys():
            area[d[1]] = []
        area[d[0]].append(d[1])
        area[d[1]].append(d[0])

    paths = find_paths(["start"], area, revisit_allowed)
    return len(paths)


def find_paths(paths, area, revisit_allowed):
    if paths[-1] == "end":
        return [paths]
    possible_paths = []
    for cave in area[paths[-1]]:
        has_visited = cave in paths and cave.islower()
        if cave == 'start' or (has_visited and not revisit_allowed):
            continue
        possible_paths.extend(find_paths(paths + [cave], area, revisit_allowed if not has_visited else False))
    return possible_paths


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]


test_data = {'input_test.txt': (10, 36), 'input.txt': (3421, 84870)}
for file in test_data.keys():
    result1 = d12(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d12(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
