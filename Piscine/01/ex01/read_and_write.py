def CorrectLine(line):
    i = 0
    new_line = ""
    while i <  len(line):
        if line[i] == '"' or line[i] == '\'':
            ch = line[i]
            new_line += ch
            i += 1
            while i < len(line) and line[i] != ch:
                new_line += line[i]
                i += 1
            new_line += line[i]
            i += 1
            if i < len(line) and line[i] == ',':
                new_line += '\t'
            elif i < len(line):
                new_line += line[i]
            print(new_line)
        else:
            while i < len(line) and line[i] != ',':
                new_line += line[i]
                i += 1
            if i < len(line) and line[i] == ',':
                new_line += '\t'
            elif i < len(line):
                new_line += line[i]
        i += 1
        
    return new_line

def ReadAndWrite():
    with open("./d01_ds.csv", 'r') as file:
        with open("ds.tsv", 'w+') as out:
            line = file.readline()
            while line:
                out.write(CorrectLine(line));
                line = file.readline()


if __name__ == '__main__':
    ReadAndWrite();
