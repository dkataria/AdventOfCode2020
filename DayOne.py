
import AocGetInput
input = AocGetInput.getInput(1)


temp = [int(x) for x in input]
numset = set(temp)
target = 2020
result = 0

# part 1: two sum
def partOne(input):
    for num in input:
        if target - num in numset:
            result = num * (target - num)
            return result

# part 2: three sum
def partTwo(input):
    for i in range(len(input) -1):
        for j in range(i+1, len(input)):
            curr = target - input[i] - input[j]
            if curr in numset:
                result = input[i] * input[j] * curr
                return result

print(partOne(temp))
print(partTwo(temp))
