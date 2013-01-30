import calculator
import mess
from tkinter import *

<<<<<<< HEAD
print("enter numders that you want to combine")
so1 = input("first number")
so2 = input("second number")
cal = calculator.calculate(so1,so2)
calcifer = cal.display()
mess.mss(calcifer)
=======
done = True
while done == True:
    print("enter numders that you want to combine")
    so1 = input("first number")
    so2 = input("second number")
    cal = calculator.calculate(so1,so2)
    total = cal.display()
    mess.mss(total)
    answer = input("Do you want to calcifer again LOL: y/n")
    if(str(answer)=='y'):
        done = True
    else: done = False
>>>>>>> new update

