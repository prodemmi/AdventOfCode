import os
import time

start = time.time()

mapNumbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def checkCharStackIsInNumbers(stack: str):
    for number in mapNumbers.keys():
        if number in stack:
            return mapNumbers.get(number)
        
    return None

def detectNumber(line: str, reversed: bool = False):
    charStack= ''
    for char in line:
        char = str(char)
        if reversed:
            charStack = char + charStack
        else:
            charStack += char

        if char.isnumeric():
            return char
        
        isInNumbers = checkCharStackIsInNumbers(charStack)
        if isInNumbers:
            return isInNumbers

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    sum = 0
    for line in file.readlines():
            line = line.strip()
            first = detectNumber(line)
            second = detectNumber(line[::-1], True)
            sum += int(first + second)

    print(sum)

end = time.time()

print(end - start)