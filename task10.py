val = input('Введите числа через запятую: ')
ints_as_strings = val.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)
input()