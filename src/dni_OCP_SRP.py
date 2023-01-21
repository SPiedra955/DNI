from src.assignmentTable import *

class dni:
    
    def __init__(self, document=""):
        self.dni = document
        self.table = assignment_table()
        
    def setDni(self, document):
        self.dni = document

    def checkLenDni(self):
        if len(self.dni) == 9:
            return 'Checking DNI given'
        else:
            return False
    
    def checkNum(self):
        if self.dni[:-1].isdigit():
            return True
        else:
            return  False
 
    def checkDniLetter(self):
        if self.dni[-1].isalpha():
            return 'Checking DNI letter'
        else:
            return 'DNI last character must be a letter'     
    
    def checkLenDniNums(self):
        if len(self.dni[:-1]) == 8:
            return True
        return 'DNI must contain 8 digits and 1 letter'
    
    
    def correctDniNum(self):
        if self.checkNum() == self.checkLenDniNums():
            return True
        
    def getDniNumPart(self):
        if self.correctDniNum() == True:
            return self.dni[:-1]
        return False

    def getDniletterPart(self):
        if self.checkDniLetter():
            return self.dni[-1].upper()
        
    def obtainLetter(self):    
        return self.table.calculatingLetter(self.getDniNumPart())
    
    def comparingLetter(self):
        if self.obtainLetter() == self.getDniletterPart():
            return 'Data is Correct'
        return 'Incorrect letter of DNI'