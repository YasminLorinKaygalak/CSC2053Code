# Declare the class BankAccount
# Python convention is to capitalize first letter in each word of class name
class BankAccount:
    # __init__ method is like the constructor in Java
    # variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # __str__ is like the toString() method in Java
    # it's used for debugging purposes
    def __str__(self): #__ methodsa are given by pyhton
        return self.account_number + ' has the balance ' + str(self.balance) #since we are returning and concatenating strings you have to turn the integer to a str value 

    # first parameter in class methods MUST
    # be self
    def deposit(self, amount): #the user created these methods because there is no underscore
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance
