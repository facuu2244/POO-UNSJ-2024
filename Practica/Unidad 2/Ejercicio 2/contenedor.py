from claseCajaAhorro import cajaDeAhorro

class contenedor:
    __lista=list
    
    def __init__(self):
        self.__lista=[]
        
    def cargar(self):
        for i in range(2):
            print("Datos caja ", i+1)
            numcaja=i+1
            nombre=input("Ingrese nombre del titular: ")
            ape=input("Apellido: ")
            cuil=input("Ingrese ciul:")
            caja=cajaDeAhorro(numcaja, nombre, ape, cuil)
            self.__lista.append(caja)