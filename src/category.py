class Category:
    def __init__(self):
        self.type = "type"
        self.ledger = []
        self.amount = 0
        self.description = ""
        self.total = 0

    def deposit(self, pAmount, pdescription):
        emptyStr = " "
        if description == "":
            self.ledger.append({ "amount": pAmount, "description": emptyStr })
        else:
            self.ledger.append({"amount": pAmount, "description": pdescription})

    def withdraw(self, nAmount, ndescription):
        if nAmount > self.total:
            return False
        else:
            self.ledger.append({"amount": nAmount, "description": ndescription})
            return True

    def get_balance(self):
        getBalance = self.ledger.values()
        balance = eval(getBalance)
        return balance

    def transfer(self, amount, type):
        pass

    def check_funds(self, amount, type):
        pass

    def __str__(self):
        pass