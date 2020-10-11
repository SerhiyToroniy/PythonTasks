class SwiftTransfer:

    def __init__(self, ident = None, iban_number = None, account_holder = None, amount = None, currency = None, fee_amount = None, payment_date = None):
        self.ident = ident
        self.iban_number = iban_number
        self.account_holder = account_holder
        self.amount = amount
        self.currency = currency
        self.fee_amount = fee_amount
        self.payment_date = payment_date

    def __str__(self):#possibility to use "print(SwiftTransfer())"
        result = ""
        for i in dir(self):
            if i[0]+i[1]!="ge" and i[0]+i[1]!="se" and i[0]+i[1]!="__":   result+=i.upper() + ": " + str(getattr(self,i)) + "\n"
        return result

    #getters for every single attribute of our class
    def getID(self):
        return self.ident
    def getIBAN_NUMBER(self):
        return self.iban_number
    def getACCOUNT_HOLDER(self):
        return self.account_holder
    def getAMOUNT(self):
        return self.amount
    def getCURRENCY(self):
        return self.currency
    def getFEE_AMOUNT(self):
        return self.fee_amount
    def getPAYMENT_DATE(self):
        return self.payment_date

    #setters for every single attribute of our class
    def setID(self, var):
        self.ident = var
    def setIBAN_NUMBER(self, var):
        self.iban_number = var
    def setACCOUNT_HOLDER(self, var):
        self.account_holder = var
    def setAMOUNT(self, var):
        self.amount = var
    def setCURRENCY(self, var):
        self.currency = var
    def setFEE_AMOUNT(self, var):
        self.fee_amount = var
    def setPAYMENT_DATE(self, var):
        self.payment_date = var
