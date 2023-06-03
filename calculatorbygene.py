from calculatorop import CalculatorOp
import math

class CalcModified(CalculatorOp):
    def squaringProduct (self, firstNum):
        return (firstNum ** 2)
    def sqrt (self, firstNum):
        return math.sqrt(firstNum)