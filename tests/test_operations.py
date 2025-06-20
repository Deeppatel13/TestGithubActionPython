from src.math_operations import add, subtract

def test_add():
    assert add(4,8)==12
    assert add(-6,8)==2
    assert add(55,44)==99
    
def test_sub():
    assert subtract(4,8)==-4
    assert subtract(54,50)==4
    assert subtract(75,65)==10