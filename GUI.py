from tkinter import *

root=Tk()
root.geometry("300x150")

e1=Label(root, text='Select reference year:')
e1.place(x=10, y=10)

years=Listbox(root, height=3, selectmode="SINGLE")
n=1
for i in range(2001,2501):
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
