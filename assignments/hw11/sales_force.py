"""
Name: Angie Bui
sales_force.py
Problem: using object with a list qnd list of ojects
encapsulate data for a sales person.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import*


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file):
        the_file = open(file, "r")
        for line in the_file.readlines():
            split_file = line.split(",")
            everyone_id = split_file[0]
            everyone_id = int(everyone_id)
            name = split_file[1].strip()
            sales = split_file[2].strip().split(" ")
            employee = SalesPerson(everyone_id, name)
            for i in range(len(sales)):
                employee.enter_sale(float(sales[i]))
            self.sales_people += [employee]

    def quota_report(self, quota):
        qu_report = []
        for person in self.sales_people:
            info = []
            employee_id = person.get_id()
            employee_name = person.get_name()
            employee_total = person.total_sales()
            employee_quota = person.met_quota(quota)
            info.append(employee_id)
            info.append(employee_name)
            info.append(employee_total)
            info.append(employee_quota)
            qu_report.append(info)
        return qu_report

    def top_seller(self):
        top_list = []
        top_sales_amt = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales.sort()
            high = sales[-1]
            top_sales_amt.append(high)
            top_sales_amt.sort()
        if top_sales_amt[-1] != top_sales_amt[-2]:
            for i in self.sales_people:
                if top_sales_amt[-1] in i.get_sales():
                    top_list.append(i)
                    return top_list
        elif top_sales_amt[-1] == top_sales_amt[-2]:
            for i in self.sales_people:
                if top_sales_amt[-1] in i.get_sales():
                    top_list.append(i)
                if top_sales_amt[-2] in i.get_sales():
                    top_list.append(i)
                    return top_list

    def individual_sales(self, employee_id):
        for one_person in self.sales_people:
            if employee_id == one_person.get_id():
                return one_person

    def get_sale_frequencies(self):
        my_list = []
        for person in self.sales_people:
            sales = person.get_sales()
            my_list.append(sales)
        freq_dic = {}
        for sub in my_list:
            for item in sub:
                if item in freq_dic:
                    freq_dic[item] += 1
                else:
                    freq_dic[item] = 1
        return freq_dic
     
