from category import Category

def test_one():
    assert True

# You can write tests here or create new files in this directory with the name test_[something].py


def test_deposit():
    c = Category("Food")
    c.deposit(10, "paycheck")
    assert True

#Create Category class
def test_category_class():
    c = Category("food")
    assert isinstance(c, Category)

#Category has type attribute
def test_category_has_type():
    c = Category("type")
    assert hasattr(c, "type")

#Category type can be set
def test_create_category_with_type_setter():
    type_name = "Clothing"
    c = Category(type_name)
    c.type = type_name
    assert c.type == type_name

#Category can have multiple category types
def test_category_can_have_multiple_types():
    c1 = Category("Food")
    c2 = Category("Entertainment")
    assert c1 != c2

#Category has ledger attribute
def test_category_has_ledger_attribute():
    c = Category("Entertainment")
    c.deposit(20, "paycheck")
    assert c.ledger != []

#Ledger is a list
def test_category_is_a_list():
    c = Category("Entertainment")
    c.deposit(20, "paycheck")
    if isinstance(c.ledger, list):
        assert True
    else:
        assert False 
        
#########################################################################################

#Category has deposit method
def test_category_has_deposit_method():
    c = Category("Strawberries")
    assert hasattr(c, 'deposit')


#If deposit method is missing description arg then empty str is return
def test_missing_deposit_description():
    c = Category("Pets")
    c.deposit(30)
    assert c.ledger == [{'amount': 30, 'description': ""}]

#Deposit method updates category balance(total)
def test_deposit_updates_total():
    c = Category("Pets")
    c.deposit(30)
    assert c.total == 30

#Deposit method updates ledger
#Deposit method accepts amount and description
#Ledger format is {"amount": amount, "description": description}
def test_category_matches_intended_format():
    c = Category("Entertainment")
    c.deposit(20, "paycheck")
    assert c.ledger == [{'amount': 20, 'description': 'paycheck'}]

######################################################################################
#Category has withdraw method
def test_category_has_withdraw_method():
    c = Category("Bananas")
    assert hasattr(c, 'withdraw')


#withdraw method uses check_funds method before running
#Withdraw will fail if there is not enough funds
def test_withdraw_fails_when_low_funds():
    c = Category("Oranges")
    c.withdraw(20, "stuff")
    assert c.ledger != [{'amount': -20, 'description': 'stuff'}]

#Withdraw amount is stored as a negative number
def test_withdraw_amount_is_negative():
    c = Category("Oranges")
    c.deposit(30)
    c.withdraw(20, "stuff")
    assert c.ledger == [{'amount': 30, 'description': ''}, {'amount': -20, 'description': 'stuff'}]


#Withdraw returns True if withdraw took place
#Withdraw lowers the category balance by withdraw amount
def test_withdraw_lowers_cat_balance():
    c = Category("Plums")
    c.deposit(40)
    c.withdraw(20)
    assert c.total < 40


#Category has get_balance method
#get_balance method returns current balance of the budget for category type

#Category has transfer method
#transfer method takes in another budget category
#transfer method uses check_funds method before running
#transfer method add a withdrawal to ledger with amount and description
#transfer method removes amount from current category and adds amount to another category
#ledger has "Transfer to [destination]" in current category
#ledger has "Transfer from [destination]" in destination category
#transfer method returns true if transfer took place
#transfer method returns false if false if failed

#Category has check_funds method
#check funds accepts an amount as arg
#check funds returns false if amount is less than the balance of category
#check funds returns True if amount is more than the balance of category

#Category has __str__ method
#__str__ returns a title line
#returns a list of items from the ledger
#returns the category total