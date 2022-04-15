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

    def total_sale(self):
        sales_total = 0.0
        for each_sale in range(len(self.sales)):
            sales_total = sales_total + float(self.sales[each_sale])
        return sales_total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        tot_sales = self.total_sale()
        fquota = float(quota)
        if tot_sales >= fquota:
            return True
        return False

    def compare_to(self, other):
        tot_sales = self.total_sale()
        other_tot = other.total_sale()
        if other_tot > tot_sales:
            return -1
        if other_tot < tot_sales:
            return 1
        return 0

    def __str__(self):
        tot_sales = self.total_sale()
        employee_id_chr = str(self.employee_id)
        str_out = employee_id_chr + '-' + self.name + ':' + str(tot_sales)
        return str_out

