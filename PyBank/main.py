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
    
    
output_path = os.path.join("c:\\Users\\kklos\\OneDrive\\Desktop\\python-challenge\\py_analyses", "pybank_analyses.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {len(months)}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${round(average_change, 2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['value']})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['value']})"])


    

