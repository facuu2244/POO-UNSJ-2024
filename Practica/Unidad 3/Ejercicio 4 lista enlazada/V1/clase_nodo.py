class nodo:
    __publicacion:object
    __siguiente:object
    
    def __init__(self, publi):
        self.__publicacion=publi    
        
    def set_siguiente(self, siguiente): #Recibe un nodo como parametro
        self.__siguiente=siguiente
        
    def dar_siguiente(self):
        return self.__siguiente
    def dar_publicacion(self):
        return self.__publicacion