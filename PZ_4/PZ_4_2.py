# Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
# увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P <25).
# По данному P определить, через сколько месяцев размер вклада превысит 1100 руб.,
# и вывести найденное количество месяцев K (целое число) и итоговый размер вклада S (вещественное число).

p = float(input('Введите кол-во процентов: ')) / 100
if p < 0.25:
    s = 1000
    k = 0
    while s < 1101:
        s += s * p
        k += 1

    print('Итоговый размер вклада составляет: ', s, '\nКол-во месяцев для достижения суммы в 1100р.: ', k)
else:
    print('Процент не может превышать 25!')
print('\nПрограмма завершена!')