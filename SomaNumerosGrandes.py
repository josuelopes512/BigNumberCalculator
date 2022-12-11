class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class BigNumberCalculator:
    def __init__(self):
        self.queue = Queue()
        self.stack = Stack()
    
    def multiply(self, number1, multiplier):
        i = 0
        result = number1
        
        while(i < int(multiplier)-1):
            result = self.add(number1, result)
            i += 1
        
        return result

    def add(self, number1, number2):
        result = ""

        # Converter os números para listas de dígitos
        digits1 = list(number1)
        digits2 = list(number2)

        # Adicionar zeros ao início da lista de dígitos mais curta
        # para garantir que ambas as listas tenham o mesmo tamanho
        if len(digits1) < len(digits2):
            digits1 = ["0"] * (len(digits2) - len(digits1)) + digits1
        elif len(digits1) > len(digits2):
            digits2 = ["0"] * (len(digits1) - len(digits2)) + digits2

        carry = 0
        for i in range(len(digits1) - 1, -1, -1):
            digit1 = int(digits1[i])
            digit2 = int(digits2[i])
            sum = digit1 + digit2 + carry

            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0

            result = str(sum) + result

        if carry == 1:
            result = "1" + result

        return result


if __name__ == '__main__':
    # Criar uma nova calculadora de números grandes
    calculator = BigNumberCalculator()

    # Adicionar dois números muito grandes
    result = calculator.add("12345678901234567890", "98765432109876543210")

    # # Exibir o resultado
    print(result)  # 111111111111111111100
    
    # calculator = BigNumberCalculator()
    
    # result = calculator.multiply("12345678901234567890", "3")

    # print(result) # 37037036703703703670

