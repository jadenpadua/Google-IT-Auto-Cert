#/!usr/bin/env python3
import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []

    for row in employee_file:
        employee_list.append(row)
    
    return employee_list


def process_data(employee_list):
    department_list = []

    for employee in employee_list:
        department_list.append(employee['Department'])
    
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for key in sorted(dictionary):
            f.write(str(key) + ':' + str(dictionary[k]) + '\n')
        f.close()

employee_list = read_employees('/home/student-12adda23/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary,'/home/student-12adda23/data/test_report.txt' )
