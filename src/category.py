class Category:
    def __init__(self, type):
        self.type = type
        self.ledger = []
        self.total = 0

    def deposit(self, pAmount, pDescription=""):
        self.ledger.append({"amount": pAmount, "description": pDescription}) 
        self.total += pAmount
        

    def withdraw(self, nAmount, nDescription=""):
        if nAmount > self.total:
            print("Not enough funds")
            return False
        else:
            self.ledger.append({"amount": -1*nAmount, "description": nDescription}) 
            self.total -= nAmount
            return True

    def get_balance(self):
        return f'Your balance is ${self.total}'

    def transfer(self, amount, category_to):
        if amount < self.total:
            transferTo = f'Transfer to {category_to.type}'
            self.withdraw(amount, transferTo)
            transferFrom = f'Transfer from {self.type}'
            category_to.deposit(amount, transferFrom)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.total:
            print('You have enough money in your account')
            return False
        else:
            print(f'Warning, amount exceeds your balance of {self.total}')
            return True

    def __str__(self):       
        outputStr = f"*************{self.type}*************\n"
        for item in self.ledger:
            outputStr += f'{item["description"]:30}${item["amount"]:8.2f}\n'
        outputStr += f'Total: ${self.total:8.2f}\n'
        return outputStr


clothing = Category("Clothing")
clothing.deposit(10.00, "sold shoes")
clothing.deposit(20.00)
clothing.withdraw(15.00, "new shoes")
clothing.check_funds(40.00)
clothing.check_funds(5.00)

food = Category("Food")
food.deposit(20.00, "paycheck")
food.withdraw(10.00, "groceries")
clothing.transfer(5, food)


print(clothing)
print(food)
