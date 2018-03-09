
import csv
import pandas as pd

#create variable to store combined values
dic = {"Date": [], "Revenue": []}
print(dic)
#open documents and append to dictionary dic
csv_path1 = "budget_data_1.csv"
csv_path2 = "budget_data_2.csv"

with open(csv_path1, newline='') as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter=',')
    next(csvreader1, None)
    for row in csvreader1: 
        dic["Date"].append(row[0])
        dic["Revenue"].append(row[1])
with open(csv_path2, newline='') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    next(csvreader2, None)
    for rows in csvreader2:
        dic["Date"].append(rows[0])
        dic["Revenue"].append(rows[1])

    
df_dic = pd.DataFrame(dic)
clean_dic = df_dic.drop_duplicates(["Date"], keep=False)

Months = clean_dic["Date"].index[-1] + 1

num_dic = pd.to_numeric(clean_dic["Revenue"])
x = pd.DataFrame(num_dic)
Total_Revenue = x["Revenue"].sum()
Total_Change = ((x["Revenue"][0])- (x["Revenue"][126]))
print(Total_Change)
max = x["Revenue"].max()
min = x["Revenue"].min()

#Finalize Outputs for report
Output1 = "Total Months: " + str(Months)
Output2 = "Total Revenue: " + str(Total_Revenue)
Output3 = "Average Revenue Change: " + str(Total_Change/Months)
Output4 = "Greatest Increase in Revenue: $" + str(max)
Output5 = "Greatest Decrease in Revenue: $" + str(min)

#Write outfile
Output = "financial_analysis_output.csv"
with open(Output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow([Output1])
    writer.writerow([Output2])
    writer.writerow([Output3])
    writer.writerow([Output4])
    writer.writerow([Output5])