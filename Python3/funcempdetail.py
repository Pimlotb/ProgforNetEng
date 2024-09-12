
def employeeDetail(emp_no,emp_name):
    return{'Employee Number':emp_no , 'Employee Name':emp_name}

emp_no = input('Enter your employee number:')
emp_name = input ('Enter your employee name:')

empdetails = employeeDetail(emp_no,emp_name)

print (empdetails)
