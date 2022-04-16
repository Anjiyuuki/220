"""
Name: Angie Bui
sales_person.py
Problem: Creates a sales person class with different
functions to be used in Sale Force.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        add = 0
        for sale in self.sales:
            add += sale
        return add

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() == quota or self.total_sales() > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        tot_sales = self.total_sales()
        other_tot = other.total_sales()
        if other_tot > tot_sales:
            return -1
        if other_tot < tot_sales:
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
 

