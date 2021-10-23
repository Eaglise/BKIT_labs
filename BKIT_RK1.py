# используется для сортировки
from operator import itemgetter

class Conductor:
    """Дирижёр"""
    def __init__(self, id, fio):
        self.id = id
        self.fio = fio

class Orchestra:
    """Оркестр"""
    def __init__(self, id, name, num, con_id):
        self.id = id
        self.name = name
        self.num = num #количество музыкантов в оркестре
        self.con_id = con_id

class ConOrc:
    """
    'Дирижёр оркестра' для реализации связи многие-ко-многим
    """
    def __init__(self, con_id, orc_id):
        self.con_id = con_id
        self.orc_id = orc_id

# Оркестры
orcs = [
    Orchestra(1, 'оркестр имени Осипова', 50, 3),
    Orchestra(2, 'симфонический оркестр Московской филармонии', 33, 5),
    Orchestra(3, 'военный оркестр', 118, 2),
    Orchestra(11, 'сводный духовой оркестр', 24, 1),
    Orchestra(22, 'Смуглянка', 12, 5),
    Orchestra(33, 'Гленн Миллер', 68, 4),
]

# Дирижёры
cons = [
    Conductor(1, 'Иванов'),
    Conductor(2, 'Петров'),
    Conductor(3, 'Смирнов'),
    Conductor(4, 'Спичка'),
    Conductor(5, 'Артемьев'),
]

con_orcs = [
    ConOrc(3,1),
    ConOrc(4,1),
    ConOrc(5,2),
    ConOrc(2,3),
    ConOrc(3,3),
    ConOrc(5,3),
    ConOrc(1,11),
    ConOrc(5,22),
    ConOrc(1,33),
    ConOrc(4,33),
    ConOrc(5,33),
]

def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(c.fio, o.name, o.num)
        for o in orcs
        for c in cons
        if o.con_id==c.id]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.fio, co.orc_id, co.con_id)
        for c in cons
        for co in con_orcs
        if c.id==co.con_id]
    many_to_many = [(o.name, o.num, con_name)
        for con_name, orc_id, con_id in many_to_many_temp
        for o in orcs
        if o.id==orc_id]

    print('Задание А1')
    """
    «Дирижёр» и «Оркестр» связаны соотношением один-ко-многим.
    Выведите список всех связанных дирижёров и оркестров, отсортированный по оркестрам,
    сортировка по дирижёрам произвольная. 
    """
    res_11 = sorted(one_to_many, key = lambda x: str(x[1]).lower())
    print(res_11)

    print('\nЗадание А2')
    """
    «Дирижёр» и «Оркестр» связаны соотношением один-ко-многим.
    Выведите список дирижёров с суммарным количеством музыкантов в каждом оркестре,
    отсортированный по количеству музыкантов.
    """
    res_12_unsorted = []
    # Перебираем всех дирижёров
    for c in cons:
        # Список оркестров дирижёра
        c_orcs = list(filter(lambda i: i[0]==c.fio, one_to_many))
        # Если список не пустой
        if len(c_orcs) > 0:
            # Количество музыкантов оркестра
            o_nums = [num[2] for num in c_orcs]
            # Суммарное количество музыкантов оркестра
            o_nums_sum = sum(o_nums)
            res_12_unsorted.append((c.fio, o_nums_sum))
    # Сортировка по количеству музыкантов
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    """
    «Дирижёр» и «Оркестр» связаны соотношением многие-ко-многим. 
    Выведите список всех оркестров, у которых в названии присутствует слово «оркестр»,
    и список работающих в них дирижёров. 
    """
    res_13 = {}
    # Перебираем все оркестры
    for o in orcs:
        if 'оркестр' in o.name:
            # Список дирижёров оркестра
            o_cons = list(filter(lambda i: i[0]==o.name, many_to_many))
            # Только ФИО дирижёров
            o_cons_names = [x[2] for x in o_cons]
            # Добавляем результат в словарь
            # ключ - оркестр, значение - список фамилий
            res_13[o.name] = o_cons_names
    print(res_13)

if __name__ == '__main__':
    main()
