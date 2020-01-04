import currency
import currency_1
import currency_5
import currency_10
import currency_20
import currency_50
import currency_100
import currency_500

class token_player(object):
    def __init__(self, id,  node_location, name ):
        self.id = id
        self.wallet = {1: [currency_1(currency())] * 5,
                       5: [currency_5(currency())] * 5,
                       10: [currency_10(currency())] * 5,
                       20: [currency_20(currency())] * 6,
                       50: [currency_50(currency())] * 2,
                       100: [currency_100(currency())] * 2,
                       500: [currency_500(currency())] * 2,
        }
        self.node_location = node_location
        self.ownership_purple = []
        self.ownership_light_blue = []
        self.ownership_pink = []
        self.ownership_orange = []
        self.ownership_red = []
        self.ownership_yellow = []
        self.ownership_green = []
        self.ownership_blue = []
        self.ownership_railroad = []
        self.name = name

    def sell(self, node):
        ##TODO


    def recieve_payment(self,payment):
        for i in range(len(payment)):
            self.wallet[1].extend(payment[0])
            self.wallet[5].extend(payment[1])
            self.wallet[10].extend(payment[2])
            self.wallet[20].extend([payment[3]])
            self.wallet[50].extend([payment[4]])
            self.wallet[100].extend([payment][5])
            self.wallet[500].extend(payment[6])


    def pay(self, price):
        total_payment = 0
        currency_amount_1 = int(input("Enter the number of 1's: "))
        currency_amount_5 = int(input("Enter the number of 5's: "))
        currency_amount_10 = int(input("Enter the number of 10's: "))
        currency_amount_20 = int(input("Enter the number of 20's: "))
        currency_amount_50 = int(input("Enter the number of 50's: "))
        currency_amount_100 = int(input("Enter the number of 100's: "))
        currency_amount_500 = int(input("Enter the number of 500's: "))
        total_payment = (currency_amount_1 * 1) + (currency_amount_5 * 5) + (currency_amount_10 * 10) + (currency_amount_20 * 20) \
                        + (currency_amount_50 * 50) + (currency_amount_100 * 100) + (currency_amount_500 * 500)

        if total_payment >= price:
            confirmation = input(total_payment + "This is how much you are paying type yest to confim purchase or no to exit transaction:" )
            if confirmation.lower() == "yes" or confirmation.lower() == "y":
                payment =  (self.sub_1(currency_amount_1), self.sub_5(currency_amount_5), self.sub_10(currency_amount_10),self.sub_20(currency_amount_20),
                                                         self.sub_50(currency_amount_50),self.sub_100(currency_amount_100),self.sub_500(currency_amount_500))
                return payment
            else:
                return None


    def add_1(self, num):
       val = [[currency_1(currency())]] * num
       self.wallet[1].extend(val)

    def add_5(self, num):
       val = [[currency_1(currency())]] * num
       self.wallet[5].extend(val)

    def add_10(self, num):
       val = [[currency_1(currency())]] * num
       self.wallet[10].extend(val)

    def add_20(self, num):
        val = [[currency_1(currency())]] * num
        self.wallet[20].extend(val)

    def add_50(self, num):
        val = [[currency_1(currency())]] * num
        self.wallet[50].extend(val)

    def add_100(self, num):
        val = [[currency_1(currency())]] * num
        self.wallet[100].extend(val)

    def add_500(self, num):
        val = [[currency_1(currency())]] * num
        self.wallet[500].extend(val)


    def sub_1(self, num):
        if num <= len(self.wallet[1]):
            val = self.wallet[1][-num:]
            del self.wallet[1][-num:]
            return val
        else:
            print("player does not have enough 1 dollars currency")

    def sub_5(self, num):
        if num <= len(self.wallet[5]):
            val = self.wallet[5][-num:]
            del self.wallet[5][-num:]
            return val
        else:
            print("player does not have enough 5 dollars currency")

    def sub_10(self, num):
        if num <= len(self.wallet[10]):
            val = self.wallet[10][-num:]
            del self.wallet[10][-num:]
            return val
        else:
            print("player does not have enough 10 dollars currency")

    def sub_20(self, num):
        if num <= len(self.wallet[20]):
            val = self.wallet[20][-num:]
            del self.wallet[20][-num:]
            return val
        else:
            print("player does not have enough 20 dollars currency")

    def sub_50(self, num):
        if num <= len(self.wallet[50]):
            val = self.wallet[50][-num:]
            del self.wallet[50][-num:]
            return val
        else:
            print("player does not have enough 50 dollars currency")

    def sub_100(self, num):
        if num <= len(self.wallet[100]):
            val = self.wallet[100][-num:]
            del self.wallet[100][-num:]
            return val
        else:
            print("player does not have enough 100 dollars currency")

    def sub_500(self, num):
        if num <= len(self.wallet[500]):
            val = self.wallet[500][-num:]
            del self.wallet[500][-num:]
            return val
        else:
            print("player does not have enough 500 dollars currency")