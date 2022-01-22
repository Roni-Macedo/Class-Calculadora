"""class Calculadora:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adicao(self):
        return self.x + self.y

    def subtracao(self):
        return self.x - self.y

    def multiplicacao(self):
        return self.x * self.y

    def divisao(self):
        return self.x / self.y

    def operacao(self, operador):

        if operador == "+":
            return self.adicao

        elif operador == "-":
            return self.subtracao

        elif operador == "*":
            return self.multiplicacao

        elif operador == "/":
            return self.divisao


while True:
    usuario_input = input("DIGITE SEU CALCULO >: ")
    usuario_input = usuario_input.strip().split(" ")

    try:
        numero_1 = int(usuario_input[0])
        numero_2 = int(usuario_input[2])
        op = usuario_input[1]

        calculadora = Calculadora(numero_1, numero_2)

        resultado = calculadora.operacao(op)
        print(resultado)

    except:
        print("CALCULO  INVALIDO ex: < 2 + 2 >")

    novo_calculo = input("DESEJA UM NOVO CALCULO? s/n >: ")

    if novo_calculo == "s":
        continue
    else:
        break"""


class Calculadora:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adicao(self):
        return self.x + self.y

    def subtracao(self):
        return self.x - self.y

    def multiplicacao(self):
        return self.x * self.y

    def divisao(self):
        return self.x / self.y

    def operacao(self, op):
        if op == '+':
            return self.adicao()
        elif op == '-':
            return self.subtracao()
        elif op == '*':
            return self.multiplicacao()
        elif op == '/':
            return self.divisao()


while True:
    usuario_input = input("\nDIGITE SEU CALCULO >: ")
    usuario_input = usuario_input.strip().split(" ")

    try:
        numero_1 = int(usuario_input[0])
        numero_2 = int(usuario_input[2])
        operador = usuario_input[1]

        if operador == "/" and numero_2 == 0:
            print("\nERRORs divisor / 0")

        calculadora = Calculadora(numero_1, numero_2)

        resultado = calculadora.operacao(operador)
        print("\n",resultado)
    except:
        print("\nCALCULO  INVALIDO ex: < 2 + 2 >")

    avancar_calculadora = input("\nDESEJA UM NOVO CALCULO? s/n >: ")
    if avancar_calculadora == 's':
        continue
    else:
        print("FIM")
        break
