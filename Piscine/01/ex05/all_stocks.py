import sys

companies = {
    'Apple' : 'AAPL',
    'Microsoft' : 'MSFT',
    'Netflix' : 'NFLX',
    'Tesla' : 'TSLA',
    'Nokia' : 'NOK'
}
stocks = {
    'AAPL' : 287.73,
    'MSFT' : 173.79,
    'NFLX' : 416.90,
    'TSLA' : 724.88,
    'NOK' : 3.37
}

def GetCompanyNameByTicker(ticker):
    for key, value in companies.items():
        if value == ticker:
            return key

def IdentifyCompanyAndTicker(names, tickers, clist):
    i = 0
    while i < len(tickers):
        if names[i] in companies:
            print(f"{names[i]} stock price is {stocks[companies[names[i]]]}")
        elif tickers[i] in stocks:
            print(f"{tickers[i]} is a ticker symbol for {GetCompanyNameByTicker(tickers[i])}")
        else:
            print(f"{clist[i]} is an unknown company or an unknown ticker symbol")
        i += 1
def main(argv):
    if len(argv) != 1:
        return
    names = []
    tickers = []
    original = []
    clist = [x.strip() for x in argv[0].lower().split(',')]
    for comp in clist:
        if len(comp) == 0:
            return
        else:
            names += [str(comp[0]).upper() + comp[1:]]
            tickers += [comp.upper()]
    IdentifyCompanyAndTicker(names, tickers, clist)



if __name__ == '__main__':
    main(sys.argv[1:])
