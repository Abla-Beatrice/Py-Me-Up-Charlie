import os
import csv

#create variables to be used in output
total_months = 0
total_revenue = 0
average_change =0
greatest_increase = ""
greatest_increase_value = 0
greatest_decrease = ""
greatest_decrease_value = 0

# open csv
budget_csv = 'Resources/budget_data.csv'

with open(budget_csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

# store the csv header
    header = next(reader)
 
    for row in reader:
        date = row[0]
        # if there is a date in the new row, add 1 to total_months
        if (date):
            total_months = total_months + 1

        profit_loss = int(row[1])

        # if there is an int in the new row, add it in to the total
        if (profit_loss):
            total_revenue = total_revenue + profit_loss

            # check if the current could contain the greatest increase/decrease
            if (profit_loss > greatest_increase_value):
                greatest_increase = date
                greatest_increase_value = profit_loss
            elif (profit_loss < greatest_decrease_value):
                greatest_decrease = date
                greatest_decrease = profit_loss

print('Financial Analysis')
print ('-------------------------')
print(f'Total Months: ' + str(total_months))
print(f'Total Revenue: ' + "$" + str(total_revenue))
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_decrease} (${greatest_decrease_value}')
print(f'Greatest Decrese in Profits: {greatest_decrease} (${greatest_decrease_value}')

output_file = 'output.txt'

with open(output_file, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('-------------------------\n')
    text.write(f'Total Months: {total_months}\n')
    text.write(f'Totat: ${total_revenue}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase in Profits: {greatest_decrease} (${greatest_decrease_value})\n')
    text.write(f'Greatest Decrease in Profits: {greatest_decrease} (${greatest_decrease_value})\n')

