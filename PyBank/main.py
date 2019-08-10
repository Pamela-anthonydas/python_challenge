import os
import csv

# Define file path
csvpath = os.path.join('Resources', 'budget_data.csv')
# Open the CSV using the set path csvpath
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    # Skip header row
    header = next(csvreader)
    # Initialize counters
    maxval=0
    minval=0
    rowcount=0
    total=0
    rev=0
    # Loop through the data
    for row in csvreader:
        # Find the total count of months
        rowcount=rowcount+1
        # Find the net total amount of "Profit/Losses" over the entire period
        total=total+(int(row[1]))
        # check if row[1]: profit/Losses is greater than maxval, and assign it to maxval variable , assign row[0] to maxDate variable
        if int(row[1]) > int(maxval):
            maxval=row[1]
            maxDate=row[0]
        # check if row[1]: profit/Losses is lesser than minval, and assign it to minval variable , assign row[0] to minDate variable
        elif int(minval) > int(row[1]):
            minval=row[1]
            minDate=row[0]
            
    # Calculte the average change
    average=total/rowcount
    # Print to terminal
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {rowcount}")
    print(f"Total: ${total}")
    print(f"Average change: ${round(average,2)}")
    print(f"Greatest Increase in Profits: {maxDate} (${maxval})")
    print(f"Greatest Increase in Profits: {minDate} (${minval})")

    # Print resuls to text file
output_path = os.path.join("output", "new.txt")

# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as csvfile:

    csvfile.write("Financial Analysis\n")
    csvfile.write("------------------------------ \n")
    csvfile.write(f"Total Months : {rowcount}\n")
    csvfile.write(f"Total: ${total}\n")
    csvfile.write(f"Average change: ${round(average,2)}\n")
    csvfile.write(f"Greatest Increase in Profits: {maxDate} (${maxval})\n")
    csvfile.write(f"Greatest Increase in Profits: {minDate} (${minval})\n")
    csvfile.write("------------------------------\n")
   