labyrinth = []

with open('labyrinth.txt') as myFile:
    for line in myFile:
        labyrinth.append(line.replace('\n', '').split(' '))


line_num = 0
for line in labyrinth:
    plate_num = 0
    for plate in line:
        if plate == '1':
            labyrinth[line_num][plate_num] = '-1'
        elif plate == 'a':
            labyrinth[line_num][plate_num] = '1'
            pozIn = (line_num, plate_num)
        elif plate == 'b':
            labyrinth[line_num][plate_num] = '0'
            pozOut = (line_num, plate_num)
        else:
            labyrinth[line_num][plate_num] = '0'
        plate_num += 1
    line_num += 1

if not pozOut:
    print('Maze has no solution.')

for line in labyrinth:
    print(line)