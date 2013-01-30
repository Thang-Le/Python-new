class calculate(object):
    
    def __init__(self,number1,number2,):
        self.number1 = number1
        self.number2 = number2
    def display(self):
<<<<<<< HEAD
        answer = str(input("enter Operation:"))
        elif(str(answer) == 'add'):
=======
        answer = input("enter Operation:")
        if(str(answer) == 'add'):
>>>>>>> new update
            total = float(self.number1)+float(self.number2)
        elif(str(answer) == 'subtract'):
            total = float(self.number1)-float(self.number2)
        elif(str(answer)== 'multiply'):
            total = float(self.number1)*float(self.number2)
        elif(str(answer)== 'divide'):
<<<<<<< HEAD
            if(self.number2 == 0):
                print("WARNING")
            else:
                total = float(self.number1)/float(self.number2)
=======
            total = float(self.number1)/float(self.number2)
>>>>>>> new update
        else: print ("wrong ope")
        return total
