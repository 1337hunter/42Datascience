from bs4 import BeautifulSoup
import requests
import sys
import time
import cProfile
import pstats
import io
import pytest


def my_func():
    result = []
    for i in range(10000):
        result.append(i)

    return result

def GetPage(ticker):
    try:
        resp = requests.get(f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}")
        return resp.text
    except:
        raise ValueError()

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

def test_all():
    html_doc = """<html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <div data-test=fin-row><div>Total Revenue</div>1000</div>
        <div data-test=fin-row><div>Basic EPS</div>1000</div>
        <div data-test=fin-row><div>Diluted Average Shares</div>1000</div>
        <div data-test=fin-row><div>Total Expenses</div>1000</div>
        <p class="story">...</p>
        """
    soup = BeautifulSoup(html_doc, 'html.parser')
    divs = soup.find_all("div", {"data-test": "fin-row"})
    div = FindRow('Basic EPS', divs)
    assert div != None
    div = FindRow('Bla bla', divs)
    assert div == None
    soup = BeautifulSoup(GetPage("blablabla".lower()), 'html.parser')
    with pytest.raises(ValueError):
        GetRowData(soup, 'Basic EPS')
    soup = BeautifulSoup(GetPage("AMD".lower()), 'html.parser')
    GetRowData(soup, 'Basic EPS')
    assert type(GetRowData(soup, 'Basic EPS')) == type(tuple())

def CheckArguments(av):
    if len(av) == 1 and av[1] == 'test':
        exit()
    if len(av) != 2:
        print("Not enough arguments")
        exit()

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
    main(av)


if __name__ == '__main__':
    CallProfil(sys.argv[1:])
    
    