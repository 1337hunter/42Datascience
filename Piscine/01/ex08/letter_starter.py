import sys

def TrySendEmail(email, name, cmail):
    if cmail == email:
        print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
        return True
    else:
        return False


def WriteLetter(email):
    with open("./employees.tsv", 'r') as emploeers:
        line = emploeers.readline().strip()
        while line:
            splited = line.split('\t')
            if TrySendEmail(email, splited[0], splited[2]):
                return 
            line = emploeers.readline().strip()

def main(argv):
    if (len(argv) != 1):
        return
    WriteLetter(argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])