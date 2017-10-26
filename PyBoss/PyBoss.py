import csv
from datetime import datetime
import us_state_abbrev

#read given csv and write into list
def read_csv_to_list(filepath):
    employees = []
    with open(filepath, encoding ="utf-8-sig",mode = 'r', newline="") as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=",")
        for row in csvreader:
            employees.append({"Emp ID":row["Emp ID"],
                             "Name":row["Name"],
                             "DOB":row["DOB"],
                             "SSN":row["SSN"],
                             "State":row["State"]})
           # print(employees)
        
    return employees

def convert(oldDict):
    newDict = []
    
    for items in oldDict:
        
        first_name,last_name = items["Name"].split(" ",2)
        
        dob = datetime.strptime(items["DOB"], '%Y-%m-%d')
        formatted_dob = str(datetime.strptime(items["DOB"], '%Y-%m-%d').date())
        
        formatted_ssn = items["SSN"].replace(items["SSN"][:7],"***-**-")
       
        formatted_state = us_state_abbrev.us_state_abbrev[items["State"]]
        
        newDict.append({"Emp ID":items["Emp ID"],
                                    "first name":first_name,
                                    "last name":last_name,
                                    "DOB":formatted_dob,
                                    "SSN":formatted_ssn,
                                    "State":formatted_state
                                    })
    return newDict

def export_to_csv(filename,dataset):
    with open(filename, 'w',encoding='utf-8') as output_file:
        keys = ['Emp ID','first name','last name','DOB','SSN','State']
        writer = csv.DictWriter(output_file,lineterminator='\n',  fieldnames=keys)
        writer.writeheader()
        
        for records in dataset:
            writer.writerow(records)


