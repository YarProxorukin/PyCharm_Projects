"""Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате."""

import pickle


class Counter:
    """Задача блока 1"""
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 2
        return self.value


def save_def(count, name):
    with open(name, 'wb') as f:
        pickle.dump(count, f)


def load_def(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


counter1 = Counter(5)
counter2 = Counter(10)
counter3 = Counter(15)

counters = [counter1, counter2, counter3]
save_def(counters, 'counters.bin')
loaded_counters = load_def('counters.bin')

for counter in loaded_counters:
    print(f'Значение счётчика: {counter.value}, Инкремент: {counter.increment()}, Декремент: {counter.decrement()}')

