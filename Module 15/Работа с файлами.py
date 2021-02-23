heatWaves = open('HeatWaves.txt', 'r')
print(heatWaves.read(13))
print(heatWaves.read(5))
print(heatWaves.readline())
print(heatWaves.readlines())
print()

myFile = open('name_file.txt', 'w')
myFile.write('"Write" method without new line\n')
print('"Print" function with new line on the end of this string\n', file=myFile)
myFile.flush()
myFile.close()

with open('name_file.txt', 'a') as myFile:
    myFile.write('You can open file with construction "with open("file.txt", "rt") as \'Value\'".'
                 'It will close by itself.')


def change_char(text, n=1):
    alpha = 'abcdefghijklmnoprstuvwxyz'
    alpha_up = alpha.upper()
    summary = ''
    for char in text:
        if char in alpha:
            summary += alpha[(alpha.index(char) + n) % len(alpha)]
        elif char in alpha_up:
            summary += alpha_up[(alpha_up.index(char) + n) % len(alpha)]
        else:
            summary += char
    return summary


with open('name_file.txt', 'r') as inputFile:
    with open('output_file.txt', 'w') as outputFile:
        outputFile.write(change_char(inputFile.read()))
