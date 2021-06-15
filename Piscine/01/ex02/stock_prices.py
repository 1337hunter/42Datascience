import sys

def PrintStocks(company):
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
    if company in companies:
        print(stocks[companies[company]])
    else:
        print("Unknown company")


def main(argv):
    if (len(argv) != 1):
        return
    company = str(argv[0][0]).upper()
    company += argv[0][1:].lower()

    PrintStocks(company)



if __name__ == "__main__":
    main(sys.argv[1:])
