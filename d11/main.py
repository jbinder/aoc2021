import numpy as np


def d11(file_name, max_steps):
    octopuses = np.array([[int(y) for y in x] for x in get_input(file_name)])
    flashes = 0
    for i in range(max_steps if max_steps > 0 else 1000):
        octopuses += 1
        masked = np.ma.masked_array(data=octopuses, mask=np.full(octopuses.shape, False), hard_mask=True)
        while 10 in masked:
            flashing_pos_indices = np.where(masked == 10)
            flashing_pos = list(zip(flashing_pos_indices[0], flashing_pos_indices[1]))[0]
            x1, y1 = max(flashing_pos[0] - 1, 0), max(flashing_pos[1] - 1, 0)
            x2, y2 = min(flashing_pos[0] + 1, masked.shape[0] - 1), min(flashing_pos[1] + 1, masked.shape[1] - 1)
            masked[x1:x2 + 1, y1:y2 + 1] += 1
            masked[flashing_pos] = np.ma.masked
            masked = np.ma.where(masked > 10, 10, masked)
            flashes += 1
        octopuses = np.where(masked.data >= 10, 0, masked.data)
        if max_steps == 0 and np.all((octopuses == 0)):
            return i + 1
    return flashes


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]


test_data = {'input_test.txt': (1656, 195), 'input.txt': (1617, 258)}
for file in test_data.keys():
    result1 = d11(file, 100)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d11(file, 0)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
