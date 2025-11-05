import os
import math
class Calculadora():
    def __init__(self, n1=0, n2=0, base=0):
        self.n1 = n1
        self.n2 = n2
        self.base = base
    
    def DefinirNumeros(self):
        self.n1 = float(input('Digite o primeiro numero: '))
        self.n2 = float(input('Digite o segundo numero: '))

    def MostrarNumeros(self):
        print(f'Numeros escolhidos: \n\nn1 = {self.n1} \nn2 = {self.n2}\n---------------')
        
    def Somar(self):
        self.soma = self.n1 + self.n2
        return f'A soma dos numeros {self.n1} e {self.n2} é {self.soma}'
    
    def Subtrair(self):
        self.subtracao = self.n1 - self.n2
        self.subtracao2 = self.n2 - self.n1
        return f'Subtração:\n{self.n1} - {self.n2} = {self.subtracao} \n{self.n2} - {self.n1} = {self.subtracao2}'
    
    def Multiplicar(self):
        self.multiplicacao = self.n1 * self.n2
        return f'Multiplicação:\n{self.n1} x {self.n2} = {self.multiplicacao}'

    def Dividir(self):
        self.divisao = self.n1 / self.n2
        self.divisao2 = self.n2 / self.n1
        return f'Divisão:\n{self.n1} / {self.n2} = {self.divisao:.2f} \n{self.n2} / {self.n1} = {self.divisao2:.2f}'

    def Potenciacao2(self):
        self.Potenciacao21 = self.n1 ** 2
        self.Potenciacao22 = self.n2 ** 2
        return f'{self.n1} ^ 2 = {self.Potenciacao21} \n{self.n2} ^ 2 = {self.Potenciacao22}'
    
    def Potenciacao3(self):
        self.Potenciacao31 = self.n1 ** 3
        self.Potenciacao32 = self.n2 ** 3
        return f'{self.n1} ^ 3 = {self.Potenciacao31} \n{self.n2} ^ 3 = {self.Potenciacao32}'
    
    def RaizQuadrada(self):
        self.rq1 = math.sqrt(self.n1)
        self.rq2 = math.sqrt(self.n2)
        rq1Inteira = self.rq1.is_integer()
        rq2Inteira = self.rq2.is_integer()
        if rq1Inteira == False and rq2Inteira == False: 
            return f'As raizes quadradas dos numeros {self.n1} e {self.n2} não são exatas \ntendo valor inteiro de {self.rq1:.2f} para o numero {self.n1} e de {self.rq2:.2f} para o numero {self.n2}'
        elif rq1Inteira == False and rq2Inteira == True:
            return f'A raiz quadrada do numero {self.n1} não é exata, tendo valor inteiro de {self.rq1:.2f} \nmas o numero {self.n2} tem raiz quadrada exata tendo o valor de {self.rq2}'
        elif rq2Inteira == False and rq1Inteira == True:
            return f'A raiz quadrada do numero {self.n2} não é exata, tendo valor inteiro de {self.rq2:.2f} \nmas o numero {self.n1} tem raiz quadrada exata tendo o valor de {self.rq1}'
        else:
            return f'√n1 = {self.rq1:.2f} \n√n2 = {self.rq2:.2f}'
    
    def Logaritmo(self):
        self.base = int(input('Escolha a base do seu logaritmo: '))
        self.logn1 = math.log(self.n1, self.base)
        self.logn2 = math.log(self.n2, self.base)
        return f'Log n1 = {self.logn1:.2f} \nLog n2 = {self.logn2:.2f}'
    
    def MaioreMenor(self):
        self.maior = max(self.n1, self.n2)
        self.menor = min(self.n1, self.n2)
        if self.n1 == self.n2:
            return 'Os numeros são iguais'
        else:
            return f'O numero {self.maior} é maior do que o numero {self.menor}'
    
    def PotenciacaoEntreOsNumeros(self):
        self.pown1 = pow(self.n1, self.n2)
        self.pown2 = pow(self.n2, self.n1)
        return f'{self.n1}^{self.n2} = {self.pown1}  \n {self.n2}^{self.n1} = {self.pown2}'

calc = Calculadora()
calc.DefinirNumeros()
calc.MostrarNumeros()   
opcao = int(input('''
             =-=-Calculadora-=-=
            [ 1 ] Somar
            [ 2 ] Subtrair
            [ 3 ] Multiplicar
            [ 4 ] Dividir
            [ 5 ] Potenciação Quadrática
            [ 6 ] Potenciação Cúbica
            [ 7 ] Raiz quadrada
            [ 8 ] Logaritmo
            [ 9 ] Comparar os Numeros
            [ 10 ] Potenciação entre os numeros
                  
Qual operação deseja executar? 
'''))
os.system('cls')
match opcao:

    case 1:
        print(calc.Somar())
    case 2:
        print(calc.Subtrair())
    case 3:
        print(calc.Multiplicar())
    case 4:
        print(calc.Dividir())
    case 5:
        print(calc.Potenciacao2())
    case 6:
        print(calc.Potenciacao3())
    case 7:
        print(calc.RaizQuadrada())
    case 8:
        print(calc.Logaritmo())
    case 9:
        print(calc.MaioreMenor())
    case 10:
        print(calc.PotenciacaoEntreOsNumeros())
