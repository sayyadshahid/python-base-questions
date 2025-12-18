# class variable 


class Employee:
    company_name = "google" # class variable 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# access class variable 

e1 = Employee("shahid", 20000)  # ======> objects 
e2 = Employee("shaaad", 50000)

print(Employee.company_name) #google
print(e1.company_name) #google

# modify class variables
# class_name.variable name 
Employee.company_name = "tcs"
print(Employee.company_name) #tcs

print("==========================with decoretor(@classmethod)===============================")

# with decoretor

class Employeee:
    company_name = "fladdra" # class variable 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    @classmethod  #decoretor 
    def get_class_name(cls):
        # modifying variable name 
        cls.company_name = "JACSTO"
        print(cls.company_name)

Employeee.get_class_name() 


print("===============@staticmethod========================")
class Bank:
    bankname = "BOI"
    rate_of_interest = 12.90

    @staticmethod
    def SI(principal, year):
        si = (principal * year * Bank.rate_of_interest) / 100
        print(si)

# Call using class
Bank.SI(20000, 2)

# Call using object
b = Bank()
b.SI(20000, 2)
