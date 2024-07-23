import csv

class transferencia:
    __cvu=int
    __num_transac=int
    __importe=float
    __tipo=str
    
    def __init__(self, cvu, num, imp, tipo):
        self.__cvu=cvu
        self.__num_transac=num
        self.__importe=float(imp)

    def dar_imp(self):
        return self.__importe  
    def dar_cvu(self):
        return self.__cvu      
        
class gestor_transferencia:
    __gestor:list
    
    def __init__(self):
        self.__gestor=[]
        
    def __str__(self) -> str:
        for cuenta in self.__gestor:
            return print(cuenta)
    
    def cargar(self, ruta_transfe):
        with open(ruta_transfe, "r") as archi_tranfe:
            reader=csv.reader(archi_tranfe)
            next(reader)
            
            for fila in reader:
                cvu, num, imp, tipo=fila
                una_transfe=transferencia(cvu,num,imp,tipo)
                self.__gestor.append(una_transfe)
                
    def nuevo_saldo(self, cvu): #Suma los importes de las transferenciasc de ese cliente para despues actualizar su saldo
        saldo=0
        for tran in self.__gestor:
            if cvu==tran.dar_cvu():
                saldo+=tran.dar_imp()
        return saldo