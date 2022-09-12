class Factorial():
    def __init__(self):
        self.suma = 1
    
    def numeroFactorial(self, num):
        if num == 0:
            return 1
        else:
            for i in range(1,num+1,1):
                self.suma *= i
                if self.suma == num:
                    return i
            return "No tiene factorial"


numero1 = Factorial()
print(numero1.numeroFactorial(24))