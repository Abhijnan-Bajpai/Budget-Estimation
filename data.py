import pandas as pd
import random as ran


def generate_expense(year, lst):
    if year >= 2001:
        generate_expense(year - 1, lst)
        base_num = ran.randint(10000,15000)
        lst.append(base_num * (year % 2000))
        return lst
    else:
        return

n = int(input("Data from 2001 upto which year: "))

Jan = generate_expense(n, [])
Feb = generate_expense(n, [])
Mar = generate_expense(n, [])
Apr = generate_expense(n, [])
May = generate_expense(n, [])
Jun = generate_expense(n, [])
Jul = generate_expense(n, [])
Aug = generate_expense(n, [])
Sep = generate_expense(n, [])
Oct = generate_expense(n, [])
Nov = generate_expense(n, [])
Dec = generate_expense(n, [])

csv_dict = {
    "Year": [i for i in range(2001,n+1)], "Jan": Jan, "Feb": Feb, "Mar": Mar, "Apr": Apr, "May": May, "Jun": Jun, "Jul": Jul, "Aug": Aug,
    "Sep": Sep, "Oct": Oct, "Nov": Nov, "Dec": Dec}

dfObj = pd.DataFrame(csv_dict)
print(dfObj)

