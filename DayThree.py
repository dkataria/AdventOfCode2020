import AocGetInput

input = AocGetInput.getInput(3)

def partOne(result, rightStep, downStep):
    rows = len(result)
    cols = len(result[0])
    currentRow, index, treeCount = 0, 0, 0

    while currentRow < rows:
        if result[currentRow][index] == '#':
            treeCount +=1
        index = (index + rightStep) % cols
        currentRow +=downStep

    return treeCount

def partTwo(result):
    product = 1
    for each in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        product = product * partOne(result, each[0], each[1])
    return product

print(partOne(input, 3, 1))
print(partTwo(input))
