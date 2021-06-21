import sys
import resource

class FileLine:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.file = open(self.file_name, 'r')
        except:
            print("File open error")
            exit()
    def __call__(self):
        return self.file.readline().strip()



def main():
    my_best_class = FileLine(sys.argv[1])
    start_resources = resource.getrusage(resource.RUSAGE_SELF)

    while my_best_class():
        pass

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