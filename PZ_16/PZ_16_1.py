""". Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения"""


class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 2


counter = Counter(5)
print(f'Исходное значение: {counter.value}')
counter.increment()
print(f'Значение после инкремента: {counter.value}')
counter.decrement()
print(f'Значение после декремента: {counter.value}')
