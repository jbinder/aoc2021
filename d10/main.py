from functools import reduce
from queue import LifoQueue


def d10(file_name, result_p, score_p):
    lines = get_input(file_name)
    parenthesis = {')': '(', ']': '[', '}': '{', '>': '<'}
    parenthesis_inv = {v: k for k, v in parenthesis.items()}
    result = []
    for line in lines:
        queue = LifoQueue()
        conflicting_ch = ''
        for ch in line:
            if ch in parenthesis.values():
                queue.put(ch)
            elif ch in parenthesis.keys() and queue.queue[-1] == parenthesis[ch]:
                queue.get()
            else:
                conflicting_ch = ch
                break
        result.append(result_p(conflicting_ch, queue, parenthesis_inv))
    return score_p(list(filter(None, result)))


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]


def score_p1(result):
    point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum([point_map[x] for x in result])


def score_p2(result):
    point_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = [reduce(lambda a, b: a * 5 + point_map[b], x, 0) for x in result]
    return sorted(scores)[len(scores) // 2]


def result_p1(ch, queue, parenthesis_inv):
    return ch if ch != '' else None


def result_p2(ch, queue, parenthesis_inv):
    return None if ch != '' else ''.join([parenthesis_inv[x] for x in reversed(queue.queue)])


test_data = {'input_test.txt': (26397, 288957), 'input.txt': (392139, 4001832844)}
for file in test_data.keys():
    result1 = d10(file, result_p1, score_p1)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d10(file, result_p2, score_p2)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
