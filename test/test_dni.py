from src.dni import *
import pytest

@pytest.mark.check_document
def test_check_document():    
    assert dni('49482728E').checkLength() == 'Checking DNI given'
    assert dni('49482723388E').checkLength() == False
    assert dni('48288').checkLength() == False
 
    assert dni('49482728E').checkNum() == True
    assert dni('45185088O').checkNum() == True
    assert dni('erer34567').checkNum() == 'DNI must contain numbers'
    
    assert dni('49482728E').checkLenDniNums() == True
    assert dni('49482728').checkLenDniNums() == False
    assert dni('4885').checkLenDniNums() == False
    
    assert dni().correctDniNum() == "Checking if letter it's correct"

    assert dni('49482728E').checkDniLetter() == 'Checking DNI letter'
    assert dni('494827E88').checkDniLetter() == 'DNI last character must be a letter'
      
    assert dni('49482728E').obtainLetter() == 'E'
    assert dni('78484464T').obtainLetter() == 'T'
    assert dni('26861694V').obtainLetter() == 'V'
    
    assert dni('49482728E').getDniNumPart() == '49482728'
   
    assert dni('49482728e').getDniletterPart() == 'E'
    assert dni('49482728a87').getDniletterPart() =='7'