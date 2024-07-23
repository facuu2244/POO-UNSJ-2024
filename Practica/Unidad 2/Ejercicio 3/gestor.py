import numpy as np

class gestor:
    __gestor=np.zeros((5,7))
    
    def mostrar(self):
        print(self.__gestor)
        
    def cargar(self, dia, num, imp):
        self.__gestor[num-1][dia-1]+=imp
        
    def total_suc(self, num):
        print(np.sum(self.__gestor[num-1]))
        
    def calc_dia(self, dia):
        if dia <= 5:
            max=0
            for i in range(5):
                if self.__gestor[i][dia-1]>max:
                    max=self.__gestor[i][dia-1]
                    sucu=i+1
            print("La sucursal que mas recaudo fue la numero ", sucu)
        else:
            print("Dia invalido")
    
    def menos_factu(self):
        self.__min=9999999
        self.__sucu=[]
        for i in range(5):
            __suma=np.sum(self.__gestor[i])
            if __suma<self.__min:
                self.__min=__suma
                self.__sucu=i
        
        print("\nLa sucursal que menos recaudo fue: ", self.__sucu)

    def total_sucu(self):
        for i in range(5):
            total=np.sum(self.__gestor[i])
            print(f"\nSucursal {i+1} total: {total}")