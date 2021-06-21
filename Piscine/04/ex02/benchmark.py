import timeit
import sys

def AddToList(x, new_list):
    if x.find('@gmail.com') != -1:
        new_list.append(x)

def Map(emails):
    new_list = []
    list(map(lambda x: AddToList(x, new_list),  emails))
    return new_list

def Filter(emails):
    return list(filter(lambda x: '@gmail.com' in x, emails))

def Comprehension(emails):
    return [x for x in emails if x.find('@gmail.com') != -1]

def CommonApproach(emails):
    ret = []
    for x in emails:
        if x.find('@gmail.com') != -1:
            ret.append(x)
    return ret

def MakeLoop(n, emails):
    start_time = timeit.default_timer()
    i = 0
    while i < n:
        CommonApproach(emails)
        i += 1
    return timeit.default_timer() - start_time

def MakeComprehension(n, emails):
    i = 0
    start_time = timeit.default_timer()
    while i < n:
        Comprehension(emails)
        i += 1
    return timeit.default_timer() - start_time

def MakeMap(n, emails):
    i = 0
    start_time = timeit.default_timer()
    while i < n:
        Map(emails)
        i += 1
    return timeit.default_timer() - start_time

def MakeFilter(n, emails):
    i = 0
    start_time = timeit.default_timer()
    while i < n:
        Filter(emails)
        i += 1
    return timeit.default_timer() - start_time

def MakeCommands():
    commands = {}
    commands["loop"] = MakeLoop
    commands["list_comprehension"] = MakeComprehension
    commands["map"] = MakeMap
    commands["filter"] = MakeFilter
    return commands

def main(av):
    commands = MakeCommands()
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    print(commands[av[0]](int(av[1]), emails))

        

def CheckArguments():
    av = sys.argv[1:]
    commands = MakeCommands()
    if len(av) != 2:
        print("Wrong argument number")
        exit()
    if av[0] not in commands.keys():
        print("Wrong command")
        exit()
    if not av[1].isdigit():
        print("Number of loops must be digit")
        exit()

if __name__ == '__main__':
    CheckArguments()
    main(sys.argv[1:])