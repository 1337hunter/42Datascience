def data_types():
    one = type(42).__name__
    two = type('21 school').__name__
    three = type(42.21).__name__
    four = type(False).__name__
    five = type([]).__name__
    six = type({}).__name__
    seven = type(()).__name__
    eight = type(set()).__name__
    print("[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}]".format(
        one, two, three, four, five, six, seven, eight))

if __name__ == '__main__':
    data_types()
