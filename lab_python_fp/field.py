goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    if len(args) == 1:
        for dict in items:
            if args[0] in dict.keys():
                yield dict[args[0]]
    else:
        for dict in items:
            checked = set(args) & set(dict.keys())
            if bool(checked) == True:
                yield {arg:dict[arg] for arg in args if arg in checked}

if __name__ == '__main__':
    list1 = field(goods, 'title')
    for i in list1:
        print(i)
    dict1 = field(goods, 'title', 'price')
    for i in dict1:
        print(i)
