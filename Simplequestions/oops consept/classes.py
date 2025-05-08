# what is class ------> classes is collection of atributes, methods and objects
# __init__, ---> this are special types of methods and also known as constructors
# __dict__, ----> is a special attribute that stores all the writable attributes of an object in the form of a dictionary.
# self ---> self is veriable to contain current memory reference of current object 
# object ---> e1 = Employee("shahid", 20000)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


#  "display" function passing as a arggumrnt
    def display(self):
        print(f"emp name is {self.name} and salary is {self.salary}")


e1 = Employee("shahid", 20000)  # ======> objects 
e2 = Employee("shaaad", 50000)

print(e1.__dict__)  # ========> access all details in the form of dictionary
print(e1.name)

e1.salary = 51000000  # ---> update intial values
# access display method
e1.display()


print("==============================class function=======================================")

# build in class function
# 1. getattr---> get attribute .... syntax ==> getattr(object_name, attribute)
print(getattr(e1, 'name')) #shahid

# 2. setattr---> set attribute .... syntax ==> setattr(object_name, attribute_name, updating_value)
setattr(e1, 'salary', 100) 
print(e1.__dict__)   #  {'name': 'shahid', 'salary': 100}

# 3. detattr---> del attribute .... syntax ==> detattr(object_name, attribute)
delattr(e1, 'salary')
print(e1.__dict__) #{'name': 'shahid'}  =====> salary attribute is deleted

# 4. hasattr---> has attribute .... syntax ==> hasattr(object_name, attribute)
print(hasattr(e1, "salary"))  # written value in the form of boolean.... output====> False

print("==============================class attribute=======================================")




class Student:
    "This class represents an student."  #---------->  fro __doc__
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# build in class attribute
# 1.__doc__
print(Student.__doc__)

# 2.__dict__
print(Student.__dict__)  #details of class in the form of dictionary

# 3. __name__
print(Student.__name__)  #Student  ---> name of class

# 4.__module__
print(Student.__module__)   #__main__   return current module name 

# 5. __basses__
print(Student.__bases__)  

print("===============================isinstance=====================================")

# isinstance(object_name, class_name)  -----> this function is use for object is present in the class or not 
print(isinstance(e1, Employee)) #True   
print(isinstance(e1, Student))  #False  
