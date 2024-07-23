import csv
from claseClientes import *

class gestor_cliente:
    __gestor:list
    
    def __init__(self):
        self.__gestor=[]
        
    def cargar(self, ruta):
        with open(ruta, "r") as archi_clientes:
            reader=csv.reader(archi_clientes, delimiter=";")
            next(reader)
            for fila in reader:
                nom,ape,dni, num, saldo= fila
                un_cliente=cliente(nom,ape,dni,num,saldo)
                
                self.__gestor.append(un_cliente)
        
        
    def verificar_cliente(self, dni):
        band=False
        i=0
        while band==False and i<len(self.__gestor):
            if dni==self.__gestor[i].dar_dni():
                band=True
                num_cuenta=self.__gestor[i].dar_numcuenta()
                saldo=self.__gestor[i].dar_saldo()
                self.__gestor[i].mostrar_datos()
            i+=1
        return band, num_cuenta, saldo
    
    def buscar(self, dni):
        band=False
        i=0
        while band==False and i<len(self.__gestor):
            if dni==self.__gestor[i].dar_dni():
                band=True
                nom=self.__gestor[i].dar_nom()
                ape=self.__gestor[i].dar_ape()
                num=self.__gestor[i].dar_numcuenta()
            i+=1
        return num, nom, ape
        