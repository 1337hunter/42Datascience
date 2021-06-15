import sys

def EncodeShift(ch, shift):
    ret = ord(ch)
    if ord(ch) >= 65 and ord(ch) <= 90:
        while shift:
            ret += 1
            shift -= 1
            if ret > 90:
                ret = 65
    elif ord(ch) >= 97 and ord(ch) <= 122:
        while shift:
            ret += 1
            shift -= 1
            if ret > 122:
                ret = 97
    return chr(ret)

def DecodeShift(ch, shift):
    ret = ord(ch)
    if ord(ch) >= 65 and ord(ch) <= 90:
        while shift:
            ret -= 1
            shift -= 1
            if ret < 65:
                ret = 90
    elif ord(ch) >= 97 and ord(ch) <= 122:
        while shift:
            ret -= 1
            shift -= 1
            if ret < 97:
                ret = 122
    return chr(ret)

def EncodeString(str, shift):
    code = ""
    for ch in str:
        code += EncodeShift(ch, shift)
    return code


def DecodeString(str, shift):
    code = ""
    for ch in str:
        code += DecodeShift(ch, shift)
    return code

methods = {}
methods["encode"] = EncodeString
methods["decode"] = DecodeString

def main(argv):
    if len(argv) != 3:
        return
    code = methods[argv[0]](argv[1], int(argv[2]))
    print(code)
    
if __name__ == '__main__':
    main(sys.argv[1:])