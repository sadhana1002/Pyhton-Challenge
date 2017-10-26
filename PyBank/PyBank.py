import csv

#read given csv and write into list
def read_csv_to_list(filepath):
    revenues = []
    with open(filepath, encoding ="utf-8-sig",mode = 'r', newline="") as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=",")
        for row in csvreader:
            revenues.append((row['Date'],float(row['Revenue'])))
    return revenues

#calculate average change between records and store in list
def get_moving_avg_list(mainlist):
    moving_average =[]
    
    for i in range(len(mainlist)-1):
        current_avg = (mainlist[i][1]+mainlist[i+1][1])/2
        moving_average.append(current_avg)
    return moving_average
    
#calculate total revenue
def calculate_total_revenue(revenue_data):
    total_revenue = 0

    for item in revenue_data:
        total_revenue = total_revenue + item[1]
    
    return total_revenue

#print results
def display_result(resultDict):
    for item in resultDict:
        print(f"{item}\t:{resultDict[item]}")
    print("\n")

def export_to_csv(filename,dataset):
    with open(filename, 'w',encoding='utf-8') as output_file:
        keys = dataset.keys()
        writer = csv.DictWriter(output_file,lineterminator='\n',  fieldnames=keys)
        writer.writeheader()
        writer.writerow(dataset)
