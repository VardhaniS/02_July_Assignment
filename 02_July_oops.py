#!/usr/bin/env python
# coding: utf-8

# 1. Explain what inheritance is in object-oriented programming and why it is used.
By using inheritance we can reuse the parent class  .
To decrease the complexity of the coode. To reduce the time and space.
# 2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
# differences and advantages.
# 
Single Inheritance - the dervied class or child class inherits properties from the one parent class or base class.
The other propeties can be added .

Multiple Inheritance - the dervied class inherits the properties from more than one base class.
It takes the required propeties from different classes.
# 3. Explain the terms "base class" and "derived class" in the context of inheritance.
# 
Base class - It is also know as the parent class

Dervied class - or the child class . it dervies the propties from the base class
# 4. What is the significance of the "protected" access modifier in inheritance? How does
# it differ from "private" and "public" modifiers?
# 
Protected access modifier can be accessed from the dervied class. 
Private access modifier can be acceses only in the class
Public access modifier can be accessed from everywhere inside and outside of the class
# 5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# 
Super keyword is used in the child classs. It is used to refer the parent class attributes.

# In[3]:


class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display_info(self):
        print(f"Name: {self.name} and age: {self.age}")
        
employee=Employee("Vardhani",24)
employee.display_info()


# 6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
# Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
# attribute called "fuel_type". Implement appropriate methods in both classes.

# In[1]:


class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def display_info(self):
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
              
class Car(Vehicle):
    def __init__(self,make,model,year,fuel_type):
        super().__init__(make,model,year)
        self.fuel_type=fuel_type
        
    def display_info(self):
        super().display_info()
        print(f"Fuel type:{self.fuel_type}")
        
car=Car(564,"XV",2015,"Petrol")
car.display_info()

        


# 7. Create a base class called "Employee" with attributes like "name" and "salary."
# Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
# attribute called "department" for the "Manager" class and "programming_language"
# for the "Developer" class.

# In[5]:


class Employee:
    def __init__(self,name,salary):
        self._name=name
        self.salary=salary
        
    def _display_info(self):
        print(f"Name: {self._name} ")
        print(f"Salary:{self.salary}")
        
    
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display_info(self):
        super()._display_info()
        print(f"Department:{self.department}")
        
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def display_info(self):
        self._display_info()
        print(f"Programming language:{self.programming_language}")
        
manager=Manager("Vardhani",50000,"IT")
manager.display_info()
developer=Developer("Pavani",54000,"BPO")
developer.display_info()
        


# 8. Design a base class called "Shape" with attributes like "colour" and "border_width."
# Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
# specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
# the "Circle" class.

# In[8]:


class Shape:
    def __init__(self,colour,border_width):
        self.colour=colour
        self.border_width=border_width
        
    def display_info(self):
        print(f"Colour :{self.colour}")
        print(f"Border Width:{self.border_width}")
        
class Rectangle(Shape):
    def __init__(self,colour,border_width,length,width):
        super().__init__(colour,border_width)
        self.length=length
        self.width=width
        
    def display_info(self):
        print("Rectangle")
        super().display_info()
        print("Length:",self.length)
        print("Width:",self.width)
    
class Circle(Shape):
    def __init__(self,colour,border_width,radius):
        super().__init__(colour,border_width)
        self.radius=radius
        
    def display_info(self):
        print("Circle")
        super().display_info()
        print("Radius",self.radius)
        
rectangle=Rectangle("White",5.5,6,9)
rectangle.display_info()
circle=Circle("Black",6.3,6)
circle.display_info()


# 9. Create a base class called "Device" with attributes like "brand" and "model." Derive
# two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
# "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.

# In[11]:


class Device:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        
class Phone(Device):
    def __init__(self,brand,model,screen_size):
        super().__init__(brand,model)
        self.screen_size=screen_size
        
    def display_info(self):
        super().display_info()
        print("Screen_size:",self.screen_size)
        
class Tablet(Device):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity=battery_capacity
        
    def display_info(self):
        super().display_info()
        print("Battery Capacity:",self.battery_capacity)
        
iphone=Phone("MI",'7s',16)
iphone.display_info()
tablet=Tablet("Apple",3,90)
tablet.display_info()
    


# 10. Create a base class called "BankAccount" with attributes like "account_number" and
# "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
# "BankAccount." Add specific methods like "calculate_interest" for the
# "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

# In[4]:


class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
class SavingAccount(BankAccount):
    def calculate_interest(self):
        self.balance=self.balance+(self.balance*0.04)
        print("Balance of Saving Account:",self.balance)
        
class CheckingAccount(BankAccount):
    def deduct_fees(self):
        self.balance=self.balance-500
        print("Balance of Checking Account:",self.balance)

saving_account=SavingAccount(543876,900)
saving_account.calculate_interest()

checking_account=CheckingAccount(236944,8256)
checking_account.deduct_fees()


# In[ ]:




