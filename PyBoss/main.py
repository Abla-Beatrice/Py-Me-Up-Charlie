import os
import csv
import datetime

employee_csv = os.path.join('employee_data.csv')

us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

empID = 0
name = ""
dob = 0
ssn = 0
state = ""
employee_dict = {
    "Emp ID": [],
    "First Name": [], 
    "Last Name": [],
    "DOB": [],
    "SSN": [],
    "State": [],
}

with open('Resources/employee_data.csv') as csvfile:

    reader = csv.reader(csvfile)

    header = next(reader)

    for row in reader:
        EmpID = row[0]
        employee_dict["Emp ID"].append(EmpID)

        First = row[1].split()[0]
        Last = row[1].split()[1]
        employee_dict["First Name"].append(First)
        employee_dict["Last Name"].append(Last)

        formatted_dob = datetime.datetime.strptime(row[2],"%Y-%m-%d")
        formatted_dob = formatted_dob.strftime("%m/%d/%Y")
        employee_dict["DOB"].append(formatted_dob)

        split_ssn = list(row[3])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)
        employee_dict["SSN"].append(joined_ssn)


        state_abbrev = us_state_abbrev[row[4]]
        employee_dict["State"].append(state_abbrev)


with open('new_employee.csv', 'w') as csvfile:
    employee_csv_data = csv.DictWriter(csvfile, fieldnames =list(employee_dict.keys()))
    employee_csv_data.writeheader()
    value = list(zip(employee_dict["Emp ID"], employee_dict["First Name"],employee_dict["Last Name"],
            employee_dict["DOB"], employee_dict["SSN"], employee_dict["State"]))
   
    employee_csv_data.writerows([dict(zip(list(employee_dict.keys()), [e,f,l,d,s,st])) for e,f,l,d,s,st in value])