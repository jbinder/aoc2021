import statistics


def d07(file_name, incremental_fuel):
    positions = get_input(file_name)
    if not incremental_fuel:
        med = statistics.median(positions)
        return sum([abs(x-med) for x in positions])
    else:
        med = round(statistics.mean(positions))
        m = sum([sum(range(1, abs(x - (med - 1)) + 1)) for x in positions])
        for i in range(1, 3):
            m = min(m, sum([sum(range(1, abs(x - (med + i)) + 1)) for x in positions]))
        return m


def get_input(file_name):
    with open(file_name, 'r') as f:
        return [int(x) for x in f.readlines()[0].split(',')]


test_data = {'input_test.txt': (37, 168), 'input.txt': (337833, 96678050)}
for file in test_data.keys():
    result1 = d07(file, False)
    print(f"{file}/1: {result1} {result1 == test_data[file][0]}")
    result2 = d07(file, True)
    print(f"{file}/2: {result2} {result2 == test_data[file][1]}")
