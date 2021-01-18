print("\t\tОПЕРАТОРЫ СРАВНЕНИЯ И ЛОГИЧЕСКИЕ ОПЕРАТОРЫ")
print(True or False and not False or True)
print("\nПрактика\n")

year = 2020  # int(input("Введите год: "))
print("Это высокосный год?", year % 4 == 0, "\n")

num = int(123456789)
num = str(num)
print("Строчная проверка:", '5' in num, "\n")

try:
    a = 4  # int(input('Введите число:'))
except ValueError as e:
    print('Ну мы же просили - чи-сло!')
else:
    print(a)
finally:
    print('Ну слава Богу все закончилось.\n')

print('Давайте проверим кратное ли число двум или трем.')
a = 4  # int(input('Введите число:'))
if a % 2 == 0 or a % 3 == 0:
    print('Число кратное двум или трем.\n')

print("Проверка нечетности чисел.")
a = 7  # int(input("Проверка нечетности чисел.\nВведите число а: "))
b = 7  # int(input("А тепреь число b: "))
if a % 2 == 1 and b % 2 == 1:
    print("Числа a и b - нечетные.")
else:
    print("Какое-то из чисел или оба числа четные.")
print('\n')

print('Сверим часы!')
time = '9:30'  # input('Подскажите-ка сколько времени.\n')
time = list(map(int, time.split(':')))
if 6 <= time[0] < 12:
    print('Так это же утро, друг мой!')
print('\n')

print('Определим-ка в какой плоскости находятся наши координаты!')
coordinate = '-9.3'  # input('А какие у нас координаты? Запишите через точку:\n')
coordinate = list(map(int, coordinate.split('.')))
cord = {'x': coordinate[0], 'y': coordinate[1]}
if cord['x'] > 0 and cord['y'] > 0:
    print("Поздравляю, у вас І плоскость.")
elif cord['x'] < 0 < cord['y']:
    print("Поздравляю, у вас ІI плоскость.")
elif cord['x'] < 0 and cord['y'] < 0:
    print("Поздравляю, у вас ІII плоскость.")
else:
    print("Поздравляю, у вас VІ плоскость.")

print('\nА какое у нас время года?')
month = 5  # int(input('Введите номер месяца: '))
if month in [1, 2, 12]:
    print('Теперь зима-зимушка')
elif month in [3, 4, 5]:
    print('Весна-красна жизню принесла.')
elif month in [6, 7, 8]:
    print('Сонце пече, річка тече!..')
elif month in [9, 10, 11]:
    print('Осень - меланхолии пора...')
else:
    print("Не, ну просил же: ме-сяц!")
print('\n')

print('А теперь ударимся в метеорологию')
wind = 5  # float(input('Введите скорость ветра: '))
if 1 <= wind <= 4:
    print(f'Скорость ветра {wind} м/с. Слабый ветер')
elif 4 < wind <= 10:
    print(f'Скорость ветра {wind} м/с. Умеренный ветер')
elif 10 < wind <= 18:
    print(f'Скорость ветра {wind} м/с. Сильный ветер')
elif wind > 18:
    print(f'Скорость ветра {wind} м/с. Ураганный ветер')
else:
    print(f'Скорость ветра меньше 1 м/с. Ветра нет.')
print(' ')

print("Проверка логина и пароля")
login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = 'root'  # input('Введите логин:\n')
if username in login_list:
    password = '1q2w3e4r'  # input('Введите пароль:\n')
    if password_list[username] == password:
        print('Добро пожаловать!')
    else:
        print('Пароль недействителен. Забыли пароль?')
else:
    print('Логин недействителен. Не желаете ли зарегистрироваться?')
print(' ')

a = 95   # int(input('Введите а: '))
print(not(-10 <= a <= -1 or 2 <= a <= 15))

a = 5
b = 56
c = 90
if (a < 45, b >= 45, c >= 45) or (a >= 45, b < 45, c >= 45) or (a >= 45, b >= 45, c < 45):
    print('Один из них импостор.\n')
else:
    print('Все в параде. \n')

a = 85   # int(input('Введите двухзначное число: '))
b = a % 5
c = a // 5
if not (10 <= a <= 99):
    raise ValueError('Ваше число не двухзначное. Вы потеряли свой шанс.')
elif b == 0 and c % 2 == 1 or c in [10, 11]:
    print("В числе эсть цифра 5.\n")
else:
    print("В вашем числе нет цифры 5.\n")

a = [4, 95, 'good', 4.5]
if len(a) == len(set(a)):
    print('Все элементы в списке уникальны.\n')
else:
    print('Не вс элементы в списке уникальны.\n')

a = 12344321
if str(a) == str(a)[::-1]:
    print('Число-палиндром\n')
else:
    print('Число-непалиндром\n')

print('\t\tЦИКЛЫ\n')

print('Найдем сумму натуральных чисел.')
a = 3  # int(input('Введите сколько чисел вы хотите суммировать? '))
s = 0
for i in list(range(1, a+1)):
    s = s + i
    print(s)
print("Сумма всех ваших чисел -", s, '\n')

n = 5  # int(input('Какую елочку хочеш получить? '))
for i in list(range(1, n+1)):
    print('*'*i)
print('|____\n')


s = 0
i = 1
while s <= 500:
    s += i
    i += 1
print(s)

s = 1
i = 1
while True:
    s = i*i
    print(f'Квадрат числа {i} - {s}')
    i += 1
    if s >= 1000:
        break
print()

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for i in random_matrix:
    min_index = 0
    max_index = 0
    min_value = i[min_index]
    max_value = i[max_index]

    for j in range(len(i)):
        if i[j] < min_value:
            min_value = i[j]
            min_index = j
        if i[j] > max_value:
            max_value = i[j]
            max_index = j
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
    mean_value_rows.append(round(sum(i)/len(i), 2))

print(' Минимальные значения -', min_value_rows, '\n',
      "Их индексы", min_index_rows, '\n',
      "Макс значения -", max_value_rows, '\n',
      "Их индексы -", max_index_rows, '\n',
      "Средние значения на строку -", mean_value_rows)
