import sys

#it work only becouse company -> ticker pair is unique
def PrintCompanyAndPrice(ticker):
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
    company = ""
    for key, val in companies.items():
        if (val == ticker):
            company = key
    if company != "":
        print(f"{company} {stocks[ticker]}")
    else:
        print("Unknown ticker")

def main(argv):
    if (len(argv) != 1):
        return
    ticker = argv[0].upper()
    PrintCompanyAndPrice(ticker)

if __name__ == '__main__':
    main(sys.argv[1:]);
