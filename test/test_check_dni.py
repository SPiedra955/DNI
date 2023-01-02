from src.dni_letter_assignment import *
import pytest 

@pytest.mark.dni_is_correct
def test_dni_is_correct():
    assert True == dni('49482728').check_dni_number()
    assert True == dni('49482727').check_dni_number()
    assert True == dni('52548265').check_dni_number()
    assert 'Check your DNI'== dni('48?48@/?¿').check_dni_number()
    assert 'Check your DNI' == dni('494827288').check_dni_number()
  
@pytest.mark.letter_correct_dni
def test_letter_correct_dni():
    assert 'E' == getLetter('49482728').get_dni_letter()
    assert 'K' == getLetter('49482727').get_dni_letter()
    assert 'G' == getLetter('52548265').get_dni_letter()
    
@pytest.mark.dni_with_letter
def test_dni_with_letter():
    assert '49482728E' == dni('49482728').dni_set()
    assert '49482727K' == dni('49482727').dni_set()
    assert '52548265G'  == dni('52548265').dni_set()
    assert 'Insert DNI letter again' == dni('4855').dni_set()
    assert 'Insert DNI letter again' == dni('4hjfdfe/(').dni_set()