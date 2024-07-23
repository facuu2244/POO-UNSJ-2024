from claseMovimiento import movimiento
import numpy as np
import csv

class gestor_movimiento:
    __gestor:np.array
    
    def __init__(self) -> None:
        self.__gestor=np.array([])
        
    def cargar(self, ruta):
        with open(ruta, "r") as archi_movi:
            reader=csv.reader(archi_movi, delimiter=";")
            next(reader)
            for fila in reader:
                num,fecha,descri, tipo, imp= fila
                un_movimiento=movimiento(num,fecha,descri, tipo, imp)
                #list=[un_movimiento]
                #self.__gestor=np.array(list)
                self.__gestor=np.append(self.__gestor,un_movimiento)
                
    def actu_saldo(self, num_cuenta, saldo):
        print('''Movimientos:
Fecha           Descripcion         Importe         Tipo de movimiento''')
        for movi in self.__gestor:
            if num_cuenta==movi.dar_numcuenta():
                if movi.dar_tipo()=='P':
                    saldo=saldo-movi.dar_imp()
                    print(movi)
                    
                elif movi.dar_tipo()=='C':
                    saldo+=movi.dar_imp()
                    print(movi)
        
        print(f"Nuevo saldo: {saldo}")
        
    def validar_movi(self, num, nom, ape):
        band=False
        for movi in self.__gestor:
            if num==movi.dar_numcuenta():
                band=True
            
        if band==False:
            print(f"{ape}, {nom} no tuvo movimientos durante abril")
        else:
            print ("El cliente si tuvo movimientos durante el mes de abril")

        
    
    def ordenar(self):
        print("Lista de movimientos actual:")
        for movimiento in self.__gestor:
            print(movimiento)
        print("-------------------------------------------------------------")
        self.__gestor.sort()
        print("Lista ordenada de movimientos:")
        for movimiento in self.__gestor:
            print(movimiento)
        
        