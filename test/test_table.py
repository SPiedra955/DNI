from src.assignmentTable import assignment_table
import pytest

@pytest.mark.testGetLetter
def test_get_letter():
    assert assignment_table().getLetter(22) == "E"
    assert assignment_table().getLetter(10) == "X"
    assert assignment_table().getLetter(21) == "K"
    assert assignment_table().getLetter(23) == 'Letter out of range'
    assert assignment_table().getLetter(31) == 'Letter out of range'
    assert assignment_table().getLetter(28) == 'Letter out of range'
    
@pytest.mark.testGetDividend
def test_get_dividend():
    assert assignment_table().getDividend() == 23
    assert assignment_table().getDividend() != 'Check table' 

@pytest.mark.testCalculatingLetter
def test_calculating_letter():
    assert assignment_table().calculatingLetter('49482728') == 'E'
    assert assignment_table().calculatingLetter('49482727') == 'K'
    assert assignment_table().calculatingLetter('52548265') == 'G'   
    assert assignment_table().calculatingLetter('5//48/65') == 'DNI must be integers'
    assert assignment_table().calculatingLetter('*/)08/76') == 'DNI must be integers'
    assert assignment_table().calculatingLetter('3ç+]8/15') == 'DNI must be integers'