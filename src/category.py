class Category:
    def __init__(self, type):
        self.type = type
        self.ledger = []
        self.amount = 0
        self.description = ""
        self.total = 0

    def deposit(self, pAmount, pdescription):
        emptyStr = " "
        # if description == null:
        #     self.ledger.append({ "amount": pAmount, "description": emptyStr })
        # else:
        self.ledger.append({"amount": pAmount, "description": pdescription})
        print(self.ledger)

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
        if amount < self.total:
            transferTo = f'Transfer to {type}'
            self.withdraw(amount, transferTo)
            transferFrom = f'Transfer from {self.type}'
            self.deposit(amount, transferFrom)
            return True
        else:
            return False

    def check_funds(self, amount, type):
        if amount < type.total:
            return False
        else:
            return True

    def __str__(self):
        # items = ""
        # for key, value in self.ledger.items():
        #     items = (key, ":  ", value)


        return f'''
        *************{self.type}*************
        Total: {self.total}
        '''


clothing = Category("Clothing")
clothing.deposit(10, "new shoes")
print(clothing.deposit(10, "new shoes"))
