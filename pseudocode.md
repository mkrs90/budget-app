class of Category:
    define __init__(self):
        self.name - like food, clothing, and entertainment
        self.ledger = []
        self.total = 0

    define deposit(self accept amount and description):
        if no description given default to empty string
        else append the following object to the ledger list
        {"amount": amount, "description": description}


    (should this be an if statement? if positive do deposit, negative withdraw)
    define withdraw(self accepts negative amounts):
        if there are not enough funds return false - nothing should be added to ledger
        else (when there are enough funds)
        add negative number to the ledger and return true

    define get_balance(self):
        returns current balance based on what is currently in the ledger
        target only the values then eval them to get total
       
    define transfer(self amount categoryType):
        calls the withdraw method that give it the amount and a description of 
        "Transfer to [Destination Budget Category]. 
        calls deposit method that adds that amount and a description of 
        "Transfer from [Source Budget Category].
        IF not enough funds nothing happens.
        Return true if transfer happened false if not
       
    define check_funds(self accepts amount category):
        if the amount is less than funds of the budget category
            return false
        else
            returns true

    define __str__(self):
        A title line where the name of the category is centered in a line of * characters.
        A list of the items in the ledger. 
        A line displaying the category total.

        will I need to loop through the list to add to the return statement?

        return f'''
        *************{self.category}*************
        initial deposit        1000.00
        groceries               -10.15
        restaurant and more foo -15.89
        Transfer to Clothing    -50.00
        Total: {self.total}
        '''





       