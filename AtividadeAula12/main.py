import random

from Estruturas.listaEncadeada.LinkedList import LinkedList

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    def getNome(self):
        return self._nome
    def getEndereco(self):
        return self._endereco
    def getTelefone(self):
        return self._telefone



class Josephus:
    def __init__(self):
        self.lista = LinkedList()
        self.listaName = LinkedList()
        self.listaEndereco = LinkedList()
        self.listaTelefone = LinkedList()
        self.current = None

        nomes = "Ana/Bruno/Carlos/Diana/Eduardo/Fernanda/Gustavo/Helena/Igor/Joana/Kevin/Larissa/Marcelo/Natalia/Oscar/Patricia/Quintino/Rafaela/Sergio/Tatiana"
        telefones = "999-111-2222/888-333-4444/777-555-6666/666-444-3333/555-222-1111/111-333-5555/444-666-8888/222-999-7777/333-111-8888/555-444-2222/999-777-3333/888-666-1111/333-555-9999/222-444-7777/777-888-2222/111-666-4444/444-333-5555/555-999-1111/666-222-8888/888-777-6666"
        enderecos = "Rua A, 123/Avenida B, 456/Rua C, 789/Avenida D, 321/Rua E, 654/Avenida F, 987/Rua G, 159/Avenida H, 753/Rua I, 246/Avenida J, 864/Rua K, 357/Avenida L, 951/Rua M, 468/Avenida N, 753/Rua O, 159/Avenida P, 357/Rua Q, 864/Avenida R, 468/Rua S, 753/Avenida T, 951"

        nomes = nomes.split('/')
        telefones = telefones.split('/')
        enderecos = enderecos.split('/')

        for x in range(0, len(nomes)):
            self.listaName.insert(x, nomes[x])
            self.listaEndereco.insert(x, enderecos[x])
            self.listaTelefone.insert(x, telefones[x])
        self.lista.insert(0, 'Pessoa sobrevivente: ')
        for x in range(0,21):
            if x != 0:
                self.lista.insert(x,Pessoa(self.listaName[x-1],self.listaEndereco[x-1],self.listaTelefone[x-1]))

    def processar(self,sorteado):
        sorteado = self.lista[sorteado]
        print(sorteado.getNome())
        print(sorteado.getTelefone())
        print(sorteado.getEndereco())


jose = Josephus()
resultado = random.randint(1,21)
jose.processar(resultado)