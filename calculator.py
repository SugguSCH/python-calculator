class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        #error change b - a to a - b
        return a - b

    def multiply(self, a, b):
        #change result 1 to 0
        result = 0
        # add condition to check b
        if b < 0:
            for i in range(abs(b)):
                result = self.add(result, a)
            # change result to negative
            result = -result
        else :
            for i in range(b):
                result = self.add(result, a)
        return result
    
    def divide(self, a, b):
        result = 0
        #add condition to check negative number
        if b > 0:
            if a < 0:
                a = abs(a)
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
                result = -result
            else:
                while a >= b:
                    a = self.subtract(a, b)
                    result += 1
        else:
            b = abs(b)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            result = -result
        return result
    
    def modulo(self, a, b):
        #add condition to check negative number
        if b > 0:
            if a < 0:
                a = abs(a)
            while a >= b:
                a = a-b
            return a
        else :
            b = abs(b)
            a = abs(a)
            while a >= b:
                a = a-b
            return -a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))