class SwiftTransfer:
    def __init__(self, id = None, iban_number = None, account_holder = None, amount = None, currency = None, fee_amount = None, payment_date = None):
        self.id = id
        self.iban_number = iban_number
        self.account_holder = account_holder
        self.amount = amount
        self.currency = currency
        self.fee_amount = fee_amount
        self.payment_date = payment_date

    def __str__(self):#possibility to use "print(SwiftTransfer)"
        return "ID: " + str(self.id) + "\nIban_num: " + str(self.iban_number) + "\nAccount holder: " + str(self.account_holder) + "\nAmount: " + str(self.amount) + "\nCurrency: " + str(self.currency) + "\nFee_amount: " +str(self.fee_amount) + "\nPayment_date: " + str(self.payment_date)

    def _input(self):
        self.id = input("ID: ")
        self.iban_number = input("Iban number: ")
        self.account_holder = input("Account holder: ")
        self.amount = input("Amount: ")
        self.currency = input("Currency: ")
        self.fee_amount = input("Fee amount: ")
        self.payment_date = input("Payment date: ")
        return self

    #getters for every single attribute of out class
    def _getID(self):
        return self.id
    def _getIBAN_NUMBER(self):
        return self.iban_number
    def _getACCOUNT_HOLDER(self):
        return self.account_holder
    def _getAMOUNT(self):
        return self.amount
    def _getCURRENCY(self):
        return self.currency
    def _getFEE_AMOUNT(self):
        return self.fee_amount
    def _getPAYMENT_DATE(self):
        return self.payment_date
