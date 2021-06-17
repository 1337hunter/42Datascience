import sys

class Research:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_file_header(self, origin, line):
        check = line.split(',')
        if not line or len(check) != 2:
            raise Exception('Bad file header')
        if origin[0][-1].isspace() or origin[0][0].isspace() or (len(origin[1]) > 1 and origin[1][0].isspace()) or origin[1][-1] != '\n':
            raise Exception('Bad file content', "Bad header alignment")
        if len(origin[1]) > 2 and origin[1][-2].isspace():
            raise Exception('Bad file content', "Bad header alignment")
            

    def check_content_alignent(self, line):
        if len(line[0]) > 1 or (len(line[1]) > 2 and line[1][1] != '\n'):
            raise Exception('Bad file content', "Bad data alignment")

    def check_file_content(self, content):
        if len(content) != 2:
            raise Exception('Bad file content', 'Not enougth data content')
        if not content[0].isnumeric() or not content[1].isnumeric():
            print(content[0], not content[0].isdigit(), content[1], not content[1].isdigit())
            raise Exception('Bad file content', "Table data must be digital")
        if int(content[0]) not in (1, 0) or int(content[1]) not in (1, 0):
            raise Exception('Bad file content', "Data content must be 0 or 1")
        if int(content[0]) == int(content[1]):
            raise Exception('Bad file content', "(contains equel numbers)")

    def file_reader(self):
        with open(self.file_name, "r") as file:
            line = file.readline()
            self.check_file_header(line.split(','), line.strip())
            strs = -1
            while line:
                strs += 1
                line = file.readline()
                if line:
                    self.check_content_alignent(line.split(','))
                    self.check_file_content(line.strip().split(','))
            if (strs < 1):
                raise Exception('File has no content')
        with open(self.file_name, "r") as file:
            data = file.read()
            return data

def CheckArguments(av):
    if len(av) != 1:
        raise Exception('Wrong argument', "The argument number is not one")


def CreateDatatable(path):
    with open(path, 'w+') as file:
        file.write('head,tail\n0,1\n1,0\n0,1\n1,0\n0,1\n0,1\n0,1\n1,0\n1,0\n0,1\n1,0\n')

def main(av):
    CheckArguments(av)
    CreateDatatable(av[0])
    data = Research(av[0]).file_reader()
    print(data, end='')

if __name__ == '__main__':
    main(sys.argv[1:])