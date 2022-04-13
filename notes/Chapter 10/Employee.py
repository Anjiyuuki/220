class Employee:
    # name, salary, bday, id
    #constructor
        #instance variable
    def __init__(self, id, name):
        '''
        blah blah blah, Doc string... so like Help(Circle) it will let you know
        '''
        self.id = int(id)
        self.name = name
        self.salary = 0
        self.birthday = ''

    #methods
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.__parse_birthday(birthday)

    # Encapsulation
    # Interface
    def __parse_birthday(self, birthday):
        # 1/1/2001
        # Jan 1, 2001
        if birthday.find('/') < 0:
            self.birthday = birthday
        else:
            month, day, year = birthday.split('/')
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            month_string = months[int(month)-1]
            self.birthday = '{0} {1},{2}'.format(month_string, day, year)
        self.birthday = birthday

