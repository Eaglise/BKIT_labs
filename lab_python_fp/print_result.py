# Здесь должна быть реализация декоратора
def print_result(func):
    def wrap(*args, **kwargs):
        print(func.__name__)
        var = func(*args, **kwargs)
        if type(var) == list:
            for i in var:
                print(i)
        elif type(var) == dict:
            for i in var:
                print(i, " = ", var[i])
        else:
            print(var)
        return func(*args, **kwargs)
    return wrap

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()