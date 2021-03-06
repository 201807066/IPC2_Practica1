from TDA_Cola.nodo import Nodo

class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def empty(self):
        return self.primero == None

    def push(self, ingrediente):
        if self.empty():
            self.primero = self.ultimo = Nodo(ingrediente)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(ingrediente)

    def show(self):
        aux = self.primero
        if self.empty():
            print("No hay pedidos pendientes en Pizza Family")
        else:
            while aux != None:
                print("Pizza con ingrediente -> "+ aux.ingrediente + "\n")
                aux = aux.siguiente

    def firstOrder(self):
        aux = self.primero
        if self.empty():
            print("No hay pedidos pendientes en Pizza Family")
        else:
            print("Pizza con ingrediente -> "+ aux.ingrediente)

    def pop(self):
        if self.empty():
            print("No hay ordenes agregados en la cola...")
        else:
            self.primero = self.primero.siguiente
            input("Orden entregado con exito...")