from Employee import*
from Organization import*
def print_employee(e):
    print(e.get_name(), e.get_id(), e.get_salary(), )

def main():
    o = Organization('College of Charleston')
    e = Employee(1, 'Bob')
    o.add_employee(e)
    emp_1 = o.get_employee(e)
    print(emp_1)

main()