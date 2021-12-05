import numpy as np


def d05(file_name, include_horizontal):
    input_values = get_input(file_name)
    max_x = max(list(map(lambda x: max(x[1][0], x[0][0]), input_values))) + 1
    max_y = max(list(map(lambda x: max(x[1][1], x[0][1]), input_values))) + 1
    box = np.zeros((max_x, max_y))
    for val in input_values:
        (x1, x2) = (val[0][0], val[1][0]) if val[0][0] < val[1][0] else (val[1][0], val[0][0])
        (y1, y2) = (val[0][1], val[1][1]) if val[0][1] < val[1][1] else (val[1][1], val[0][1])
        if x1 == x2 or y1 == y2:
            box[x1:x2+1, y1:y2+1] += 1
        elif include_horizontal:
            x1, y1, x2, y2 = val[0][0], val[0][1], val[1][0], val[1][1]
            for i in range(abs(x1 - x2) + 1):
                box[x1 + (i if x1 < x2 else -i), y1 + (i if y1 < y2 else -i)] += 1
    return np.count_nonzero(box >= 2)


def get_input(file_name):
    with open(file_name, 'r') as f:
        return np.array([[[int(n) for n in y.split(',')] for y in x.split('->')] for x in f.readlines()])


test_data = {'input_test.txt': (5, 12), 'input.txt': (6710, 20121)}
for file in test_data.keys():
    result1 = d05(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d05(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
