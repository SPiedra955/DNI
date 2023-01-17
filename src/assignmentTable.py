class assignment_table:
    
    def __init__(self):
        self.table = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
					   'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]  
#Encapsulation   
    def getLetter(self, position):      
        try:
            return self.table[position]
        except:
            return 'Letter out of range'       
#Every method have is responsability   
    def getDividend(self):
        try:
            return len(self.table)
        except:
            if len(self.table) != 23:
                return 'Check table'
    
    def calculatingLetter(self, DNI):
        try:
            position = int(DNI) % len(self.table)
            return self.getLetter(position)
        except:
            if type(DNI) != int:
                return 'DNI must be integers'