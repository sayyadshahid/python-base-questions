# polymorphism:====>  One function or method works in different ways depending on the object it is working with.
# ex: --> len() function is working on dict, string and touples count their length but differrent ways 



print("===========polymorphism with inheritace================")
class Veh:
    def __init__(self, name, colour, price):
        self.name = name
        self.colour = colour
        self.price = price

    def get_details(self):
        print(f"name is: {self.name}, colour is: {self.colour} and price is: {self.price}")

    def max_speed(self):
        print(f"for {self.name}  max speed is 200")

class Car(Veh):
    def max_speed(self):
        print(f"for {self.name} max speed is 300")


V1 = Veh("Kawasaki", "red", 400000)
C1 = Car("BMW", "White", 70000000)

V1.get_details()
C1.get_details()


print("===========for max_speed have same function but different work this is called pollymorphism=====================")
V1.max_speed()
C1.max_speed()


print("=========over-riding build in function =======================")
# with __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):  # Overriding built-in str()
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title) + len(self.author)

b = Book("Harry Potter", "J.K. Rowling")
print(b)  # Outputs: Harry Potter by J.K. Rowling
print(len(b))


print("=============with function===================")

class Veh:
    def __init__(self, name, colour, price):
        self.name = name
        self.colour = colour
        self.price = price

    def get_details(self):
        print(f"name is: {self.name}, colour is: {self.colour} and price is: {self.price}")

    def max_speed(self):
        print(f"for {self.name}  max speed is 200")

class Car(Veh):
    def max_speed(self):
        print(f"for {self.name} max speed is 300")

def call(obj):
    obj.get_details()
    obj.max_speed()


V1 = Veh("Kawasaki", "red", 400000)
C1 = Car("BMW", "White", 70000000)
call(V1)
print("++++++++++next++++++=++")
call(C1)