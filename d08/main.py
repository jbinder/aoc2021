import numpy as np


def d08(file_name, pt2):
    numbers = get_input(file_name)
    unique_lengths = [2, 3, 4, 7]
    if not pt2:
        outputs = [x[1] for x in numbers]
        known_digits = [[len(y) in unique_lengths for y in x] for x in outputs]
        return np.count_nonzero(np.array(known_digits) == True)
    else:
        decoded = ['-' for _ in range(10)]
        len_to_val = {2: 1, 3: 7, 4: 4, 7: 8}
        res = 0
        for n in numbers:
            all_digits = sorted(set(n[0] + n[1]), key=len)
            for digit in all_digits:
                length = len(digit)
                if length in len_to_val.keys():
                    decoded[len_to_val[length]] = digit
                elif length == 6 and (not contains_any([decoded[1], decoded[7]], digit)):
                    decoded[6] = digit
                elif length == 6 and (contains_any([decoded[4]], digit)):
                    decoded[9] = digit
                elif length == 6:
                    decoded[0] = digit
                elif length == 5 and (contains_any([decoded[1], decoded[7]], digit)):
                    decoded[3] = digit
                elif length == 5 and (set(decoded[4]).difference(decoded[1]).issubset(set(digit))):
                    decoded[5] = digit
                elif length == 5:
                    decoded[2] = digit
            res += int(''.join([str(decoded.index(x)) for x in n[1]]))
        return res


def contains_any(ref_digits, digit):
    for d in ref_digits:
        if set(d).issubset(digit):
            return True
    return False


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [[[''.join(sorted(z.strip())) for z in y.strip().split(' ')] for y in x.split('|')]
                for x in f.readlines()]


test_data = {'input_test.txt': (26, 61229), 'input.txt': (381, 1023686)}
for file in test_data.keys():
    result1 = d08(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d08(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
