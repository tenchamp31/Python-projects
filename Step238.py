from abc import ABC, abstractmethod
class computer(ABC):
    def paySlip(self, amount):
            print("Your computer price amount: ",amount)        #pass the argument
    @abstractmethod
    def payment(self, amount):
        pass


class Creditcardpayment(computer):
    def payment(self, amount):
        print("The spending amount of {} has surpassed your 150$ limit ".format(amount))


obj = Creditcardpayment()
obj.paySlip("600$")
obj.payment("600")




