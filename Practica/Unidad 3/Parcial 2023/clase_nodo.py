class nodo:
    __servicio:object
    __siguiente:object
    
    def __init__(self, servicio):
        self.__servicio=servicio
        
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
        
    def dar_servicio(self):
        return self.__servicio
    def dar_siguiente(self):
        return self.__siguiente