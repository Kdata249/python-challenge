import os
import csv

#vairables
net_total = 0


#lists to store data
months = []
profits_losses = []
changes = []
greatest_increase = {}
greatest_decrease = {}


budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    #save header separately
    budget_header = next(budget_data)

    #loop thru csv and add to lists
    for rows in budget_data:
        months.append(rows[0])
        profits_losses.append(int(rows[1]))

        #calculate total
        net_total = net_total + int(rows[1])

    #Find greatest increase and decrease in profits
    for num in profits_losses
        if num

    average_change = (profits_losses[-1] - profits_losses[0])/(len(profits_losses) - 1)
    
    print(len(months))
    print(net_total)
    print(average_change)
    
    

