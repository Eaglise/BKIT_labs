import json
from cm_timer import cm_timer_1
import unique
from print_result import print_result
from gen_random import gen_random

path = "data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    jobs = list(sorted(unique.Unique((i['job-name'] for i in data), ignore_case=True)))
    return jobs

@print_result
def f2(arg):
    jobs_filtered = list(filter(lambda x: str(x)[0:11].lower()=='программист', arg))
    return jobs_filtered

@print_result
def f3(arg):
    moddified = list(map(lambda x: str(x)+' с опытом Python', arg))
    return moddified

@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    salary = list(map(lambda x: " зарплата " + str(x) + " руб.", salary))
    return list(zip(arg, salary))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))


