class Student:
    def __init__(self, name, hours, q_points):
        self.name = name
        self.hours = float(hours)
        self.quality_points = q_points

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_quality_points(self):
        return self.quality_points()

    def set_name(self, name):
        self.name = name

    def get_gpa(self):
        return self.quality_points / self.hours
