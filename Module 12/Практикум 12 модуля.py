per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = [money*per_cent['ТКБ'], money*per_cent['СКБ'], money*per_cent['ВТБ'], money*per_cent['СБЕР']]
print(deposit)
