from src.assignmentTable import *

class dni:
    
    def __init__(self, dni=""):
        self.numLetter = dni
        self.correctNumber = False
        self.correctLetter = False
        self.table = assignment_table()
        
    def setDni(self, dni):
        self.numLetter = dni
    
    def getDni(self):
        return self.numLetter
    
    def setNumber(self, value):
        self.correctNumber = value 
    
    def getCorrectNumber(self):
        return self.correctNumber
    
    def setCorrectLetter(self, value):
        self.correctLetter = value
        
    def getCorrectLetter(self):
        return self.correctLetter
    
    def checkDocument(self):
        return self.checkDni() and self.checkLetter()
    
    def checkDni(self):
        self.setNumber(self.checkDniLen() and self.checkNumber())
        return self.getCorrectNumber()
    
    def checkLetter(self):
        if self.getCorrectNumber():
            self.setCorrectLetter(self.getDniLetter() and not 
                                  self.getDniLetter().isdigit() and self.checkValidLetter())
            return self.getCorrectLetter
        else:
            return False
    
    def letterFromTable(self):
        if self.getCorrectNumber():
            return self.table.calculatingLetter(self.getDniNumbers())
        return False
                    
    def checkDniLen(self):
        return len(self.numLetter) == 9
    
    def checkNumber(self):
        return self.numLetter[:-1].isdigit()
    
    def checkValidLetter(self):
        if self.getCorrectNumber():
            return self.getDniLetter() == self.letterFromTable()
        return False
    
    def getDniLetter(self):
        return self.numLetter[-1].isupper()
    
    def getDniNumbers(self):
        if self.getCorrectNumber():
            return self.numLetter[:-1]
        return False