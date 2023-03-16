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
    c = Category("food")
    assert hasattr(c, "food")

#Category type can be set
def test_create_category_with_type_setter():
    type_name = "Clothing"
    c = Category(type_name)
    c.type = type_name
    assert c.type == type_name

#



