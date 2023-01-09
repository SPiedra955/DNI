class dni:

    def __init__(self, numberDni):
        self.number = numberDni
        self.validNumbersInDni = '0123456789'
        self.lenDniWithoutNumber = 8
        self.assignment_table = [ "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", 
                                  "N", "J" ,"Z" ,"S" ,"Q" ,"V" ,"H" ,"L" ,"C" ,"K" ,"E" ]
    
    def check_dni_number(self):
        for num in self.number:
            if num in self.validNumbersInDni and len(self.number) == self.lenDniWithoutNumber:
                return True
        return 'Check your DNI'
            
    def dni_set(self):
        if dni.check_dni_number(self) == True:
            return self.number + letter.get_dni_letter(self)
        return 'Insert DNI letter again'
#This is a son from class dni,from his son we can call each function inside his father, 
#We invocated the dni class and add attributes or variables to make new parameters.
class letter(dni):
    
    def __init__(self, number): #We called this function from class dni
        dni.__init__(self, number)

    def get_dni_letter(self):
        
        calculatePositionInTable = int(self.number) % len(self.assignment_table)
        assignedLetter = self.assignment_table[calculatePositionInTable]
            
        return assignedLetter
      