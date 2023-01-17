from src.assignmentTable import *

class dni:
    
    def __init__(self, dni=""):
        self.numLetter = dni
        self.correctNumber = False
        self.correctLetter = False
        self.table = assignment_table()
        
    def setDni(self, dni):
        self.numLetter = dni
        
    #check the lenght of the DNI with letter
    
    def checkDniLen(self):
        return len(self.numLetter) == 9
  
    ### CHECKING DNI,NUMERIC PART ###
                                
    def checkNumber(self):
        return self.numLetter[:-1].isdigit()
    
    #writing a method for reasign later

    def setNumber(self, value):
        self.correctNumber = value 
    
    def getCorrectNumber(self):
        return self.correctNumber
    
    #getting the numbers of dni
     
    def getDniNumbers(self):
        if self.getCorrectNumber():
            return self.numLetter[:-1]
        return False
    
    #if the previous methods are complished we called the dni with letter
    
    def getDni(self):
        return self.numLetter
    
    #if the total length of the dni is 9 and the dni without letter are numbers

    def checkDni(self):
        self.setNumber(self.checkDniLen() and self.checkNumber())
        return self.getCorrectNumber()
    
    ### CHECKING LETTER ###
    
    #writing a method for reasign later
    
    def setCorrectLetter(self, value):
        self.correctLetter = value
        
    def getCorrectLetter(self):
        return self.correctLetter
    
    #taking the letter of dni
    
    def getDniLetter(self):
        return self.numLetter[-1].isupper()
    
    #the dni num is correct then we call the class assignment_table we calculate the letter
    #we give the argument calling
    
    def letterFromTable(self):
        if self.getCorrectNumber():
            return self.table.calculatingLetter(self.getDniNumbers())
        return False
    
    #if the letter given si equal to that one that was calculated
    
    def checkValidLetter(self):
        if self.getCorrectNumber():
            return self.getDniLetter() == self.letterFromTable()
        return False
    
    #check if the letter in dni is a letter and the letter given is correct
    
    def checkLetter(self):
        if self.getCorrectNumber():
            self.setCorrectLetter(self.getDniLetter().isalpha() and self.checkValidLetter())
            return self.getCorrectLetter
        else:
            return False
        
    ### THIS PART IT'S EXECUTED IF THE PREVIOUS PARTS ARE CORRECT ##
    
    def checkDocument(self):
        return self.checkDni() and self.checkLetter()