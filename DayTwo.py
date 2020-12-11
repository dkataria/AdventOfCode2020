from collections import Counter
import AocGetInput

input = AocGetInput.getInput(2)

def partOne(input):
    validcount = 0
    for password in input:
        temp = password.split()
        lower, upper = temp[0].split('-')[0], temp[0].split('-')[1]
        alpha = temp[1][0]
        keyword = temp[2]
        wordcount = Counter(keyword)
        if int(lower) <= wordcount[alpha] <= int(upper):
            validcount += 1
    print(validcount)

def partTwo(input):
    validcount = 0
    for password in input:
        temp = password.split()
        lower, upper = temp[0].split('-')[0], temp[0].split('-')[1]
        alpha = temp[1][0]
        keyword = temp[2]
        if keyword[int(lower)-1] == alpha and keyword[int(upper)-1] != alpha:
            validcount += 1
        elif keyword[int(lower)-1] != alpha and keyword[int(upper)-1] == alpha:
            validcount +=1
    print(validcount)


partOne(input)
partTwo(input)
