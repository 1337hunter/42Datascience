class Must_read:
    with open("./data.csv", 'w+') as file:
        file.write('head,tail\n0,1\n1,0\n0,1\n1,0\n0,1\n0,1\n0,1\n1,0\n1,0\n0,1\n1,0\n')
    with open("./data.csv", "r") as file:
        line = file.readline().strip()
        while line:
            print(line)
            line = file.readline().strip()

def main():
    Must_read()

if __name__ == '__main__':
    main()