#Encapsulation serves as a method to limit direct access to certain parts (Attributes, methods) of an object, preventing users from accessing state values for all variables within an object. It enables the concealment of both data members and associated methods within an instantiated class or object.

class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self._roll_no = roll_no #Protected Attrib (Don't work exactly as desired in Python. Can be accessed)
        self.__age = age  # Private attribute 
        
    def get_actualAge(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display_details(self):
        print(f"I'm {self.name} and my age is {self.__age}") #may be used as a func or normally as in print/return

s1 = Student("Tayyab", 23, 234567)
print(s1._Student__age)
s1.display_details()  # Display using public function
s1.set_age(41)  # Using setter method
print(s1.get_actualAge())  # Accessing updated age using getter method
s1.display_details()  # Display updated details


