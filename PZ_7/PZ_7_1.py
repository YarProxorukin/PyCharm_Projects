# Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S вставить строку S0.

symbol = 'C'
s = 'C aaaC aCaaa CCaaaa'
s0 = '101'
s = s.replace(symbol, s0 + symbol)
print(s)
print('Программа завершена!')
