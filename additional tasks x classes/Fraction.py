class Fraction:
    # numerator: int
    value = 0
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        print(str(self.numerator) + ' | ' + str(self.denominator))

    def calculateSum(self):
        sum = self.makeSum(self.numerator, self.denominator)
        print("Sum : " + str(sum))
    pass

    @staticmethod
    def makeSum(numerator, denominator):
        return numerator + denominator
    
    def showDifference(self):
        difference = self.numerator - self.denominator
        print("Difference : " + str(difference))
    pass

    def showProduct(self):
        product = self.numerator * self.denominator
        print("Product : " + str(product))
    pass

    def showDivide(self):
        divide = self.numerator / self.denominator
        print("Divide : " + str(divide))
    pass

print("Input denominator: ")
newDenominator = int(input())
print("Input nomerator: ")
newNumerator = int(input())
f = Fraction(newNumerator, newDenominator)
f.calculateSum()
f.showDifference()
f.showProduct()
f.showDivide()
