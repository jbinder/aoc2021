def d14(file_name, num_iterations):
    lines = get_input(file_name)
    polymer = lines[0]
    rules = {(parts := x.split(' '))[0]: parts[2] for x in lines[2:]}
    polymers = {x: 0 for x in rules.keys()}
    for j in range(len(polymer) - 1):
        polymers[polymer[j:j + 2]] += 1

    counts = {key: polymer.count(key) for key in set([x for sublist in rules.keys() for x in sublist])}
    for i in range(num_iterations):
        next_polymers = {x: 0 for x in polymers.keys()}
        for j in next_polymers:
            ch = rules[j]
            count = polymers[j]
            counts[ch] += count
            next_polymers[j[0] + ch] += count
            next_polymers[ch + j[1]] += count
        polymers = next_polymers

    return max(counts.values()) - min(counts.values())


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]


test_data = {'input_test.txt': (1588, 2188189693529), 'input.txt': (2967, 3692219987038)}
for file in test_data.keys():
    result1 = d14(file, 10)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d14(file, 40)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
