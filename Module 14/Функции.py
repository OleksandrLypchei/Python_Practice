def print_2_add_2():
    a = 2 + 2
    print(f'2 + 2 = {a}')


print_2_add_2()
print()


def hello_world():
    print('Hello World!')


hello_world()
print()


def pow_func(base_to_pow, n=2):
    result = base_to_pow**n
    return result


print('Powered 3 is ', pow_func(3))
print('10 powered into 3 is ', pow_func(10, 3))
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


def multiplyer(*num):  # '*' разпаковывает кортеж всех аргументов "args" или '**' - словарь всех клавиатурных
    result = 1          # аргументов "kwargs" (названия могут быть любые)
    for n in num:
        result *= n
    return result


print(multiplyer(1, 2, 3))
print()


def sum_funk(n):
    if n == 1:
        return 1
    else:
        return n + sum_funk(n-1)


print('Сумма всех чисед до 4 -', sum_funk(4))
print()


def reverse_string(str):
    if len(str) == 0:
        return ''
    return str[-1] + reverse_string(str[:-1])


print(reverse_string('Does it reverse?'))
print()

def sum_numbers_in(numb):
    if numb < 1:
        return 0
    return (numb % 10) + sum_numbers_in(numb//10)


print(sum_numbers_in(321))
print()
