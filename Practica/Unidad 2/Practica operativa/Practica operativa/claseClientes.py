class cliente:
    __nom=str
    __ape=str
    __dni=int
    __num_cuenta=int
    __saldo_anterior=float
    
    def __init__(self, nom, ape, dni, num, saldo):
        self.__nom=nom
        self.__ape=ape
        self.__dni=dni
        self.__num_cuenta=num
        self.__saldo_anterior=saldo
        
        
    def dar_nom(self):
        return self.__nom
    def dar_ape(self):
        return self.__ape
    def dar_dni(self):
        return int(self.__dni)
    def dar_numcuenta(self):
        return int(self.__num_cuenta)
    def dar_saldo(self):
        return float(self.__saldo_anterior)
        
    def mostrar_datos(self):
        print(f'''Cliente: {self.__ape}, {self.__nom}           Numero de cuenta: {self.__num_cuenta}           Saldo anterior: {self.__saldo_anterior}''')
        
    def modif_saldo(self, saldo):
        self.__saldo_anterior=saldo
    