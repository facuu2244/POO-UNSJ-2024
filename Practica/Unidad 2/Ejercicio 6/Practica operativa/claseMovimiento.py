class movimiento: 
    __num_cuenta=int
    __fecha=str
    __descr=str
    __tipo=str
    __importe=float
    
    def __init__(self, num, fecha, desc, tipo, imp):
        self.__num_cuenta=num
        self.__fecha=fecha
        self.__descr=desc
        self.__tipo=tipo
        self.__importe=imp
    
    def __str__(self):
        return f"{self.__fecha}          {self.__descr}          {self.__importe}            {self.__tipo}"
    
    def __lt__(self, otro):
        if int(self.__num_cuenta)<int(otro.dar_numcuenta()):
            return True
    
    def dar_numcuenta(self):
        return int(self.__num_cuenta)
    def dar_tipo(self):
        return self.__tipo
    def dar_imp(self):
        return float(self.__importe)
        
    