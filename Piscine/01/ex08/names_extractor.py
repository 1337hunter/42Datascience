import sys

def Convert(line):
    splited1 = line.split('.')
    splited2 = splited1[1].split('@')
    name = str(splited1[0][0]).upper() + (splited1[0].lower())[1:]
    surename = str(splited2[0][0]).upper() + (splited2[0].lower())[1:]
    return name + '\t' + surename + '\t' + line + '\n'


def TranslateEmails(path):
    with open(path, 'r') as inf:
        with open('./employees.tsv', 'w+') as ouf:
            ouf.write("Name\tSurename\tE-mail\n")
            line = inf.readline().strip()
            while line:
                ouf.write(Convert(line))
                line = inf.readline().strip()

def main(argv):
    if (len(argv) != 1):
        return
    TranslateEmails(argv[0])
if __name__ == '__main__':
    main(sys.argv[1:])