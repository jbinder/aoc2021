blockSize = 3

values = []
with open("../input.txt") as file:
    lines = file.readlines()
    values = [int(line) for line in lines]

blockSizes = [0, 0, 0, 0]
index = 0
lastLength = 0
numIncreases = 0

for value in values:
    for i in range(0, len(blockSizes)):
        if index - i < 0:
            continue
        if blockSizes[i] == -1:
            blockSizes[i] = 0
        else:
            blockSizes[i] += value

    currentIndex = (index - (blockSize - 1)) % (len(blockSizes))
    currentLength = blockSizes[currentIndex] if index >= (blockSize - 1) else 0
    if currentLength > 0:
        blockSizes[currentIndex] = -1
    if currentLength > 0 and currentLength > lastLength and lastLength > 0:
        numIncreases += 1
    lastLength = currentLength
    index += 1

print(f"increases: {numIncreases}")
