'''
CODE BY TEAM INCODE
LNCT-U
BCA-AIDA
SEM-2
SECTION-A AND B
'''
import random as rd


def bus_t(available,From,to,bus_price,payment_method):
    if available["Bus"]>0:
        print("-----Bus Ticket Booking.-----")
        print("Are Buses Routes are")
        for i in range(len(From)):
            print(i," From",From[i],"to",to[i])

        bus=input("Enter the bus number:")
        seats = [12, 54, 23, 13, 43, 45]
        for i in seats:
            print("These seat are available", i)

        user_seat = input("Enter the seat number: ")
        Name=input("Enter the Name: ").title()
        while(len(Name)<0):
            print("Name cannot be empty")
            Name = input("Enter the Name: ").title()
        Age=int(input("Enter the Age: "))
        while(Age<0 or Age>200):
            Age=int(input("Enter the Age: "))
        Gender=input("Enter the Gender(M or F): ").upper()
        while(Gender!='M' or Gender!='F'):
            Gender=input("Enter the Gender(M or F): ").upper()
        if bus=="0":
            available["Bus"]=available["Bus"]-1
            date=int(input("Enter the date:"))
            if date > 0 and date <= 31:
                print("The price of the ticket is ",bus_price[0])
                print("Going to the payment gateway.....")
                bus_payment(bus_price[0],payment_method)
        elif bus=="1":
            available["Bus"]=available["Bus"]-1
            date=int(input("Enter the date:"))
            if date > 0 and date <= 31:
                print("The price of the ticket is ",bus_price[1])
                print("Going to the payment gateway.....")
                bus_payment(bus_price[1], payment_method)
        elif bus=="2":
            available["Bus"]=available["Bus"]-1
            date=int(input("Enter the date:"))
            if date > 0 and date <= 31:
                print("The price of the ticket is ",bus_price[2])
                print("Going to the payment gateway.....")
                bus_payment(bus_price[2],payment_method)
        elif bus=="3":

            available["Bus"]=available["Bus"]-1
            date=int(input("Enter the date:"))
            if date > 0 and date <= 31:
                print("The price of the ticket is ",bus_price[3])
                print("Going to the payment gateway.....")
                bus_payment(bus_price[3],payment_method)
        else:
            print()
            return bus_t(available,From,to,bus_price,payment_method)
    else:
        print("No bus available")
        return None

def train_t(available,From,to,train_price,payment_method):
    if available["Train"] > 0:
        print("-----Train Ticket Booking.-----")
        print("Are Trains Routes are")
        for i in range(len(From)):
            print(i, " From", From[i], "to", to[i])

        train = input("Enter the Train number:")
        seats = [12, 54, 23, 13, 43, 45]
        for i in seats:
            print("These seat", i)

        user_seat = input("Enter seat number: ")
        Name=input("Enter the Name: ").title()
        while(len(Name)<0):
            print("Name cannot be empty")
            Name = input("Enter the Name: ").title()
        Age=int(input("Enter the Age: "))
        while(Age<0 or Age>200):
            Age=int(input("Enter the Age: "))
        Gender=input("Enter the Gender(M or F): ").title()
        while(Gender!="M" or Gender!="F"):
            Gender=input("Enter the Gender(M or F): ").title()
        if train == "0":
            available["Train"] = available["Train"] - 1
            date=int(input("Enter the date:"))
            if date > 0 and date < 31:
                print("The price of the ticket is ", train_price[0])
                print("Going to the payment gateway.....")
                train_payment(train_price[0], payment_method)
        elif train == "1":

            available["Train"] = available["Train"] - 1
            date=int(input("Enter the date:"))
            if date >0 and date<31:
                print("The price of the ticket is ", train_price[1])
                print("Going to the payment gateway.....")
                train_payment(train_price[1], payment_method)
        elif train == "2":
            available["Train"] = available["Train"] - 1
            date=int(input("Enter the date:"))
            if date > 0 and date < 31:
                print("The price of the ticket is ", train_price[2])
                print("Going to the payment gateway.....")
                train_payment(train_price[2], payment_method)
        elif train == "3":

            available["Train"] = available["Train"] - 1
            date=int(input("Enter the date:"))
            if date > 0 and date < 31:
                print("The price of the ticket is ", train_price[3])
                print("Going to the payment gateway.....")
                train_payment(train_price[3], payment_method)
        else:
            print()
            return train_t(available, From, to, train_price, payment_method)
    else:
        print("No bus available")
        return None
def bus_payment(bus_price,payment_method):
    print("These are payment method")
    print("Upi")
    method=input("Enter the payment method:").title()
    if method in payment_method:
        upi_id=input("Enter the upi id: ")
        price=bus_price
        print("The price of the ticket is ",price)
        print("Payment Successful")
        print("Making bill")
        bill(price)
        return None
    else:
        return bus_payment(bus_price,payment_method)

def train_payment(train_price,payment_method):
    print("These are payment method")
    print("Upi")
    method=input("Enter the payment method:").title()
    if method in payment_method:
        upi_id=input("Enter the upi id:")
        price=train_price
        print("The price of the ticket is ",price)
        print("Payment Successful")
        print("Making bill")
        bill(price)
        return None
    else:
        return train_payment(train_price,payment_method)

def bill(price):
    print("\n---Bill---")
    gst=(price*18/100)
    pf=12
    gstp=price-gst
    tprice=price+pf
    print("------Ticketing Booking System------")
    print("Ticket price: ",gstp)
    print("Gst: ",gst)
    print("Platform fees: ",pf)
    print("Total price: ",tprice)


def login():
    usernames = ["Aayush098", "Akshit007", "Sanskar200", "Saraswat001"]
    passwords = ["bhoaplaayush", "password", "papaji", "lnct"]
    user_n_or_o=input("Old User or New User: ").title()
    if user_n_or_o == "New":
        username = input("Enter username: ").title()
        password = input("Enter password: ").lower()
        usernames.append(username)
        passwords.append(password)
        in1 = usernames.index(username)
        in2 = passwords.index(password)
        if username in usernames and password in passwords:
            if in1 == in2:
                print("Login Successful")
                return None
            else:
                print("Login Failed")
                print("Retry")
                return login()
        else:
            print("Login Failed")
            print("Retry")
            return login()

    else:
        username = input("Enter username: ").title()
        password = input("Enter password: ").lower()
        in1=usernames.index(username)
        in2=passwords.index(password)
        if username in usernames and password in passwords:
            if in1==in2:
                print("Login Successful")
                return None
            else:
                print("Login Failed")
                print("Retry")
                return login()
        else:
            print("Login Failed")
            print("Retry")
            return login()


def main():
    From=["Bhopal","Indore","Sagar","Ujjain"]
    to=["Indore","Sagar","Bhopal","Bhopal"]
    bus_price=[500,600,400,400]
    train_price=[1200,980,780,1000]
    payment_method=["Upi"]
    available={"Bus":10,"Train":32}
    print("------Welcome To Ticketing Booking System------")
    login()
    bus_or_train=input("What do you want to book Train or Bus: ").lower()
    if bus_or_train=="bus":
        bus_t(available,From,to,bus_price,payment_method)
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ran_pnr_number = rd.choices(numbers, k=10)
        s = ""
        for i in range(len(numbers)):
            s += ran_pnr_number[i]
        print("\nThe bus number is ",s)
    elif bus_or_train=="train":
        train_t(available,From,to,train_price,payment_method)
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ran_pnr_number = rd.choices(numbers, k=10)
        s = ""
        for i in range(len(numbers)):
            s += ran_pnr_number[i]
        print("\nThe train pnr is PNR",s)

    print("Do you want to cancel this ticket? (y/n)")
    yes=input("Enter: ")
    if yes == "y" or yes == "Y":
        c_cancel=input("Do you really want cancel this ticket? (y/n)")
        if c_cancel == "y" or c_cancel == "Y":
            print("Ticket canceled.")
        else:
            print("Ticket not Canceled.")
    else:
        print("Ticket not canceled.")

    print("Thank you for using are services")









main()