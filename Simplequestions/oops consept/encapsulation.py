# Encapsulation is used for privacy and protection — to hide important data from being directly accessed or modified by the outside world.

# __variable_name ===>   "__" double underscore is also known as privacy member  ------------> name-mangled to prevent direct access from outside the class.
# _variable_name ===>   "_" single  underscore is also known as protection member  ------->meant to be accessed only within the class and its subclasses.

class Student:
    def __init__(self, name, marks):
        self.name = name            # public
        self._marks = marks         # protected
        self.__password = "1234"    # private

    def display(self):
        print(f"Name: {self.name}, Marks: {self._marks}")

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

s = Student("shahid", 90)
print(s.__dict__)

# # specific property access 
# print(s.__password)  -------> this is impossible to access like that 
# print(s._marks)-------> this is also impossible to access like that 

print("==================specific property access ================")
print(s.get_password())    #add get in front of veriable
print(s._marks)


print("=====================privecy function============")

class Student:
    def __init__(self, name, marks):
        self.name = name            # public
        self._marks = marks         # protected
        self.__password = "1234"    # private

    def display(self):
        print(f"Name: {self.name}, Marks: {self._marks}")

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def __private_function(self):   #======> but this is not usable 
        pass

s1= Student("shahid", "80")
s1.get_password()
print(s1.__dict__)
s1.set_password("sss")
print(s1.get_password())