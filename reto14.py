class Armstrong():
    def __init__(self):
        self.suma = 0

    def esArmstrong(self,num):
        lst = map(lambda i: int(i) ** len(str(num)), (list(str(num))))
        for i in lst:
            self.suma += i
        return self.suma == num


num1 = Armstrong()
print(num1.esArmstrong(153))