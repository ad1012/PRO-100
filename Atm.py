class Atm:
    def __init__(self, cardNumber, pin ):

        self.cardNumber = cardNumber
        self.pin = pin

    def check_balance(self):

        print("Your current balance is: 250000")

    def withdrawal(self, balance):
        new_balance = 250000 - balance
        print("You have withdrew "+ str(balance) +". Your new balance is "+ str(new_balance))


def main():
    Card_number = input("Enter your Card Number: ")
    pin_number = input("Enter Your Pin Number: ")

    new_user = Atm(Card_number, pin_number)

    print("Select an option: ")
    print("1.Withdraw    2.Check Balance")
    activity = int(input("Enter Activity Number: "))

    if (activity == 1):
        balance = int(input("Enter your amount: "))
        new_user.withdrawal(balance)
    elif (activity == 2):
        new_user.check_balance()
    else:
        print("Enter a Valid Number")

if __name__ =="__main__":
    main()


