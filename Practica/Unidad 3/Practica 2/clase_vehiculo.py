import abc
from abc import ABC

class vehiculo(ABC):
    __marca:str
    __modelo:str
    __anio_fabri:int
    __capacidad:int
    __num_plazas:int
    __distancia:float
    __tarifa_base:float
    
    def __init__(self, marca, modelo, anio, capacidad, num, distancia, tarifa):
        self.__marca=marca
        self.__modelo=modelo
        self.__anio_fabri=anio
        self.__capacidad=capacidad
        self.__num_plazas=num
        self.__distancia=distancia
        self.__tarifa_base=float(tarifa)
    
    def dar_tarifa(self):
        return self.__tarifa_base
    def dar_modelo(self):
        return self.__modelo
    def dar_anio(self):
        return self.__anio_fabri
    def dar_capacidad(self):
        return self.__capacidad
    
    @abc.abstractmethod
    def calcular_tarifa(self):
        pass