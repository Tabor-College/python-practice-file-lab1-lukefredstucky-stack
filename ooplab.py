'''
class Dog:
    def __init__(self, name, age):
        self.name = name

    def bark(self):
        print(self.name, "says woof")


d1 = Dog("buddy", 3)
print(d1.name)
d1.bark()


class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self,a,b):
        return a*b
    def subtract(self,a,b):
        return a-b
    def divide(self,a,b):
        return a/b
c = Calculator()
print(c.add(2,3))
print(c.multiply(4,5))

class bankaccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance =+ amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficent funds")
        else:
            self.balance -= amount
    def display(self):
        print(self.owner," has ", self.balance)

acc = bankaccount("alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.display()


class counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count =+1
    def display(self):
        print("count", self.count)     
c = counter()   
c.increment()
c.increment()
c.display()
'''


class car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def accelerate(self):
        self.speed += 10
    def brake(self):
        if self.speed <= 0:
            print("cannot go slower than 0")
        else:
            self.speed -= 5
    def display(self):
        print(self.brand,"speed", self.speed)
c1 = car("toyota",50)
c1.accelerate()
c1.display()


#questions
#a class is a way to bundle attributes into a singular section of a program
#objects are string and numbers or any variable python sees



