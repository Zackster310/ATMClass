class ATM:
    def __init__(self, cardNumber, PIN, balance):
        self.balance = balance
        self.PIN = PIN
        self.cardNumber = cardNumber

    def cashWithdrawal(self, PIN, amount):
        if PIN == self.PIN:
            self.balance = self.balance - amount
            print(amount,"has been withdrawn, remaining balance:", self.balance)
        else:
            print("authentication failed")

    def displayBalance(self, PIN):
        if PIN == self.PIN:
            print("current balance:", self.balance)
        else:
            print("authentication failed")


Card1 = ATM(88559966, 5566, 1000)
Card2 = ATM(97468852, 4689, 5000)

Card2.cashWithdrawal(4689, 460)

Card1.displayBalance(5566)
Card2.displayBalance(4689)