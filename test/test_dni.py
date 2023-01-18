from src.dni_OCP_SRP import *
import pytest

@pytest.mark.check_length
def test_check_document():    
    assert dni('49482728E').checkLength() == 'Checking DNI given'
    assert dni('49482723388E').checkLength() == False
    assert dni('48288').checkLength() == False

@pytest.mark.check_num
def test_check_num():
    assert dni('49482728E').checkNum() == True
    assert dni('45185088O').checkNum() == True
    assert dni('erer34567').checkNum() == False

@pytest.mark.check_dniLetter
def test_check_dni_letter():
    assert dni('49482728E').checkDniLetter() == 'Checking DNI letter'
    assert dni('494827E88').checkDniLetter() == 'DNI last character must be a letter'
      
@pytest.mark.check_lenDni
def test_checkLenNums():    
    assert dni('49482728E').checkLenDniNums() == True
    assert dni('4942728').checkLenDniNums() == 'DNI must contain 8 digits and 1 letter'
    assert dni('48878789965').checkLenDniNums() == 'DNI must contain 8 digits and 1 letter'
 
@pytest.mark.get_dniNumPart
def test_dniNumPart():  
    assert dni('49482728E').getDniNumPart() == '49482728'
    assert dni('494827288E').getDniNumPart() == False

@pytest.mark.dniLetterPart
def test_letterPart():
    assert dni('E').getDniletterPart() == 'E'
    assert dni('j').getDniletterPart() == 'J'

@pytest.mark.obtain_letter
def test_ObtainLetter():
    assert dni('49482728E').obtainLetter() == 'E'
    assert dni('78484464T').obtainLetter() == 'T'
    assert dni('26861694V').obtainLetter() == 'V'

@pytest.mark.comparingLetter
def test_comparingLetter():
    assert dni('49482728E').comparingLetter() == 'Data is Correct'
    assert dni('49482728L').comparingLetter() == 'Incorrect letter of DNI'