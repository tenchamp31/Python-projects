class User:                         #creating User
    name = "Anthony"
    email = "anthony2@gmail.com"
    password = "23424322"


    def GetLoginInfo(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter email here: ")
        entry_password= input("Enter password here: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password is incorrect.")




class Employee(User):
    base_pay = 12.50
    department = "retail"
    pin_number= "343343"


    def GetLoginInfo(self):                         #using pin instead of password
        entry_name = input("Enter name here: ")
        entry_email = input("Enter email here: ")
        entry_password= input("Enter password here: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The pin/email is incorrect")



#Using both user and employee class

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()





            






    

