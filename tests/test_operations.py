from src.math_operations import *  

 

def test_add() :
    assert add(2, 3) == 5 # assert functions checks if the result of the add function is equal to 5
    assert add(1 ,-1) == 0   
    





def test_subtract():
    assert sub(5,3) ==  2 
    assert sub(5,4) == 1 
    assert sub(3,3) == 0 
    assert sub(2,3) == -1