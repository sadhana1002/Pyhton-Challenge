import os
import PyBoss 

#get file names to process
file_names = ['employee_data1.csv','employee_data2.csv']

for index,value in enumerate(file_names):
    #read values into list, calculate total months and revenue
    filepath = os.path.join('raw_data',value).replace("\\","/")
    
    employees = PyBoss.read_csv_to_list(filepath)

    formatted_employees = PyBoss.convert(employees)

    n = len(value) - 4
    output_filename = f"{value[:n]}_new_format.csv"

    output_path = os.path.join('output',output_filename).replace("\\","/")

    PyBoss.export_to_csv(output_path,formatted_employees)


   