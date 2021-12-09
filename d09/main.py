import numpy as np
from functools import reduce
import operator


def d09(file_name, pt2):
    n = get_input(file_name)
    maxes_r = np.full((1, n.shape[1]), np.max(n))
    maxes_c = np.full((n.shape[0] + 2, 1), np.max(n))
    n = np.r_[maxes_r, n, maxes_r]
    n = np.c_[maxes_c, n, maxes_c]
    mins = ((n < np.roll(n, 1, 0)) &
            (n < np.roll(n, -1, 0)) &
            (n < np.roll(n, 1, 1)) &
            (n < np.roll(n, -1, 1)))
    masked = np.ma.masked_array(data=n, mask=~mins, fill_value=0)
    masked += 1
    if not pt2:
        return masked.sum()

    masked -= 1
    min_indices_xy = np.where(masked.mask == False)
    min_indices = list(zip(min_indices_xy[0], min_indices_xy[1]))
    counts = []
    for index in min_indices:
        counts.append(count(index, n, np.full(n.shape, False)))
    return reduce(operator.mul, sorted(counts, reverse=True)[:3], 1)


def count(index, data, processed):
    if processed[index]:
        return 0
    processed[index] = True
    element = data[index]
    if element == 9:
        return 0
    res = 1
    res += count((index[0] + 1, index[1]), data, processed)
    res += count((index[0], index[1] + 1), data, processed)
    res += count((index[0] - 1, index[1]), data, processed)
    res += count((index[0], index[1] - 1), data, processed)
    return res


def get_input(file_name):
    with open(file_name, 'r') as f:
        return np.array([[int(y) for y in x.strip()] for x in f.readlines()])


test_data = {'input_test.txt': (15, 1134), 'input.txt': (541, 847504)}
for file in test_data.keys():
    result1 = d09(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d09(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
