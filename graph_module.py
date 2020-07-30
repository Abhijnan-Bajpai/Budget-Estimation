import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import numpy as np
from sklearn.linear_model import LinearRegression

root=Tk()
root.geometry("300x150")

e1=Label(root, text='Select reference year:')
e1.place(x=10, y=10)

years=Listbox(root, height=3, selectmode="SINGLE")
n=1
for i in range(2001,5000):
    years.insert(n,i)
    n+=1
years.place(x=10, y=50)

year=0
def selection():
    global year, years
    year=years.get(ACTIVE)
    print(year)
    
def cofo(*funcs):
    def cofn(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return cofn    
    
b=Button(root, text="Submit", padx=5, command=cofo(selection, root.destroy))
b.place(x=200, y=40)

root.mainloop()

###############################################################################################

if year<=2019:

    df = pd.read_csv('Data.csv')
    df = df[["Year", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    budget_list = list()

    num_year = year
    year_iterable = num_year % 2000 - 1

    for i in month_list:
        budget_list.append(df[i][year_iterable])

    plt.plot(month_list, budget_list, color='blue')
    plt.xlabel(f"Months of {num_year}")
    plt.ylabel(f"Expenditures in {num_year}")
    plt.title(f"Expenditure graph of the year {num_year}")
    plt.show()
    
##############################################################################################

else:
    data = pd.read_csv("Data.csv")  # load data set
    cols = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    data = data[data.columns[cols]]
    def est(n):

        ans=[]
        for x in  range(1,13):
            col1 = [0]
            dat1 = data[data.columns[col1]]
            col2 = [x]
            dat2 = data[data.columns[col2]]
            X = np.array(dat1).reshape(-1, 1)  # values converts it into a numpy array
            Y = np.array(dat2).reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            ans.append(int((linear_regressor.intercept_ )+ linear_regressor.coef_ * (n)))

        Mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        plt.scatter( Mon,ans)
        plt.plot( Mon,ans, color='red')
        plt.title(f'Budget for the year {n}')
        plt.xlabel('Months:->')
        plt.ylabel('Expenditure:->')
        plt.show()
    est(year)

