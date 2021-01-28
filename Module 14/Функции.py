def print_2_add_2():
    a = 2 + 2
    print(f'2 + 2 = {a}')


print_2_add_2()
print()


def divide_num_question(a, n):
    if a % n == 0:
        print(f'{a} делится на {n}')
    else:
        print(f'{a} не делится на {n}')


divide_num_question(9, 2)
print()


def new_year_falls(n=4):
    for i in range(n, 0, -1):
        print('*' * i)
    print()


new_year_falls()
new_year_falls(3)


def get_multipliers(a):
    count = 0
    for n in range(1, a+1):
        if a % n == 0:
            count += 1
    return count


print(get_multipliers(9))
print()


def is_palindrome(text):
    no_spaces = text.replace(' ', '').lower()
    reverse_text = no_spaces[:: -1]
    return reverse_text == no_spaces


print(is_palindrome('text'))
print(is_palindrome('tenet'))


def multiplier(*num):  # '*' разпаковывает кортеж всех аргументов "args" или '**' - словарь всех клавиатурных
    result = 1          # аргументов "kwargs" (названия могут быть любые)
    for n in num:
        result *= n
    return result


print(multiplier(1, 2, 3))
print()


def sum_fact(n):
    if n == 1:
        return 1
    return n + sum_fact(n-1)


print(sum_fact(4))
print()


def reverse_str(str):
    if str == '':
        return ''
    return str[-1] + reverse_str(str[:-1])


print(reverse_str('teak'))
print()


def sum_of_nums(n):
    if n < 1:
        return 0
    return n % 10 + sum_of_nums(n//10)


print(sum_of_nums(361))
print()


def endless_nums(start_from=1, step=1):
    while True:
        yield start_from
        start_from += step


# for num in endless_nums():
#     print(num)
print()


def endless_copy(list):
    while True:
        value = list.pop(0)
        list.append(value)
        yield value


# for i in endless_copy([1, 2, 3]):
#     print(i, end=' ')
print()


a = endless_nums(100, 10)
for i in range(10):
    print(next(a))

print(next(a))
print(next(a))
print()


def try_two(inside_func):
    inside_func()
    inside_func()
    return 0


def hello():
    print('Hello')


test = try_two(hello)
print()


def pow_to(x):
    def pow_wha(a):
        return a**x
    return pow_wha


pow_to_3 = pow_to(3)
print(pow_to_3(2))
print()

import time

def decor_time(fu):
    def wrapper():
        print(f'Запустилась функция {fu}')
        t0 = time.time()
        result = fu()
        dt = time.time() - t0
        print(f'Функция выполнилась за {dt:.10f} sec')
        return dt
    return wrapper



def pow_2():
    return 10000000**2


def in_build_pow ():
    return pow(10000000, 2)


pow_2 = decor_time(pow_2)
in_build_pow = decor_time(in_build_pow)

pow_2()
in_build_pow()

