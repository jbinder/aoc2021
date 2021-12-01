with open("../input.txt") as file:
    lastNum = -1
    numIncreases = 0
    for line in file:
        value = int(line)
        if 0 <= lastNum < value:
            numIncreases += 1
        lastNum = value

    print(f"increases: {numIncreases}")
