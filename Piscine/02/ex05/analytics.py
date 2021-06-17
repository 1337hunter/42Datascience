import sys
from random import randint
from config import num_of_steps

class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0
            for peace in self.data:
                heads += peace[0]
                tails += peace[1]
            return heads, tails
        def fractions(self):
            heads, tails = self.counts()
            return heads * 100 / (heads + tails), tails * 100/ (heads + tails)

    
    def __init__(self, file_name):
        self.file_name = file_name

    def TimeRequest():
        res = urlopen('http://just-the-time.appspot.com/')
        result = res.read().strip()
        result_str = result.decode('utf-8')
        return result_str
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

    def validate_content(self, content):
        if len(content) != 2:
            raise Exception('Bad file content', 'Not enougth data content')
        if not content[0].isnumeric() or not content[1].isnumeric():
            print(content[0], not content[0].isdigit(), content[1], not content[1].isdigit())
            raise Exception('Bad file content', "Table data must be digital")
        if int(content[0]) not in (1, 0) or int(content[1]) not in (1, 0):
            raise Exception('Bad file content', "Data content must be 0 or 1")
        if int(content[0]) == int(content[1]):
            raise Exception('Bad file content', "(contains equel numbers)")
        return [int(content[0]), int(content[1])]
    
    def file_reader(self, has_header=True):
        with open(self.file_name, "r") as file:
            line = file.readline()
            if line and has_header:
                self.check_file_header(line.split(','), line.strip())
                line = file.readline()
            strs = 0
            data = []
            while line:
                strs += 1
                self.check_content_alignent(line.split(','))
                data += [self.validate_content(line.strip().split(','))]
                line = file.readline()
            if strs < 1:
                raise Exception('File has no content')
            return data


class Analitics(Research.Calculations):
    def predict_random(self):
        i = 0
        predictions = []
        while i < num_of_steps:
            predict = randint(0, 1)
            predictions += [[predict, 0 if predict == 1 else 1]]
            i += 1
        return predictions
    def predict_last(self):
        return self.data[-1]
    
    def save_file(self, data, name, ext):
        with open('./' + name + '.' + ext, 'w+') as file:
            file.write(data)

def CheckArguments(av):
    if len(av) != 1:
        raise Exception('Wrong argument', "The argument number is not one")

def CreateDatatable(path):
    with open(path, 'w+') as file:
        file.write('head,tail\n0,1\n1,0\n0,1\n1,0\n0,1\n0,1\n0,1\n1,0\n1,0\n0,1\n1,0\n')