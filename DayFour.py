from collections import defaultdict
import AocGetInput

input = AocGetInput.getInput(4)

requiredFields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
validECL = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
numset = set([str(i) for i in range(10)])
alphaset = set([ch for ch in 'abcdef'])


def isValidPassportPartOne(required, available):
    if len(available) > len(required):
        return True
    missingFields = required - available
    if len(missingFields) == 0 or (len(missingFields) == 1 and 'cid' in missingFields):
        return True
    elif len(missingFields) > 1:
        return False

def isValidPassportPartTwo(required, passport):
    fieldDict = defaultdict(bool)

    for each in required:
        fieldDict[each] = False
    for field in passport:
        key = field.split(':')[0]
        value = field.split(':')[1]
        if key == 'byr':
            if 1920 <= int(value) <= 2002:
                fieldDict[key] = True
            else:
                return False
        elif key == 'iyr':
            if 2010 <= int(value) <= 2020:
                fieldDict[key] = True
            else:
                return False
        elif key == 'eyr':
            if 2020 <= int(value) <= 2030:
                fieldDict[key] = True
            else:
                return False
        elif key == 'hgt':
            if value[-2:] == 'cm':
                if 150 <= int(value[:-2]) <= 193:
                    fieldDict[key] = True
                else:
                    return False
            elif value[-2:] == 'in':
                if 59 <= int(value[:-2]) <= 76:
                    fieldDict[key] = True
                else:
                    return False
        elif key == 'hcl':
            if value[0] == '#':
                for ch in value[1:]:
                    if ch not in numset and ch not in alphaset:
                        return False
                fieldDict[key] = True
            else:
                return False
        elif key == 'ecl':
            if value in validECL:
                fieldDict[key] = True
            else:
                return False
        elif key == 'pid':
            if len(value) == 9:
                fieldDict[key] = True
            else:
                return False
    valueSet = set(fieldDict.values())
    if False in valueSet:
        return False
    else:
        return True

def solution(result,partOne):
    index = 0
    validPassports = 0
    passports = len(result)

    while(index<passports):
        if result[index] == '':
            index+=1
            continue

        currPassport = result[index]
        while index+1 < passports and result[index+1] != '':
            currPassport = currPassport + ' ' + result[index+1]
            index+=1

        currPassport = currPassport.split()
        passportFields = set()

        if partOne:
            for each in currPassport:
                key = each.split(':')[0]
                value = each.split(':')[1]
                passportFields.add(key)
            if isValidPassportPartOne(requiredFields, passportFields):
                validPassports+=1
        else:
            if isValidPassportPartTwo(requiredFields, currPassport) is True:
                validPassports+=1
        index+=1
    print(validPassports)

# Pass a flag for part one as True
# Pass a flag for part two as False
solution(input, False)