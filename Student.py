class Student:

    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if(self.gpa>=3.5):
            return True
        else:
            return False

#In python self is reference to current instance of class

#In Python, the __init__ method is important and cannot be named anything else if you want to define a constructor for your class. This method is a special method (also called a "dunder method" because of the double underscores) and is used to initialize new objects of the class.
         
