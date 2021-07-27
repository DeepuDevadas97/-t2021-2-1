class Calculator():
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def addition(self):
        return self.a+self.b

    def subtraction(self):
        return self.a-self.b
    
    def multiplication(self):
        return self.a*self.b
    
    def division(self):
        return self.a/self.b
    
    
repeat = 1
while repeat != 0:

    print("_____________________CALCULATOR_______________________________")
    
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))

    obj=Calculator(a,b)
    
    operator = input("Enter type of operation [+] [-] [*] [/] : ")
    
    if operator == "+":
        print("Result : ",obj.addition())
        
    elif operator == "-":
        print("Result : ",obj.subtraction())
        
    elif operator == "*":
        print("Result : ",obj.multiplication())
        
    elif operator == "/":
        print("Result : ",obj.division())
        
    else:
        print("Invalid Operator !!")
 
