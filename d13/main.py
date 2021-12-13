import numpy as np


def d13(file_name, only_first_instruction):
    lines = get_input(file_name)
    dots = []
    for line in lines:
        if ',' in line:
            dots.append([int(x) for x in line.split(',')])
        if '' == line:
            break
    width = np.amax(np.array([x[0] for x in dots])) + 1
    height = np.amax(np.array([x[1] for x in dots])) + 1

    paper = np.full((height, width), None)
    for dot in dots:
        paper[dot[1], [dot[0]]] = 'x'

    instructions = lines[len(dots) + 1:]
    for instruction in instructions:
        fold_at = int(instruction.split('=')[1])
        fold_by_x = 'x' in instruction
        new_width = fold_at if fold_by_x else width
        new_height = height if fold_by_x else fold_at
        folded_paper = np.full((new_height, new_width), None)
        new_dots = []
        for dot in dots:
            x = (width - dot[0] - 1 if dot[0] >= new_width else dot[0]) if fold_by_x else dot[0]
            y = dot[1] if fold_by_x else height - dot[1] - 1 if dot[1] >= new_height else dot[1]
            folded_paper[y, x] = 'x'
            new_dots.append([x, y])

        if only_first_instruction:
            return (folded_paper == 'x').sum()

        width, height, paper, dots = new_width, new_height, folded_paper, new_dots

    return ''.join([''.join(['#' if y == 'x' else '.' for y in x])+'\n' for x in folded_paper])


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]


expected_1 = '#####\n' \
             '#...#\n' \
             '#...#\n' \
             '#...#\n' \
             '#####\n' \
             '.....\n' \
             '.....\n'
expected_2 = '#..#..##...##....##.###..####.#..#..##..\n' \
             '#..#.#..#.#..#....#.#..#.#....#..#.#..#.\n' \
             '####.#....#..#....#.###..###..####.#....\n' \
             '#..#.#.##.####....#.#..#.#....#..#.#....\n' \
             '#..#.#..#.#..#.#..#.#..#.#....#..#.#..#.\n' \
             '#..#..###.#..#..##..###..####.#..#..##..\n'


test_data = {'input_test.txt': (17, expected_1), 'input.txt': (704, expected_2)}
for file in test_data.keys():
    result1 = d13(file, True)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d13(file, False)
    print(f"{file}/2: \n{result2} {result2 == test_data[file][1]}")
