class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None 
class Lista:
    def __init__(self):
        self.head = None
    def inserir_inicio(self,valor):
        novo_no = No(valor)
        novo_no.proximo = self.head
        self.head = novo_no
    def remover_no(self):
        if self.head is None:
            print("lista vazia")
        else:
            self.head = self.head.proximo
    def imprimir(self):
        atual = self.head
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


lista = Lista()


lista.inserir_inicio(50)
lista.inserir_inicio(10)
lista.inserir_inicio(50)
lista.inserir_inicio(10)
lista.remover_no()


lista.imprimir()