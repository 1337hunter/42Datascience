class Research:
    def file_reader(self):
        with open("./data.csv", "r") as file:
            data = file.read()
            return data

def CreateDatatable():
    with open("./data.csv", 'w+') as file:
        file.write('head,tail\n0,1\n1,0\n0,1\n1,0\n0,1\n0,1\n0,1\n1,0\n1,0\n0,1\n1,0\n')

def main():
    CreateDatatable()
    data = Research().file_reader()
    print(data, end='')

if __name__ == '__main__':
    main()