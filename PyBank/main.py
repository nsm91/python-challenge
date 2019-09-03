#Import Dependencies
import os
import csv
#Call in File
py_bank_path = os.path.join("../budget_data.csv")
#Open File
with open(py_bank_path,newline='') as pybank_csv:
    py_bank = csv.reader(pybank_csv,delimiter=',')
    py_bank_header = next(py_bank)
    #print(py_bank_header)
    month_counter = 0
    total_PL = 0
    avg_change = []
    last_row = 0
    max_profit1 = 0
    max_loss1 = 0

    for row in py_bank:
        #part 1
        month_counter += 1
        #part 2
        total_PL += int(row[1])
        #part 3
        change = (int(row[1]) - last_row)
        avg_change.append(change)
        last_row = int(row[1])
        #part 4
        if change > max_profit1:
            max_profit1 = change
            max_profit2 = [row[0],change]
        if change < max_loss1:
            max_loss1 = change
            max_loss2 = [row[0],change] 

    sum1 = 0
    #get rid of the first entry because its empty / erroneous
    del avg_change[0]
    for i in avg_change:
        sum1 += float(i)
    sum1 = sum1 / len(avg_change)

    print(f"Number of Months: {month_counter}")
    print(f"Total Profit: ${total_PL}")
    print(f"Average Change: {round(sum1,2)}")
    print(f"Max Profit: {max_profit2[0]} : {max_profit2[1]}")
    print(f"Max Loss: {max_loss2[0]} : {max_loss2[1]}")

    pybank_txt = open("PyBank_Summary.txt","w")
    pybank_txt.write(f"Number of Months: {month_counter}")
    pybank_txt.write(f"\nTotal Profit: ${total_PL}")
    pybank_txt.write(f"\nAverage Change: {round(sum1,2)}")
    pybank_txt.write(f"\nMax Profit: {max_profit2[0]} : {max_profit2[1]}")
    pybank_txt.write(f"\nMax Loss: {max_loss2[0]} : {max_loss2[1]}")