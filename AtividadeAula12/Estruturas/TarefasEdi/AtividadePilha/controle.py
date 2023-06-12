from pilha.Stack import Stack


class Tarefa():
    def __init__(self):
        self.pilha = Stack()

    def inverteFrase(self, frase):
        for x in frase:
            for k in x:
                self.pilha.push(k)
        print(self.pilha)


dataList = ['UM CIENTISTA DA COMPUTAÇAO DEVE RESOLVER OS PROBLEMAS LOGICAMENTE',
            'ESARF ATERCES ODALERAHCAB ME AICNEIC AD OAÇATUPMOC FI ONAIOG SUPMAC SOHNIRROM HE MU SOD SEROHLEM SOSRUC ED OAÇATUPMOC OD ODATSE ED SAIOG'
            ]

trf = Tarefa()
for x in dataList:
    trf.inverteFrase(x)
