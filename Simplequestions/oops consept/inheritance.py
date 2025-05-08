# what inheritance ===> deriving a new class from a existing class so new class inherits all members of existing class 
# child class can access parent attributes and methodbut parent class can not access child class

print("============singalinheritance===============")
class Parent:
    name = "abc"
    def display(self):
        print("parent")
        
e1 = Parent()
e1.display()

class Child(Parent):
    name1 = "xyz"
    def show(self):
        print("hey i am child")

c1 = Child()

c1.show()
c1.display()  #accessing parent function




print("===================constructor over-riding=====================")
#constructor in inheritance

class Parent1:
    def __init__(self):
        print("parent constructor called")
        self.vehicle = "car"

class Child1(Parent1):
    pass
# note: ====> when child dont have any cunstructor to automatically get their parent cunstructor

p = Child1()
print(p.__dict__) #{'vehicle': 'car'}

# but child have their own cunstructor to get more orivacy to self  ==> this is called  constructor over-riding

class Parent1:
    def __init__(self):
        print("parent constructor called")
        self.vehicle = "car"

class Child1(Parent1):
    def __init__(self):
        print("parent constructor called")
        self.vehicle = "BIKE"
p = Child1()
print(p.__dict__) #{'vehicle': 'BIKE'}



# accesss all parent properties from child with super function
print("=================================super()==================================")


class Parent2:
    def __init__(self):
        print("parent constructor called")
        self.vehicle1 = "car"

class Child2(Parent2):
    def __init__(self):
        super().__init__()
        print("child constructor called")
        self.vehicle = "BIKE"

p = Child2()
print(p.__dict__) 

print("===================================================")

class Parent3:
    def __init__(self, vehicle1):
        print("parent constructor called")
        self.vehicle1 = vehicle1

class Child3(Parent3):
    def __init__(self,  vehicle1, vehicle):
        super().__init__(vehicle1)
        print("child constructor called")
        self.vehicle = vehicle
        
p = Child3("bike", "car")
print(p.__dict__) 


print("============multilevel-linheritance===============")

class Parent3:
    def __init__(self, vehicle1):
        print("parent constructor called")
        self.vehicle1 = vehicle1

class Child3(Parent3):
    def __init__(self,  vehicle1, vehicle):
        super().__init__(vehicle1)
        print("child constructor called")
        self.vehicle = vehicle
        
class GrandChild(Child3):
    def __init__(self,  vehicle1, vehicle):
        super().__init__(vehicle1)
        print("child constructor called")
        self.vehicle = vehicle
        
p = Child3("bike", "car")
print(p.__dict__) 

print("========================Hierarchical-Inheritance=================================")


class Parent3:
    def __init__(self, vehicle1):
        print("parent constructor called")
        self.vehicle1 = vehicle1

class Child3(Parent3):
    def __init__(self,  vehicle1, vehicle):
        super().__init__(vehicle1)
        print("child constructor called")
        self.vehicle = vehicle
        
class GrandChild(Child3):
    def __init__(self,  vehicle1, vehicle):
        super().__init__(vehicle1)
        print("child constructor called")
        self.vehicle = vehicle


print("=====================multiple inheritace======================")

print("============multiple inheritance===============")

class Parent1:
    def __init__(self, vehicle1):
        print("Parent1 constructor called")
        self.vehicle1 = vehicle1

class Parent2:
    def __init__(self, vehicle2):
        print("Parent2 constructor called")
        self.vehicle2 = vehicle2

class Child(Parent1, Parent2):
    def __init__(self, vehicle1, vehicle2, vehicle3):
        Parent1.__init__(self, vehicle1)
        Parent2.__init__(self, vehicle2)
        print("Child constructor called")
        self.vehicle3 = vehicle3

c = Child("Bike", "Car", "Bus")

print(c.__dict__)


print("===============MRO(Method Resolution Order.)===================")
#NOTE:  Basically, MRO gets their parent classes list in order (left to right), and uses that order to resolve methods.
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.mro())  # or use D.__mro__

