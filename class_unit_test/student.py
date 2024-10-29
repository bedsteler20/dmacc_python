
class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        if not issubclass(lname, str) or lname == "" or lname == None:
            raise ValueError("Last name cannot be empty")
        if issubclass(fname, str) or fname == "" or fname == None:
            raise ValueError("First name cannot be empty")
        if not issubclass(major, str) or major == "" or major == None:
            raise ValueError("Major cannot be empty")
        if not isinstance(gpa, float) or gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return (
            self.last_name
            + ", "
            + self.first_name
            + " has major "
            + self.major
            + "with gpa: "
            + str(self.gpa)
        )