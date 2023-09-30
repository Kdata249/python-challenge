import os
import csv

#vairables
net_total = 0
previous_number = 0


#lists to store data
months = []
profits_losses = []
changes = []
greatest_increase = {"date": "void",
    "value": 0}
greatest_decrease = {"date": "void",
    "value": 0}


budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    #save header separately
    budget_header = next(budget_data)

    #loop thru csv and add to lists
    for rows in budget_data:
        months.append(rows[0])
        profits_losses.append(int(rows[1]))

        #calculate changes
        changes.append(int(rows[1]) - previous_number)
        previous_number = int(rows[1])
        
        #calculate total
        net_total = net_total + int(rows[1])


    #Find greatest increase and decrease in profits
    for idx, num in enumerate(changes):
        if num > greatest_increase["value"]:
            greatest_increase["value"] = num
            greatest_increase["date"] = months[idx]
        if num < greatest_decrease["value"]:
            greatest_decrease["value"] = num
            greatest_decrease["date"] = months[idx]

    average_change = (profits_losses[-1] - profits_losses[0])/(len(profits_losses) - 1)
    
    print(len(months))
    print(net_total)
    print(average_change)
    print(changes[2])
    print(greatest_increase["date"])
    print(greatest_increase["value"])
    print(greatest_decrease["date"])
    print(greatest_decrease["value"])
    

