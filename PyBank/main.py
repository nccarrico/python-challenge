# open file at csvpath
import csv
csvpath = 'budget_data.csv'

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    num_rows = 0
    net_total = 0
    dates = []
    values = []
    
    #iterate through rows and make new lists, dates and values, and calculate total months and net profit 
    for row in csvreader:
        dates.append(row[0])
        values.append(row[1])
        num_rows += 1
        net_total += int(row[1])

#iterate through values list and make new list called changes, then calculate average change 
changes = []
total_changes = 0

for i in range(num_rows - 1):
    change = int(values[i + 1]) - int(values[i])
    changes.append(change)

for e in changes:
    total_changes += int(e)
    
avg_change = total_changes / len(changes)

#function to find index of max change
def find_max_i(l):
    max_index = 0
    for i in range(len(l)):
        if l[max_index] == max(l):
            return max_index
        else:
            max_index += 1
#function to find index of min change            
def find_min_i(l):
    min_index = 0
    for i in range(len(l)):
        if l[min_index] == min(l):
            return min_index
        else:
            min_index += 1

greatest_inc_date = dates[find_max_i(changes) + 1]
greatest_dec_date = dates[find_min_i(changes) + 1]
greatest_inc_value = max(changes)
greatest_dec_value = min(changes)

#print results in console
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(num_rows))
print("Total: $" + str(net_total))
print("Average Change: $" + str(avg_change))
print(f"Greatest Increase in Profits: $ {greatest_inc_date} ($ {greatest_inc_value})")
print(f"Greatest Decrease in Profits: $ {greatest_dec_date} ($ {greatest_dec_value})")

#output results as a csv file
output_path = "Financial_Analysis.csv"

with open(output_path, 'w', newline='') as output:
    csvwriter = csv.writer(output)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow(["Total Months: " + str(num_rows)])
    csvwriter.writerow(["Total: $" + str(net_total)])
    csvwriter.writerow(["Average Change: $" + str(avg_change)])
    csvwriter.writerow([f"Greatest Increase in Profits: $ {greatest_inc_date} ($ {greatest_inc_value})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: $ {greatest_dec_date} ($ {greatest_dec_value})"])
