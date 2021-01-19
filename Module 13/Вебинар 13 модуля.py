sides = [int(input(f'Enter length of the {i+1} side of a triangle: ')) for i in range(3)]

# Вычислим какая сторона самая длинная, какая средняя и какая самая короткая.
# Это не обязательно, но мы же учимся.

triangle_type = ''
long_side = sides[0]
mid_side = sides[0]
short_side = sides[0]

for side in sides:
    if side > long_side:
        mid_side = long_side
        long_side = side
    elif long_side > side > mid_side:
        short_side = mid_side
        mid_side = side
    elif side < short_side:
        mid_side = short_side
        short_side = side

print('Triangle with side length', long_side, mid_side, short_side)

if long_side == mid_side or \
        long_side == short_side or \
        mid_side == short_side:
    triangle_type = ' isosceles'
elif long_side == mid_side == short_side:
    triangle_type = ' equilateral'

if not (sides[0] + sides[1] > sides[2] and     # Зная какая сторона дольше, а какая короче можем упростить условия
        sides[1] + sides[2] > sides[0] and     # последующих операторов.
        sides[2] + sides[0] > sides[1]):
    print('Triangle with such side length is impossible to exist.')
elif short_side**2 + mid_side**2 == long_side**2:     # Если выполняется теорема Пифагора - треугольник прямоугольный.
    triangle_type += ' right'
elif short_side**2 + mid_side**2 < long_side**2:      # Если квадраты катетов меньше - треугольник тупоугольный.
    triangle_type += ' obtuse'
elif short_side**2 + mid_side**2 > long_side**2:      # Если больше - треугольник гостроугольный.
    triangle_type += ' acute'
print(f'This is{triangle_type} triangle')

