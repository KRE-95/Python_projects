import matplotlib.pyplot as plt

#mathlibary:
print("========== interest calculator ======")
# for every information from user:
# value
interest = float(input("What is the interest?: "))
# years
years = int(input("How many years?: "))
# how much money start wiht in bank
money = float(input("How much money to start with?: "))

# matlib import (after)
list_years = list(range(0, years))
print(list_years)
# how much money pr. year:
money_pr_year = []

# once a  year
print(f"Money at the begining of the first year: {money}")
for year in range(years):
    money += money * interest  # formula for the interest with money from bank
    money_pr_year.append(money)  # matlib import
    print(f"Money at the end of the year {year + 1} : {round(money, 4)}")

plt.plot(list_years, money_pr_year)
    #show
plt.show()