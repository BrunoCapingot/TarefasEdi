from pilha.Stack import Stack


class Calculadora():
    def __init__(self):
        self.pilhaExpressoes = Stack()
        self.pilhaOperadores = Stack()
        self.pilhaValores = Stack()


    def infixaTransPosFixa(self):


        while True:
            comand = input('Insira os numeros e depois uma operação: ')
            if comand == '69':
                break
            else:
                for c in comand:

                    self.pilhaExpressoes.push(comand)
                    self.pilhaExpressoes.push('exp')

                print(self.pilhaExpressoes)



    def defineTypeOperation(self, notacao):
        if 'infixa' == notacao:
            print('Type: ' + notacao)

        elif 'pos-fixa' == notacao:
            print('Type: ' + notacao)
            self.infixaTransPosFixa()

        elif 'pre-fixa' == notacao:
            print('Type: ' + notacao)


calc = Calculadora()
#calc.defineTypeOperation('(4 + 3) * 9', 'infixa')
calc.defineTypeOperation('pos-fixa')
#calc.defineTypeOperation('(4 + 3) * 9', 'pre-fixa')
