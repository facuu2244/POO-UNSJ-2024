import numpy as np
import csv
class cuenta:
    __nya=str
    __dni=int
    __tel=int
    __saldo=float
    __cvu=int
    __porc_aumento=68
    
    def __init__(self, nya, dni, tel, saldo, cvu):
        self.__nya=nya
        self.__dni=int(dni)
        self.__tel=tel
        self.__saldo=float(saldo)
        self.__cvu=cvu
        
    def __str__(self) -> str:
        return f"{self.__nya} {self.__cvu} {self.__saldo}"
    
    def dar_dni(self):
        return self.__dni
    def dar_cvu(self):
        return self.__cvu
    
    def actualizar_saldo(self, nuevo_saldo):
        self.__saldo=self.__saldo-nuevo_saldo    
    
    def mostrar(self):
        print(f"{self.__nya}  {self.__dni}  {self.__tel}")
        
    @classmethod
    def cambiar_rendi(cls, porc):
        cls.__porc_aumento=porc
        print(f"Porcentaje de rendimiento anual actualizado a: {cls.__porc_aumento}")
    @classmethod
    def rendi_diario(cls):
        return cls.__porc_aumento/365
    
class gestor_cuenta:
    __gestor:np.array
    
    def __init__(self):
        self.__gestor=np.array([])
        
    def __str__(self):
        for cuenta in self.__gestor:
            cuenta.mostrar()
            
    
    def cargar(self, ruta_cuentas):
        with open(ruta_cuentas, "r") as archi_cuenta:
            reader=csv.reader(archi_cuenta)
            next(reader)
        
            for fila in reader:
                nya, dni, tel, saldo, cvu = fila 
                una_cuenta=cuenta(nya, dni, tel, saldo, cvu)
                self.__gestor = np.append(self.__gestor,una_cuenta)
                
    def buscar_cvu(self, cliente):
        band=False
        i=0
        cvu=None
        while band==False and i<len(self.__gestor):
            if cliente==self.__gestor[i].dar_dni():
                band=True
                cvu=self.__gestor[i].dar_cvu()
            i+=1
        return cvu
    
    def mostrar_cliente(self, cliente, nuevo_saldo):
        band=False
        i=0
        while band==False and i<len(self.__gestor):
            if cliente==self.__gestor[i].dar_dni():
                band=True
                self.__gestor[i].actualizar_saldo(nuevo_saldo)
                return print(self.__gestor[i])
            i+=1