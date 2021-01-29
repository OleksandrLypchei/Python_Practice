import time


def how_much_done(fn):
    n = 0

    def wrapper(*args, **kwargs):
        nonlocal n
        result = fn(*args, **kwargs)
        n += 1
        print('Count -', n)
        return result
    return wrapper


@how_much_done
def printt(*args):
    print(*args)
    return 0


def print_2_add_2():
    a = 2 + 2
    printt(f'2 + 2 = {a}')


print_2_add_2()
print()


def divide_num_question(a, n):
    if a % n == 0:
        printt(f'{a} делится на {n}')
    else:
        printt(f'{a} не делится на {n}')


divide_num_question(9, 2)
print()


def new_year_falls(n=4):
    for i in range(n, 0, -1):
        printt('*' * i)
    print()


new_year_falls()
new_year_falls(3)


def get_multipliers(a):
    count = 0
    for n in range(1, a+1):
        if a % n == 0:
            count += 1
    return count


printt(get_multipliers(9))
print()


def is_palindrome(text):
    no_spaces = text.replace(' ', '').lower()
    reverse_text = no_spaces[:: -1]
    return reverse_text == no_spaces


printt(is_palindrome('text'))
printt(is_palindrome('tenet'))


def multiplier(*num):  # '*' разпаковывает кортеж всех аргументов "args" или '**' - словарь всех клавиатурных
    result = 1          # аргументов "kwargs" (названия могут быть любые)
    for n in num:
        result *= n
    return result


printt(multiplier(1, 2, 3))
print()


def sum_fact(n):
    if n == 1:
        return 1
    return n + sum_fact(n-1)


printt(sum_fact(4))
print()


def reverse_str(str):
    if str == '':
        return ''
    return str[-1] + reverse_str(str[:-1])


printt(reverse_str('teak'))
print()


def sum_of_nums(n):
    if n < 1:
        return 0
    return n % 10 + sum_of_nums(n//10)


printt(sum_of_nums(361))
print()


def endless_nums(start_from=1, step=1):
    while True:
        yield start_from
        start_from += step


# for num in endless_nums():
#     printt(num)
print()


def endless_copy(list):
    while True:
        value = list.pop(0)
        list.append(value)
        yield value


# for i in endless_copy([1, 2, 3]):
#     printt(i, end=' ')
print()


a = endless_nums(100, 10)
for i in range(10):
    printt(next(a))

printt(next(a))
printt(next(a))
print()


def try_two(inside_func):
    inside_func()
    inside_func()
    return 0


def hello():
    printt('Hello')


test = try_two(hello)
print()

pi = 3.14159


def sq_round(r):
    result = 2 * pi * r
    return result


def pow_to_what(n):
    def what_to_pow(c):
        result = c ** n
        return result
    return what_to_pow


square_it = pow_to_what(2)
printt(square_it(5))
print()


def decor_time(fu):
    def wrapper():
        t0 = time.time()
        result = fu()
        dt = time.time() - t0
        return dt
    return wrapper


def pow_2():
    return 10000000**2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decor_time(pow_2)
in_build_pow = decor_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
N = 100

for i in range(N):
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()
printt(f"Функция {pow_2} выполнилась {N} раз. Среднее время выполнения - {mean_pow_2/N}")
printt(f"Функция {in_build_pow} выполнилась {N} раз. Среднее время выполнения - {mean_in_build_pow/N}")


def decor_strings(fu):
    printt('Я выполнюсь до функции')
    result = fu()
    printt("Я выполнюсь после функции")
    return result


def print_pow():
    return printt(pow(100000, 2))


def cache(fui):
    mem = {}

    def wrapper(n):
        nonlocal mem
        if n in mem:
            return mem[n]
        else:
            mem[n] = fui(n)
            return mem[n]
    return wrapper

@cache
def f(n):
    return n * 123456789


n = int(input())
f(n)