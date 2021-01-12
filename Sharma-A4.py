# Name: Kusum Sharma
# ID: VW14892

# Q1

#if x is odd do x^3 else square x
q1 = [x**3 if x%2 == 1 else x**2 for x in range(1,21)]
print(q1)

# Q2

str_list = ['UMBC', 'UMD', 'UMB', 'TU']

q2 = filter(lambda x: len(x) > 3, str_list)

print(type(q2))
print(list(q2))

# Q3

class Vehicle: #VEHICLE CLASS WITH 3 ATTRIBUTES
    def __init__(self, make, model, year): ## Constructor method has a special name __init__
        #'' The self parameter is a reference to the current instance of the class,
        #and is used to access variables that belongs to the class.
        
       # It does not have to be named self , you can call it whatever you like,
       # but it has to be the first parameter of any function in the class. '''
        self.make = make
        self.model = model
        self.year = year

    def isNew(self): #method returns True if the year equals 2020; else returns False
        if self.year == 2020:
            return True
        else:
            return False

q3 = Vehicle('Honda', 'Accord', 2020)
print(type(q3))
print(q3.__dict__)
Vehicle.isNew(q3)

# Q4

class SUV(Vehicle): #SUV that inherits from Vehicle class w two new atrributes
    def __init__(self, transmission, milage, *args, **kwargs):
        self.transmission = transmission
        self.milage = milage
        super().__init__(*args, **kwargs)
        #The super() function is used to give access to methods and properties of a parent or sibling class.
        # returns an object that represents the parent class.

q4 = SUV('Automatic', 75000, 'Honda', 'CRV', 2019)
print(type(q4))
print(q4.__dict__)
SUV.isNew(q4)


# Q5

#- Create 2 CollegeStudent objects, one that return True, another that returns false.
#Call isStressed() to check if this is the case.

class CollegeStudent:
    def __init__(self, main_course, credit):
        self.main_course = main_course
        self.credit = credit

    def isStressed(self):
        if self.main_course == "CMSC331":
            if self.credit >= 16:
                return True

        else:
            return False
student1 = CollegeStudent("CMSC331", 16)
student2 = CollegeStudent("CMSC341", 17)

print(CollegeStudent.isStressed(student2))

class Vafaei(CollegeStudent):
    def __init__(self, noPartialCredit, *args, **kwargs):
        self.noPartialCredit = True
        super().__init__(*args, **kwargs)

student3 = Vafaei(True, "CMSC313", 16) #create obj
print(Vafaei.isStressed(student3)) #print obj

# Q7
import numpy as np

x = np.reshape([['a','b','c'], ['d','e','f'], ['g','h','i']],(3,3))

x

array= ([['a', 'b', 'c'],
       ['d', 'e', 'f'],
       ['g', 'h', 'i']])

answer = x[::-1,::-1]
print(answer)

# Q8
raw_scores = [{'student_name': 'John', 'raw_score': 8}, {'student_name': 'Mary', 'raw_score': 9}]  
final_grades = map(lambda x: x['raw_score']*10, raw_scores)

print(list(final_grades))



