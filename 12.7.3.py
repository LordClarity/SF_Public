per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
deposit = [money/100*per_cent['ТКБ'],money/100*per_cent['СКБ'],money/100*per_cent['ВТБ'],money/100*per_cent['СБЕР']]
deposit = list(map(int, deposit))
print (deposit)
print ('Максимальная сумма, которую вы можете заработать -',max(deposit))