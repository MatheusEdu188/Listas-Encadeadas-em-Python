class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
class Lista:
    def __init__(self):
        self.head = None
    def inserir_no_final(self, valor):
        novo_no = No(valor)
        if self.head is None:
            novo_no.proximo = self.head
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
    def remover_nó_inicio(self):
        if self.head is None:
            print("Lista Vazia")
        else:
            self.head = self.head.proximo
    def imprimir(self):
        atual = self.head
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


lista = Lista()

lista.inserir_no_final(50)
lista.inserir_no_final(10)
lista.inserir_no_final(20)
lista.inserir_no_final(80)
lista.remover_nó_inicio()



lista.imprimir()