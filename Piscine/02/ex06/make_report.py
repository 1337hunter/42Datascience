from analytics import *
from config import report_template


def main(av):
    CheckArguments(av)
    class_inst = Research(av[0])
    analytics = Analitics([])
    data = analytics.predict_random()
    analytics.data = data
    calculations = class_inst.Calculations(data)
    heads, tails = calculations.counts()
    headf, tailf = calculations.fractions()
    report = report_template(heads, tails, headf, tailf)
    analytics.save_file(report, av[0], 'txt')

if __name__ == '__main__':
    main(sys.argv[1:])