def d03_1(input_file):
    with open(input_file) as file:
        ones = []
        count = 0
        for line in file:
            if len(ones) < 1:
                ones = [0 for _ in range(len(line) - 1)]
            for i in range(len(ones)):
                ones[i] += int(line[i])
            count += 1
        gamma = int(''.join(['1' if count - x < x else '0' for x in ones]), 2)
        epsilon = int(''.join(['0' if count - x < x else '1' for x in ones]), 2)
        return gamma * epsilon


def d03_2(input_file):
    with open(input_file) as file:
        lines = []
        for line in file:
            lines.append(line.strip())
        ogr = int(''.join([str(x) for x in (find_rating(lines, '1', '0'))]), 2)
        csr = int(''.join([str(x) for x in (find_rating(lines, '0', '1'))]), 2)
        return ogr * csr


def find_rating(lines, most_common, least_common):
    matches = lines
    for i in range(0, len(lines[0])):
        values = [int(x[i]) for x in matches]
        x = most_common if len(matches) - sum(values) <= sum(values) else least_common
        matches = [match for match in matches if x == match[i]]
        if len(matches) == 1:
            return matches[0]


test_data = {'input_test.txt': (198, 230), 'input.txt': (749376, 2372923)}
for file in test_data.keys():
    result1 = d03_1(file)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d03_2(file)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
