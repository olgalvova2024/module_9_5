class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError('Шаг указан не верно')

    def __iter__(self):
        if self.start > self.stop and self.step > 0:
            self.i = 1
        else:
            self.pointer = self.start
            self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.start < self.stop and self.step > 0:
                self.pointer += self.step
                if self.pointer > self.stop:
                    self.pointer -= self.step
                    raise StopIteration()
            elif self.start > self.stop and self.step < 0:
                self.pointer += self.step
                if self.pointer < self.stop:
                    self.pointer -= self.step
                    raise StopIteration()
            else:
                raise StopIteration()
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
print('*'*33)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
     print(i, end=' ')
     print()
print('*'*33)

for i in iter3:
    print(i, end=' ')
    print()
print('*'*33)
for i in iter4:
     print(i, end=' ')
     print()
print('*' * 33)
for i in iter5:
     print(i, end=' ')
     print()

