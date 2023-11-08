# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')
#PyBank/Resources/budget_data.csv

#Initializing required lists
profit=[]
monthly_changes=[]
date=[]


#Initializing required variables
count=0
total_profit=0
total_change_profits=0
initial_profit=0

#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    
    for row in csvreader:
        # Use to count the number of months in this dataset
         count=count+1
         
         # We will use this when collecting the greatest increase and decrease in profits
         date.append(row[0])
         
         # Append the profit information and calculate the total profit
         profit.append(row[1])
         total_profit=total_profit+int(row[1])
         
         #Calculating the average change in profits from month to month. Then calculate the aveage
         final_profit=int(row[1])
         monthly_change_profits=final_profit - initial_profit
         
         # store these monthly changes in list
         monthly_changes.append(monthly_change_profits)
         
         total_change_profits=total_change_profits + monthly_change_profits
         initial_profit=final_profit
         
         #Calculate the average change in the profits
         average_change_profits=(total_change_profits/count)
         
         #Find the max and min change in profitsand the corresponding dates these changes were observed
         greatest_increase_profit=max(monthly_changes)
         greatest_decrease_profit=min(monthly_changes)
         
         increase_date=date[monthly_changes.index(greatest_increase_profit)]
         decrease_date=date[monthly_changes.index(greatest_decrease_profit)]  
         
         print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {str(count)}")
    print(f"Total Profits: ${str(total_profit)}")
    print(f"Average Change: ${str(int(average_change_profits))}")
    print(f"Greatest Increase in Profits: {str(increase_date)} ${str(greatest_increase_profit)} ")
    print(f"Greatest Decrease in Profits: {str(decrease_date)} ${str(greatest_decrease_profit)}")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"    Total Months: {str(count)}  \n")
    text.write(f"    Total Profits: ${str(total_profit)} \n")
    text.write(f"    Average Change: ${str(int(average_change_profits))} \n")
    text.write(f"    Greatest Increase in Profits: {str(increase_date)}    (${str(greatest_increase_profit)}) \n")
    text.write(f"    Greatest Decrease in Profits: {str(decrease_date) }   (${str(greatest_decrease_profit)})\n")
    text.write("----------------------------------------------------------\n")
       
