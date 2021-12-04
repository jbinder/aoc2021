import numpy as np


def d04(file_name, last_wins):
    with open(file_name, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    numbers = [int(x) for x in lines[:1][0].split(',')]
    boxes = create_boxes(lines)

    boxes_won = set()
    for n in numbers:
        boxes = np.where(boxes == n, -1, boxes)
        for idx, box in enumerate(boxes):
            if idx in boxes_won or not is_empty(box):
                continue
            if not last_wins or (len(boxes_won) + 1 == len(boxes)):
                return np.sum(np.where(box == -1, 0, box)) * n
            else:
                boxes_won.add(idx)


def create_boxes(lines):
    boxes = []
    for line in lines[1:]:
        if len(line) == 0:
            boxes.append([])
        else:
            boxes[len(boxes) - 1].append([int(x) for x in line.split(' ') if x != ''])
    return np.asarray(boxes)


def is_empty(box):
    for i in range(box.shape[0]):
        if np.all(box[i] == -1):
            return True
    for i in range(box.shape[1]):
        if np.all(box[:, i] == -1):
            return True


test_data = {'input_test.txt': (4512, 1924), 'input.txt': (44088, 23670)}
for file in test_data.keys():
    result1 = d04(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d04(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
