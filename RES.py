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
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no


    def imprimir(self):
        atual = self.head
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo



lista = Lista()

lista.inserir_no_final(50)
lista.inserir_no_final(10)


lista.imprimir()


        