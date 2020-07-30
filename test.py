personal_details = dict()
personal_details["Salary"]=[]
personal_details["Saving goal and time in years"]=[]
personal_details["Various monthly expnditures and their priorities"]=[]

personal_details["Salary"].append(input("Please enter your salary:\n>>"))
personal_details["Saving goal and time in years"].append(float(i) for i in input("Please enter your savings goal and time required to achieve it:\nPlease enter comma-space separated values\n>>").split(", "))
print(personal_details) 
print("Please enter your various monthly expenditure amounts and their priorities.")

while(True):
    print("Type 'end' to stop providing input.")
    user_input = [int(i) for i in input("Please enter comma-space separated values:\n>>").split(", ")]
    if user_input == "end":
        break
    else:
        personal_details["Various monthly expnditures and their priorities"].append(user_input)

print(personal_details)    