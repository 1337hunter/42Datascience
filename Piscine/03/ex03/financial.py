from bs4 import BeautifulSoup
import requests
import sys
import time

def CheckArguments(av):
    if len(av) != 2:
        print("Not enough arguments")
        exit()

def GetPage(ticker):
    try:
        resp = requests.get(f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}")
    except:
        print("Request fails")
        exit()
    time.sleep(5)
    return resp.text

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

    




if __name__ == '__main__':
    main(sys.argv[1:])