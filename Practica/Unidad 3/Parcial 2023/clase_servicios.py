import abc
from abc import ABC

class servicio(ABC):
    __empresa:str
    __contratante:str
    __direc:str
    __fecha:str    
    
    def __init__(self, empresa, contratante, direc, fecha) :
        self.__empresa=empresa
        self.__contratante=contratante
        self.__direc=direc
        self.__fecha=fecha
        
    def dar_contratante(self):
        return self.__contratante
    def dar_fecha(self):
        return self.__fecha
        
    @abc.abstractmethod
    def costo(self):
        pass