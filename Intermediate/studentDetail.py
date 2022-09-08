class Student_Details:
    def __init__(self):
        self.name = input("Enter your names:")
        self.registrationNo = input("Enter your Registration number:") 
        self.yearOfBirth = int(input("Enter Year of Birth:"))
class Temp(Student_Details):
    def display(self):
        print("==============Student Details are ===========")
        print("Name:", self.name)
        print("Registration number:", self.registrationNo)
        print("Year of Birth",self.yearOfBirth)
        
        
obj1 = Temp()
obj1.display()