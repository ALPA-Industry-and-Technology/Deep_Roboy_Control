class ComplexNumber:
    def __init__(self,r = 0, i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

    def compute_data(self, a, b):
        self.d = a + b

    def do_add(self):
        self.add = self.real + self.imag 
        self.compute_data(3,10) 
        print(self.d)

c1 = ComplexNumber(2,3)

c1.do_add()