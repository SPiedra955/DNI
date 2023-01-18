from src.assignmentTable import *

class dni:
    
    def __init__(self, document=""):
        self.dni = document
        self.correctNumber = False
        self.correcLetter = False
        self.table = assignment_table()
        
    def setDni(self, document):
        self.dni = document

    def checkLength(self):
        if len(self.dni) == 9:
            return 'Checking DNI given'
        else:
            return False
    
    def checkNum(self):
        if self.dni[:-1].isdigit():
            return True
        else:
            return 'DNI must contain numbers'
 
    def checkDniLetter(self):
        if self.dni[-1].isalpha():
            return 'Checking DNI letter'
        else:
            return 'DNI last character must be a letter'     
    
    def checkLenDniNums(self):
        return len(self.dni[:-1]) == 8
    
    def correctDniNum(self):
        if self.checkNum and self.checkLenDniNums:
            return "Checking if letter it's correct"
        
    def getDniNumPart(self):
        if self.correctDniNum():
            return self.dni[:-1]

    def getDniletterPart(self):
        if self.checkDniLetter():
            return self.dni[-1].upper()
        
    def obtainLetter(self):    
        return self.table.calculatingLetter(self.getDniNumPart())
    
    def comparingLetter(self):    
        if self.obtainLetter() == self.getDniletterPart():
            return 'Data is correct'
        else:
            return 'Check DNI'
        