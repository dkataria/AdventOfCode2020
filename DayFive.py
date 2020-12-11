import math
import AocGetInput

input = AocGetInput.getInput(5)

def narrowDown(total, lower, upper):
    for curr in total[:len(total)-1]:
        if curr == 'F' or curr == 'L':
            upper = lower + math.floor((upper-lower)/2)
        elif curr == 'B' or curr == 'R':
            lower = lower + math.ceil((upper-lower)/2)
    if total[-1] == 'F' or total[-1] == 'L':
        return lower
    elif total[-1] =='B' or total[-1] == 'R':
        return upper

def solutionOne(input):

    maxSeatID = 0
    for each in input:
        row = narrowDown(each[:len(each)-3], 0, 127)
        seat = narrowDown(each[-3:], 0, 7)
        maxSeatID = max(maxSeatID, row * 8 + seat)

    print('Max seat ID is: ', maxSeatID)

def solutionTwo(input):
    maxSeatID = 0
    yourSeat = 0
    seatIDS = []
    for each in input:
        row = narrowDown(each[:len(each)-3], 0, 127)
        seat = narrowDown(each[-3:], 0, 7)
        maxSeatID = max(maxSeatID, row * 8 + seat)
        seatIDS.append(row * 8 + seat)

    seatIDS.sort()
    for index in range(1,len(seatIDS)):
        if seatIDS[index] - 1 != seatIDS[index-1]:
            yourSeat = seatIDS[index] - 1
            break

    print('Your seat id is: ', yourSeat)

solutionOne(input)
solutionTwo(input)

