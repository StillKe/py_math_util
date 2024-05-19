import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14
    
def test_add_strings():
    result = math_func.add('Hello', ' World')  # Fixed typo in 'Hello'
    assert result == 'Hello World'  # Removed extra comma
    assert isinstance(result, str)  # Changed to isinstance for type check
    assert 'sd' not in result  # Corrected assertion logic

def test_product_string():
    assert math_func.product('Hello', 3) == 'HelloHelloHello'  # Removed spaces
    result = math_func.product('Hello')  # Fixed typo in 'Hello'
    assert result == 'HelloHello'  # Removed extra spaces
    assert isinstance(result, str)
    assert 'Hello' in result  # Corrected assertion logic
