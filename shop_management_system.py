import sys
class Store:
    def __init__(self, payment_method, balance, pin): # self is an object, while the others are attributes
        self.payment_method = payment_method  # cash is false, credit card is true
        self.balance = balance
        self.pin = pin
# set methods are those which help to assign a value
# get methods help to return a value
    def set_payment_method(self, payment):
        self.payment_method = payment

    def get_payment_method(self):
        return self.payment_method

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin


# store = Store(False, 1000, "654321")
# y = store.get_balance()

class Shirt(Store):
    def __init__(self, colour, brand, size, price):
        self.colour = colour
        self.brand = brand
        self.size = size
        self.price = price

    def get_colour(self):
        return self.colour

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price

# Instantiating all the 10 objects
# So for example, Shirt3 is an object while Shirt is the class
# As you can see we can assign values in the class according to the attributes that we defined earlier

Shirt1 = Shirt("White", "Supreme", "L", 500)
Shirt2 = Shirt("Blue", "Nike", "M", 70)
Shirt3 = Shirt("Red", "Adidas", "L", 60)
Shirt4 = Shirt("Green", "Gucci", "XL", 1000)
Shirt5 = Shirt("Pink", "Kipsta", "XXL", 35)
Shirt6 = Shirt("Yellow", "Puma", "XXS", 49.99)
Shirt7 = Shirt("Violet", "Khadims", "XS", 29)
Shirt8 = Shirt("Black", "Apple", "M", 150)
Shirt9 = Shirt("Orange", "UnderArmour", "S", 80)
Shirt10 = Shirt("Brown", "Samsung", "L", 30)

# Dictionary menu

dShirt1 = {"Index": 1, "Brand": Shirt1.get_brand(), "Colour": Shirt1.get_colour(), "Size": Shirt1.get_size(),
           "Price": Shirt1.get_price()}

dShirt2 = {"Index": 2, "Brand": Shirt2.get_brand(), "Colour": Shirt2.get_colour(), "Size": Shirt2.get_size(),
           "Price": Shirt2.get_price()}

dShirt3 = {"Index": 3, "Brand": Shirt3.get_brand(), "Colour": Shirt3.get_colour(), "Size": Shirt3.get_size(),
           "Price": Shirt3.get_price()}

dShirt4 = {"Index": 4, "Brand": Shirt4.get_brand(), "Colour": Shirt4.get_colour(), "Size": Shirt4.get_size(),
           "Price": Shirt4.get_price()}

dShirt5 = {"Index": 5, "Brand": Shirt5.get_brand(), "Colour": Shirt5.get_colour(), "Size": Shirt5.get_size(),
           "Price": Shirt5.get_price()}

dShirt6 = {"Index": 6, "Brand": Shirt6.get_brand(), "Colour": Shirt6.get_colour(), "Size": Shirt6.get_size(),
           "Price": Shirt6.get_price()}

dShirt7 = {"Index": 7, "Brand": Shirt7.get_brand(), "Colour": Shirt7.get_colour(), "Size": Shirt7.get_size(),
           "Price": Shirt7.get_price()}

dShirt8 = {"Index": 8, "Brand": Shirt8.get_brand(), "Colour": Shirt8.get_colour(), "Size": Shirt8.get_size(),
           "Price": Shirt8.get_price()}

dShirt9 = {"Index": 9, "Brand": Shirt9.get_brand(), "Colour": Shirt9.get_colour(), "Size": Shirt9.get_size(),
           "Price": Shirt1.get_price()}

dShirt10 = {"Index": 10, "Brand": Shirt10.get_brand(), "Colour": Shirt10.get_colour(), "Size": Shirt10.get_size(),
           "Price": Shirt10.get_price()}

print("==================== Menu ====================")
print(dShirt1)
print(dShirt2)
print(dShirt3)
print(dShirt4)
print(dShirt5)
print(dShirt6)
print(dShirt7)
print(dShirt8)
print(dShirt9)
print(dShirt10)

purchased = False
while not purchased:
    index = float(input("Enter the index of the shirt you want to buy"))
    if 0 < index <= 10:
        if index == int(dShirt1.get("Index")):
            dictionary = dShirt1
            shirt = Shirt1
        if index == int(dShirt2.get("Index")):
            dictionary = dShirt2
            shirt = Shirt2
        if index == int(dShirt3.get("Index")):
            dictionary = dShirt3
            shirt = Shirt3
        if index == int(dShirt4.get("Index")):
            dictionary = dShirt4
            shirt = Shirt4
        if index == int(dShirt5.get("Index")):
            dictionary = dShirt5
            shirt = Shirt5
        if index == int(dShirt6.get("Index")):
            dictionary = dShirt6
            shirt = Shirt6
        if index == int(dShirt7.get("Index")):
            dictionary = dShirt7
            shirt = Shirt7
        if index == int(dShirt8.get("Index")):
            dictionary = dShirt8
            shirt = Shirt8
        if index == int(dShirt9.get("Index")):
            dictionary = dShirt9
            shirt = Shirt9
        if index == int(dShirt10.get("Index")):
            dictionary = dShirt10
            shirt = Shirt10
        print(dictionary)
        shirt_price = shirt.get_price()
        payment_method = input("Enter 0 for cash and 1 for credit card")
        if int(payment_method) == 0:
            bank = Store(False, 1000, "0")
            new_balance = float(bank.get_balance()) - float(shirt_price)
            bank.set_balance(new_balance)
            print('You Have $' + str(new_balance) + ' left')
            purchased = True
        elif int(payment_method) == 1:
            bank = Store(True, 1000, "654321")
            attempts = 0
            if bank.get_balance() >= int(shirt_price):
                while attempts <= 3:
                    pin = input("Enter a pin")
                    if pin == bank.get_pin():
                        print("Transaction successful")
                        new_balance = float(bank.get_balance()) - float(shirt_price)
                        bank.set_balance(new_balance)
                        print("You have $"+str(new_balance)+"left in your code")
                        sys.exit()
                    else:
                        new_attempts = 3 - attempts
                        print("You have"+str(new_attempts)+" left")
                        attempts = attempts + 1
                print("Invalid pin, you will be reported to the CIA")
                sys.exit()
            else:
                print("You have insufficient funds in your bank account")
                sys.exit()
        else:
            print("Enter a valid index")
            sys.exit()

    else:
        print("Invalid index")
        sys.exit()
