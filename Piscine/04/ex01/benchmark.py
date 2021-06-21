import timeit

def AddToList(x, new_list):
    if x.find('@gmail.com') != -1:
        new_list.append(x)

def Map(emails):
    new_list = []
    list(map(lambda x: AddToList(x, new_list),  emails))
    return new_list

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
    d = {}
    start_time = timeit.default_timer()
    while i < 90000:
        Comprehension(emails)
        i += 1
    comprehension_runtime = timeit.default_timer() - start_time
    d[comprehension_runtime] = 'list comprehension'

    start_time = timeit.default_timer()
    i = 0
    while i < 90000:
        CommonApproach(emails)
        i += 1
    common_runtime = timeit.default_timer() - start_time
    d[common_runtime] = 'loop'

    i = 0
    start_time = timeit.default_timer()
    while i < 90000:
        Map(emails)
        i += 1
    map_runtime = timeit.default_timer() - start_time
    d[map_runtime] = 'map'
    keys = list(d.keys())
    keys.sort()
    print(keys)
    print(f'its better to use {d[keys[0]]}')
    print(comprehension_runtime, 'vs', common_runtime, 'vs', map_runtime)
        

     

if __name__ == '__main__':
    main()