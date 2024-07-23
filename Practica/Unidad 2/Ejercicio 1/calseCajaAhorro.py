class cajaDeAhorro:
    def __init__(self,__numcuenta, __nombre, __apellido, __cuil):
        self.__numcuenta=__numcuenta
        self.__cuil=__cuil
        self.__apellido=__apellido
        self.__nombre=__nombre
        self.__saldo=0
        
    def mostrar(self):
        print("Datos de la cuenta: \n")
        print("Numero de cuenta: ",self.__numcuenta)
        print("Nombre del titular: ",self.__nombre)
        print("Apellido del titular: ",self.__apellido)
        print("Cuil: ",self.__cuil)
        print("Saldo: ",self.__saldo)
        
    def extraer(self, monto):
        if monto<=self.__saldo:
            self.__saldo=self.__saldo - monto
            print("\nNuevo saldo: ", self.__saldo)
        
        else: 
            print("Saldo insuficiente\n")

    def depositar(self, depo):
        if depo<=0:
            print("Importe invalido\n")
        
        else:
            self.__saldo+=depo
            print("Saldo depositado, nuevo saldo: ", self.__saldo)
    
    def validar(self, cuil):
        if cuil==self.__cuil:
            print("El cuil es valido y coincide con el de la cuenta\n")
        
        else:
            print("Cuil invalido o no coincide con el de la cuenta\n")
