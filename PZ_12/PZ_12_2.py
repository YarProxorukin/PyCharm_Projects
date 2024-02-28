"""
Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.
"""


def lowercase_generator(input_string):
    for symbol in input_string:
        if symbol.isupper():
            yield symbol.lower()
        else:
            yield symbol


input_string = input(str('Введите строку: '))
lowercase_result = ''.join(lowercase_generator(input_string))
print(f'Строка в нижнем регистре: {lowercase_result}')
