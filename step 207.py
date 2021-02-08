#Parent class

class User:
    name = "Bob"
    email = "bob@gmail.com"
    password = "3443"

    def getLoginInfo(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter email here: ")
        entry_password = input("Enter password here: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))

        else:
            print("Password/email is incorrect.")


#Child class
class Employee(User):
    base_pay = 12.75
    department = "Sanitation"
    pin_number = 567


#Child class
class Intern(User):
    base_pay = 0.00
    department = "Internship"
    pin_number = 000
    reference_number = 912


    def getLoginInfo(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter email here: ")
        entry_pin = input("Enter pin here: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))


#Using both methods

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

Intern = Intern()
intern.getLoginInfo()


    
