import os
import numpy as np
import PyBank 

#get file names to process
file_names = ['budget_data_1.csv','budget_data_2.csv']

# defining result structure
result = {  "File Name":"",
            "Total Months":0,                
            "Total Revenue":0,
            "Average Revenue Change":0,    
            "Greatest Increase in Revenue":0, 
            "Greatest Decrease in Revenue":0 
            }

#for each given file, do the same steps
for value in file_names:

    result["File Name"] = value

    #read values into list, calculate total months and revenue
    filepath = os.path.join('raw_data',value).replace("\\","/")
    
    revenues = PyBank.read_csv_to_list(filepath)
    result["Total Months"] = len(revenues)
    result["Total Revenue"] = PyBank.calculate_total_revenue(revenues)

    #calculate change in revenues, find avg, min and max
    avg_revenues = PyBank.get_moving_avg_list(revenues)
    result["Average Revenue Change"] = np.mean(avg_revenues)
    result["Greatest Increase in Revenue"] = np.max(avg_revenues)
    result["Greatest Decrease in Revenue"] = np.min(avg_revenues)

    #print results
    PyBank.display_result(result)
    
    n = len(value) - 4
    output_filename = f"{value[:n]}_new_format.csv"

    output_path = os.path.join('output',output_filename).replace("\\","/")

    PyBank.export_to_csv(output_path,result)