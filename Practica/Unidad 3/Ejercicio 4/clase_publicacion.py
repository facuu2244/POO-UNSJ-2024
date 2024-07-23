import abc
from abc import ABC

class publicacion(ABC):
    __titulo:str
    __categoria:str
    __precio_base:float
    __fecha_actual=2024
    def __init__(self, titulo, cate, precio):
        self.__titulo=titulo
        self.__categoria=cate
        self.__precio_base=float(precio)

    def dar_titulo(self):
        return self.__titulo
    def dar_categoria(self):
        return self.__categoria
    def dar_precio_base(self):
        return self.__precio_base
    def dar_fecha(self):
        return self.__fecha_actual
    
    @abc.abstractmethod
    def mostrar_publi():
        pass

    # def mostrar_publi(self, fecha=None): #Muestra la publicacion y calcula el importe de venta
    #     imp_venta:float
    #     if fecha!=None: #significa que es un libro
    #         porc_descuento=self.__fecha_actual-fecha
    #         imp_venta=(porc_descuento*self.__precio_base)/100
        
    #     else: #es un cd
    #         imp_venta =self.__precio_base*1.1
            
    #     print(f"{self.__titulo}, {self.__categoria}, {imp_venta:.2f}")
    