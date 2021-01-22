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
print(not (-10 <= a <= -1 or 2 <= a <= 15))

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
for i in list(range(1, a + 1)):
    s = s + i
    print(s)
print("Сумма всех ваших чисел -", s, '\n')

n = 5  # int(input('Какую елочку хочеш получить? '))
for i in list(range(1, n + 1)):
    print('*' * i)
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
    s = i * i
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

for row in random_matrix:
    min_index = 0
    max_index = 0
    min_value = row[min_index]
    max_value = row[max_index]

    for j in range(len(row)):
        if row[j] < min_value:
            min_value = row[j]
            min_index = j
        if row[j] > max_value:
            max_value = row[j]
            max_index = j
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
    mean_value_rows.append(round(sum(row) / len(row), 2))

print(' Минимальные значения -', min_value_rows, '\n',
      "Их индексы", min_index_rows, '\n',
      "Макс значения -", max_value_rows, '\n',
      "Их индексы -", max_index_rows, '\n',
      "Средние значения на строку -", mean_value_rows, '\n')


print('Давайте попрактикуемся с "enumerate"')
list_ = [-5, 2, 4, 8, 12, -7, 5]
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
print()

print("Давайте посчитаем символы в тексте")
text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()
text = text.replace('\n', '')
text = text.replace(' ', '')

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char, cnt in count.items():
    print(f'Символ {char} встречается {cnt} раз\n')

print('Давайте преждевременно остановим цикл.\n'
      'Нужно роверить, является ли заданное число степенью тройки.')
n = 81  # int(input("Введите число: "))
step = 0
while True:
    if n % 3 == 0:
        n = n // 3
        step += 1
        if n // 3 == 1:
            break
    else:
        print('Число не является тройкой в какой-то степени.')
        break
print(f'Число является тройкой в {step} степени\n')

print('Проверим гипотезу Сикаруз.')  # Гипотеза Сиракуз гласит:
n = 3  # int(input("Введите любое число."))  # Любое натуральное число сводимо к единице,
i = 0
while not n == 1:  # при следующих действиях над ним:
    if n % 2 == 0:  # 1. Если число четное, то разделить его пополам.
        n = n / 2
    else:  # 2. Если нечетное — умножить на 3, прибавить 1
        n = (n * 3 + 1) / 2  # и результат разделить на 2.
    i += 1
    print(f'После {i} итерации наше число -', n)
print()

print('Попробовали "break", перейдем на "continue".\n')
print("В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. \n"
      "Узнайте число фазанов и число кроликов.\n")

legs = 94
heads = 35

for rab in range(heads + 1):
    for birds in range(heads + 1):
        if rab + birds > heads or \
                (rab * 4 + birds * 2) > legs:
            continue
        elif rab + birds < heads or \
                (rab * 4 + birds * 2) < legs:
            continue
        else:
            print(f"Возможно там {rab} кроликов и {birds} фазанов.\n")

a = 2  # int(input())

if 100 < a < 999:
    if a % 2 == 0:
        if a % 3 == 0:
            print("Число отвечает требованиям")

if type(a) is int and \
        100 < a < 999 and \
        a % 2 == 0 and a % 3 == 0:
    print("Число отвечает требованиям")

if all([type(a) is int,
        100 < a < 999,
        a % 2 == 0, a % 3 == 0]):
    print("Число отвечает требованиям")

nums = [1, 0]  # list(map(int, input('Введите числа через пробел: ').split()))
print(all(nums))
print(not any(nums))

squares = [(a, a**2) for a in range(1, 11) if a % 2 == 0]
print(squares)
print()

M = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(M)
print()

# L = [int(input("Число:")) % 2 == 0 for i in range(5) if i % 2 == 0]
# print(L)

L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10, 0, -1)]

F = [a + b for a, b in zip(L, M)]
print(F)


in_word = 'aaabbccccdaa'  # input('Enter codeword')
char = in_word[0]
count = 0
result = ''
for a in in_word:
    if a == char:
        count += 1
    else:
        result += char + str(count)
        char = a
        count = 1
result += char + str(count)
print(result)
