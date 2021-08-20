class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber 

    def cashWithdrawlOrDeposit(self):
       answer = input("Would like to make a Cash withdrawl (yes or no, saying no will send you to the Cash Deposit stage)? ")
  
       if answer == "yes":
            print("Set to Cash WithDrawl stage:")
            print("Your card number is", self.cardNumber, "and pin number is", self.pinNumber)
            withdrawlNumber = int(input("How much money would you like to withdrawled from your account? "))
            print(withdrawlNumber, "dollars is being put it in your card and withdrawled from your account.")
        
       elif answer == "no":
            print("Set to Cash Deposit stage:")
            print("Your card number is", self.cardNumber, "and pin number is", self.pinNumber)
            depositNumber = int(input("How much money would you like to deposit to your account? "))
            print(depositNumber, "dollars is being deposited into your account and taken from your card.")

john = ATM("451 209 7182", "0122")
john.cashWithdrawlOrDeposit()