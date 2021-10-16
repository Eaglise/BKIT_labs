class Unique:
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False
        self.it = iter(items)
        self.rep = set()

    def __next__(self):
        while True:
            next_ = next(self.it)
            if self.ignore_case and isinstance(next_, str):
                rep_low = (i.lower() for i in self.rep)
                if next_.lower() not in rep_low:
                    self.rep.add(next_)
                    return next_
            elif next_ not in self.rep:
                self.rep.add(next_)
                return next_

    def __iter__(self):
        return self

if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data1):
        print(i)
    data2 = ['a','A','B','b']
    for i in Unique(data2, ignore_case=True):
        print(i)