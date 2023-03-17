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
-----------------------------------------------------

# Requirements

Complete the **Category class** in **category.py**. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment (open ended, but your final script should show usage of at least three categories for the budget). 

When objects are created, they are passed in the name of the category, only. The class should have an instance variable called **ledger that is a list**. The class should also contain the following methods:
 - A **deposit** method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

 - A **withdraw** method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.

 - A **get_balance** method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

 - A **transfer** method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.

A **check_funds** method that accepts an amount as an argument. It returns False if the amount is less than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

When the budget object is printed (__str__ or __repr__ method) it should display:
    - A title line where the name of the category is centered in a line of * characters.
    - A list of the items in the ledger. 
    - A line displaying the category total.
    
    Here is an example of the output:
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96





       