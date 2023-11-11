from sympy import *
init_printing(use_unicode=True)
from sympy import shape

class MyMatrix():
    def __init__(self, matrix):
        self.SymMatrix = Matrix(matrix)
        self.rref, self.pivots = self.SymMatrix.rref()

    def printOriginalMatrix(self):
        print("Printing original matrix...")
        self.printMatrix(self.SymMatrix)
    
    def printRREF(self):
        print("Printing RREF of your matrix...")
        self.printMatrix(self.rref)
        print("pivot columns are: " + str(self.pivots))

    def printMatrix(self, mx):
        numRow = mx.shape[0]
        numCol = mx.shape[1]
        rowstr = ""
        print("*" * numCol * 3)
        for i in range(numRow):
            for j in range(numCol):
              rowstr += " " + str(mx[i,j])
            if (i!=numRow-1):
                rowstr+="\n"
        print(rowstr)
        print("*" * numCol * 3)
    

# ============================================
# BEGIN MATRIX FUN! 
m = MyMatrix([[0,0,0],[1,1,1],[1,1,1]])
m.printMatrix(m.SymMatrix)
m.printOriginalMatrix()
m.printRREF()

# ============================================
