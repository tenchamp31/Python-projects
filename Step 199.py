class User:                           #defining User
    name = "bradford"
    email= "bradford@gmail.com'
    password = '32423462342"
    account_number = 1

class Employee(User):                   #giving child class
    base_pay = 12.45
    department = "Sanitation"
    schedule = M-F


class Customer(User):
    mailing_address = "2354 S.Blvd avnue, florida"
    mailing_list = True
