class jugador:
    __nombre:str
    __puntos:int
    __fecha:str
    __hora:str
    
    def __init__(self, nom, puntos, fecha, hora):
        self.__nombre=nom
        self.__puntos=puntos
        self.__fecha=fecha
        self.__hora=hora
        
    def __gt__(self, otro):
        if self.__puntos>otro.dar_puntos():
            return True
    
    def dar_puntos(self):
        return self.__puntos
    
    def listar(self):
        return f"       {self.__nombre}             {self.__fecha}             {self.__hora}                {self.__puntos}"