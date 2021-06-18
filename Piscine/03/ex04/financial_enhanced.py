from bs4 import BeautifulSoup
import sys
import time
import cProfile
import pstats
import io
import httplib2


def my_func():
    result = []
    for i in range(10000):
        result.append(i)

    return result

def CheckArguments(av):
    if len(av) != 2:
        print("Not enough arguments")
        exit()

def GetPage(ticker):
    try:
        http = httplib2.Http()
        resp = http.request(f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}")
    except:
        print("Request fails")
        exit()
    return str(resp)

def FindRow(name, divs):
    for div in divs:
        if div.find(text=name) is not None:
            return div
    return None

def GetRowData(soup, row_name):
    divs = soup.find_all("div", {"data-test": "fin-row"})
    div = FindRow(row_name, divs)
    if div is None:
        raise ValueError()
    divs = div.find_all("div", {"data-test": "fin-col"})
    data = [row_name]
    for div in divs:
        data += [div.get_text()]
    return tuple(data)


def main(av):
    CheckArguments(av)
    soup = BeautifulSoup(GetPage(av[0].lower()), 'html.parser')
    try:
        print(GetRowData(soup, av[1]))
    except ValueError:
        print("Wrong row name")
        exit()
    except:
        print("Parse error")
        exit()

    


def CallProfil(av):
    pr = cProfile.Profile()
    pr.enable()
    main(av)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('profiling-http.txt', 'w+') as f:
        f.write(s.getvalue())

if __name__ == '__main__':
    CallProfil(sys.argv[1:])
    
    