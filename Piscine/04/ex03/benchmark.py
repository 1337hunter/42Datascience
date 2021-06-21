import sys
import timeit
from functools import reduce

def Loop(arr):
    result = 0
    for num in arr:
        result = result + num * num
    return result


def MakeLoop(loops, n):
    start_time = timeit.default_timer()
    arr = range(1, n + 1)
    i = 0
    while i < loops:
        Loop(arr)
        i += 1
    return timeit.default_timer() - start_time


def Reduce(arr):
    return reduce(lambda x, y: x + y * y, arr)

def MakeReduce(loops, n):
    start_time = timeit.default_timer()
    arr = range(1, n + 1)
    i = 0
    while i < loops:
        Reduce(arr)
        i += 1
    return timeit.default_timer() - start_time


def MakeCommands():
    commands = {}
    commands["loop"] = MakeLoop
    commands['reduce'] = MakeReduce
    return commands

def main(av):
    commands = MakeCommands()
    print(commands[av[0]](int(av[1]), int(av[2])))

        

def CheckArguments():
    av = sys.argv[1:]
    commands = MakeCommands()
    if len(av) != 3:
        print("Wrong argument number")
        exit()
    if av[0] not in commands.keys():
        print("Wrong command")
        exit()
    if not av[1].isdigit() or not av[2].isdigit():
        print("Number of loops must be digit")
        exit()

if __name__ == '__main__':
    CheckArguments()
    main(sys.argv[1:])