import sys
import resource


def ReedFile():
    try:
        with open(sys.argv[1], 'r') as file:
            return file.read()
    except:
        print("File read error")


def main():
    start_resources = resource.getrusage(resource.RUSAGE_SELF)
    red = ReedFile()
    end_resources = resource.getrusage(resource.RUSAGE_SELF)
    pick_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'Peak Memory Usage = {round(pick_memory / (1024 ** 2), 3)}(Gb)')
    
    us_time = end_resources.ru_stime - start_resources.ru_stime + end_resources.ru_utime - start_resources.ru_utime
    print(f'User Mode Time + System Mode Time = {round(us_time, 3)}(s)')


def CheckArguments():
    if len(sys.argv) != 2:
        print("Argument error")

if __name__ == '__main__':
    CheckArguments()
    main()