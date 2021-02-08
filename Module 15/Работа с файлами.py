heat_waves_file = open('HeatWaves.txt', 'r', encoding='utf8')
for line in heat_waves_file:
    print(line, end='')
heat_waves_file.close()
print()

myFile = open('name_file.txt', 'w')
myFile.write('Write method\n')
print('Print function\n', file=myFile)
myFile.close()

with open('name_file.txt', 'a') as myFile:
    print('You can open file with construction "with open("file.txt", "rt") as Value".'
          'It will close by itself.', file=myFile)
print()

alpha = 'abcdefghijklmnoprstuvwxyz'
ALPHA = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
number = int(input('Введите число, на которое нужно здвинуть текст: '))

summary = ''


def change_char(in_char):
    if in_char in alpha:
        return alpha[(alpha.index(in_char) + number) % (len(alpha) - 1)]
    elif in_char in ALPHA:
        return ALPHA[(ALPHA.index(in_char) + number) % (len(ALPHA) - 1)]
    else:
        return in_char


with open('name_file.txt') as codeFile:
    for line in codeFile:
        for char in line:
            summary += change_char(char)


with open('output_file.txt', 'w') as codeFile:
    codeFile.write(summary)
