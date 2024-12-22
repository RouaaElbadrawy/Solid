# Single-Responsibility Principle (SRP)

class Employee:
        def __init__(self, name, email):
            self.name = name
            self.email = email

class EmailService:
    def send_email(self, customer, message):
        pass

class OrderService:
    def make_order(self, customer, order):
        pass

class InvoiceService:
    def generate_invoice(self, customer, invoice):
        pass 
    
    
# Open-Closed Principle (OCP)
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod 
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'

class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

class Cat(Animal):
    def make_sound(self):
        return 'meow'

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
        
        
# Liskov Substitution Principle (LSP) 
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width  

rectangle = Rectangle(2, 3)
print(rectangle.area())

square = Square(4)
square.set_width(5)
print(square.area())  

# Interface Segregation Principle (ISP)
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class Fax:
    def fax(self):
        pass

class SimplePrinter(Printer):
    def print(self):
        print("Printing document")

class MultifunctionalDevice(Printer, Scanner, Fax):
    def print(self):
        print("Printing document")

    def scan(self):
        print("Scanning document")

    def fax(self):
        print("Sending fax")
        
# Dependency Inversion Principle (DIP)
class NotificationService:
    def send(self, message):
        pass  

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, message):
        self.notification_service.send(message)























        
        