def Sort(d):
    sorted_values = list({k: int(v) for k, v in sorted(d.items(), key=lambda item: int(item[1]), reverse=True)}.values())
    sorted_dict = {}
    while sorted_values:
        keys_with_same_value = []
        value = sorted_values[0]
        for k in d.keys():
            if int(d[k]) == value:
                keys_with_same_value.append(k)
        keys_with_same_value.sort()
        for k in keys_with_same_value:
            sorted_values.pop(0)
            sorted_dict[k] = value
    return sorted_dict
        
def PrintKeyValue(d):
    for k, v in d.items():
        print(k, v)

def Print(d):
    for k in d.keys():
        print(k)
        

def main():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    d = dict(list_of_tuples)
    d = Sort(d)
    Print(d)
    #PrintKeyValue(d)


if __name__ == '__main__':
    main()