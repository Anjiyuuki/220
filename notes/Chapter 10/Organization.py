class Organization:
    # name, organization
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_name(self):
        return self.name

    def add_employee(self,employee):
        self.employees.append(employee)

    def get_employee(self, employee_id):
        for employee in self.employees:
            if employee.get_id() == employee_id:
                return employee

    def get_payroll(self):
        acc = 0
        for employee in self.employees:
            acc = acc + employee.get_salary()
        return acc
