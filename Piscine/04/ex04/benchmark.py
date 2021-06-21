import timeit
import random
from collections import Counter

def function1(numbers):
    d = {}
    for i in range(0, 101):
        d[i] = 0
    for n in numbers:
        d[n] += 1

def function2(numbers):
    d = {}
    for i in range(0, 101):
        d[i] = 0
    for n in numbers:
        d[n] += 1
    swapped = dict((v,k) for k,v in d.items())
    values = sorted(list(swapped.keys()))
    ret = []
    i = -1
    while i > -11:
        ret.append(swapped[values[i]])
        i -= 1
    return ret

def Count1(numbers):
    d = dict(Counter(numbers))


def Count2(numbers):
    d = dict(Counter(numbers).most_common(10))
    return d
    

def main():
    numbers = [random.randrange(0, 101) for i in range(100000000)]

    start_time = timeit.default_timer()
    function1(numbers)
    print('my function:\t',timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    Count1(numbers)
    print('Counter:\t', timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    function2(numbers)
    print('my top:\t\t', timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    Count2(numbers)
    print("Counter's top:\t", timeit.default_timer() - start_time)
    


if __name__ == '__main__':
    main()