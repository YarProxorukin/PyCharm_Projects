# С начала суток прошло N секунд (N – целое). Найти количество полных минут, прошедших с начала последнего часа.
def seconds():  # объявление функции
    n = input('Введите количество секунд: ')
    if n.isdigit():  # проверка на число
        m = int(n) // 60
        m = m % 60
        print('Количество полных минут: ', m)
    else:
        seconds()  # перезапуск, если введены не числа


seconds()
print('Программа успешно завершена!')