mapNumbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight  ': 8,
    'nine': 9
}

with open('input.txt', 'r') as file:
    sum = 0
    for line in file.readlines():
        lineNumber = ''
        for i, (key, value) in enumerate(mapNumbers.items()):
            line = line.replace(key, str(value))
        for char in line:
            if str(char).isnumeric():
                lineNumber += char
        sum += int(lineNumber[0] + lineNumber[-1])

    print(sum)