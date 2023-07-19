from significant_program import append_item_and_price, show_item_and_price, remove_item_and_price, compute_total
import pytest

def test_append_item_and_price():
    """Test the append_item_and_price function."""
    items = []
    item_prices = []
    new_item = "butter"
    new_price = 6

  
    assert append_item_and_price("milk",3) != "milk"
    assert append_item_and_price("", 3) == "",3
    assert append_item_and_price(new_item,new_price) != "milk",6
    

def test_show_item_and_price():
    """Test the show_item_and_price function."""
    items = ["milk"]
    item_prices = [5]

    assert show_item_and_price(items,item_prices) != "1. Butter - $5.0"
    assert show_item_and_price(items, item_prices) != ""
    assert show_item_and_price(items, item_prices) == "milk",5
    assert show_item_and_price(items, item_prices) != "butter",5


def test_remove_item_and_price():
    """Test the remove_item_and_price function."""
    items = ["milk","butter","chocolate"]
    item_prices = [3.10, 4, 2.50]
    removed_item = 1

    assert remove_item_and_price(removed_item) != "milk"
    assert remove_item_and_price(removed_item) != 3.10
    

def test_compute_total():
    """Test the compute_total function."""
    #Some list with values that are the prices for different items to test this function-
    item_prices = [3,4,2,5]
    fruit_prices = [5,5,5,5]
    menu = [15,10,20]

    #This assertion is the correct sum in item_prices list.
    assert compute_total(item_prices) == 14
    #This assertion is the incorrect sum in item_rpices list.
    assert compute_total(item_prices) != 15
    assert compute_total(fruit_prices) == 20
    assert compute_total(fruit_prices) != 30
    assert compute_total(menu) == 45
    assert compute_total(menu) != 46


pytest.main(["-v", "--tb=line", "-rN", "test_significant_program.py"])