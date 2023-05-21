from calculatorop import CalculatorOp

class UserInt:
        #ask the user for the given.
    def firstNumberInput (self):
        while True:
            try:
                self.firstNumber = float( input("\n\33[96mPlease enter your first number.\33[96m"))
                return self.firstNumber
            except ValueError:
                print("Numbers Only or Check your typings to avoid errors! ")

    def secondNumberInput(self):
        while True:
            try:
                self.secondNumber = float(
                    input("\n\33[90mPlease enter your second number. "))
                return self.secondNumber
            except ValueError:
                print("Numbers Only or Check your typings to avoid errors! ")

    def performOperation(self, chosen_Operation, username):
        calculate = CalculatorOp()

        if chosen_Operation == "1":
            summ = calculate.add(self.firstNumber, self.secondNumber)
            print(f"Hey {username}, the sum is {summ}")
        elif chosen_Operation == "2":
            difference = calculate.subtract(
                self.firstNumber, self.secondNumber)
            print(f"Hey {username}, the difference is {difference}")
        elif chosen_Operation == "3":
            product = calculate.multiply(self.firstNumber, self.secondNumber)
            print(f"Hey {username}, the product is {product}")
        elif chosen_Operation == "4":
            quotient = calculate.divide(self.firstNumber, self.secondNumber)
            print(f"Hey {username}, the quotient is {quotient}")
        else:
            raise ValueError        