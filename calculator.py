import sys
import os
import locale


def calculator(portfolio, income, appreciation, years):
    anual_income = income * 12
    invested = portfolio

    for _ in range(years):
        portfolio += anual_income
        invested += anual_income
        portfolio = portfolio + portfolio * appreciation

    portfolio = int(portfolio)
    profit = portfolio - invested

    portfolio = locale.currency(portfolio, grouping=True)
    invested = locale.currency(invested, grouping=True)
    profit = locale.currency(profit, grouping=True)
    
    print('After {} years, the value of the portfolio is {}.'.format(years, portfolio))
    print('Invested {} and the profit is {}'.format(invested, profit))


def main():
    if len(sys.argv) != 5:
        print('Syntax: {} {{initial_value}} {{monthly income}} {{year appreciation}} {{years}}'.format(
            os.path.basename(__file__)
        ))
        return

    try:
        initial = int(sys.argv[1])
        income = int(sys.argv[2])
        appreciation = float(sys.argv[3])
        years = int(sys.argv[4])

    except ValueError:
        print('Only numbers allowed')
        return

    locale.setlocale(locale.LC_ALL, '')
    calculator(initial, income, appreciation, years)


main()