from random import randint

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)

if __name__ == '__main__':
    nums = gen_random(5, 1, 3)
    for i in nums:
        print(i)
