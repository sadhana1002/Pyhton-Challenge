import os
import csv
import dateutil.parser as parser
import datetime
import numpy as np

filepath = os.path.join('raw_data','budget_data_1.csv').replace("\\","/")
print(filepath)

revenues = []
moving_average =[]

with open(filepath, encoding ="utf-8-sig",mode = 'r', newline="") as csvfile:
    csvreader = csv.DictReader(csvfile,delimiter=",")
    for row in csvreader:
       revenues.append((row['Date'],float(row['Revenue'])))

total_revenue = 0

for item in revenues:
    total_revenue = total_revenue + item[1]


for i in range(len(revenues)-1):
    current_avg = (revenues[i][1]+revenues[i+1][1])/2
    moving_average.append(current_avg)

print(f"Total Months:                    {len(revenues)}")
print(f"Total Revenue:                   {total_revenue}")
print(f"Average Revenue Change:          {np.mean(moving_average)}")
print(f"Greatest Increase in Revenue:    {np.max(moving_average)}")
print(f"Greatest Decrease in Revenue:    {np.min(moving_average)}")
