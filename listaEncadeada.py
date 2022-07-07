class NodoLista:

    def __init__(self,dado=0,proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    
def inserir_no_inicio(lista,novo_dado):

        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = lista.cabeca
        lista.cabeca = novo_nodo

def inserir_depois(lista,nodo_anterior,novo_dado):
    pass


lista = ListaEncadeada()
print("Lista vazia: ", lista)

inserir_no_inicio(lista,5)
inserir_no_inicio(lista,10)

print(lista)
