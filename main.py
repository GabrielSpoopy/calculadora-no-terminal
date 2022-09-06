class Calculadora:
    def __init__(self):
        self.operacao = None
        self.n1 = None
        self.n2 = None
        self.resultado = None
    
    def soma(self):
        return self.n1 + self.n2
    def subtracao(self):
        return self.n1 - self.n2
    def multiplicacao(self):
        return self.n1 * self.n2
    def divisao(self):
        return self.n1 / self.n2

    def iniciar(self):
        print('Calculadora! \n')
        self.n1 = int(input('escolha um número: '))
        self.n2 = int(input('escolha outro número: '))
        print('\n')
        print('qual será o tipo de operacao? \n 1 - soma \n 2 - subtração \n 3 - multiplicação \n 4 - divisão \n')
        self.operacao = int(input(': '))
        self.ifOperacao()
        self.mostrarResultado()

    def ifOperacao(self):
        if self.operacao == 1:
            self.resultado = self.soma()
        elif self.operacao == 2:
            self.resultado = self.subtracao()
        elif self.operacao == 3:
            self.resultado = self.multiplicacao()
        elif self.operacao == 4:
            self.operacao == self.divisao()
        else:
            pass

    def mostrarResultado(self):
        print(f'o resultado foi {self.resultado}')

programa = Calculadora()
programa.iniciar()