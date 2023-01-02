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
            return self.number + Letter.get_dni_letter(self)
        return 'Insert DNI again'
#This is an heritance from the previous class dni,the next class will contain all the functions from his father and also we can 
#invocate them and add new attributes or variables to make new parameters.
class Letter(dni):
#in this line we call function __init__ from the class dni and this return us the parameters inside.If we write 'def'automatically the function is called     
    def __init__(self, number):
        dni.__init__(self, number)

    def get_dni_letter(self):
        
        calculatePositionInTable = int(self.number) % len(self.assignment_table)
        assignedLetter = self.assignment_table[calculatePositionInTable]
            
        return assignedLetter
      