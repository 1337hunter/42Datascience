import timeit

def Comprehension(emails):
    return [x for x in emails if x.find('@gmail.com') != -1]

def CommonApproach(emails):
    ret = []
    for x in emails:
        if x.find('@gmail.com') != -1:
            ret.append(x)
    return ret

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    i = 0
    start_time = timeit.default_timer()
    while i < 900000:
        Comprehension(emails)
        i += 1
    comprehension_runtime = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    i = 0
    while i < 900000:
        CommonApproach(emails)
        i += 1
    common_runtime = timeit.default_timer() - start_time

    if common_runtime < comprehension_runtime:
        print('it is better to use a loop')
    else:
        print('it is better to use a list comprehension')
    print(comprehension_runtime, common_runtime)


if __name__ == '__main__':
    main()