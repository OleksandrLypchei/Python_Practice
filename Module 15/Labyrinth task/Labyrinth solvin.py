def find(maze, fin_point):
    for weight in range(1, len(maze) * len(maze[0])):
        for line in range(len(maze)):
            for plate in range(len(maze[0])):
                if maze[line][plate] == weight:
                    # Up
                    if maze[line - 1][plate] == 0:
                        maze[line - 1][plate] = weight + 1
                    # Down
                    if maze[line + 1][plate] == 0:
                        maze[line + 1][plate] = weight + 1
                    # Left
                    if maze[line][plate - 1] == 0:
                        maze[line][plate - 1] = weight + 1
                    # Right
                    if maze[line][plate + 1] == 0:
                        maze[line][plate + 1] = weight + 1
                    # Finding final point
                    if (line, plate) == fin_point:
                        return True
    return False


def print_path(maze,  fin_point):
    line = fin_point[0]
    plate = fin_point[1]
    weight = maze[line][plate]
    result = list(range(weight))
    while weight:
        # We're going backwards here, so writing arrows backwards too.
        weight -= 1
        if maze[line + 1][plate] == weight:
            result[weight] = '▲'
            line += 1
        if maze[line - 1][plate] == weight:
            result[weight] = '▼'
            line -= 1
        if maze[line][plate - 1] == weight:
            result[weight] = '▶'
            plate -= 1
        if maze[line][plate + 1] == weight:
            result[weight] = '◀'
            plate += 1
    return result[1:]


labyrinth = []

with open('labyrinth.txt') as myFile:
    for line in myFile:
        labyrinth.append(line.replace('\n', '').split(' '))

pozOut = 0
line_num = 0
for line in labyrinth:
    plate_num = 0
    for plate in line:
        if plate == '1':
            labyrinth[line_num][plate_num] = -1
        elif plate == 'a':
            labyrinth[line_num][plate_num] = 1
            pozIn = (line_num, plate_num)
        elif plate == 'b':
            labyrinth[line_num][plate_num] = 0
            pozOut = (line_num, plate_num)
        else:
            labyrinth[line_num][plate_num] = 0
        plate_num += 1
    line_num += 1

if not find(labyrinth, pozOut):
    print('Maze has no solution.')
else:
    result = print_path(labyrinth, pozOut)

    for i in labyrinth:
        for line in i:
            print("{:^3}".format(line), end=' ')
        print()
    print('Moves, we need to make to find the way out:')
    for arrow in result:
        print("{:^4}".format(arrow), end='')