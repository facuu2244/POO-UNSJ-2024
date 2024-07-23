from clase_programa_capacitacion import programa
import csv

class gestor_prog:
    __programas:list
    
    def __init__(self):
        self.__programas=[]
        
    def cargar(self, ruta):
        with open (ruta, "r") as archivo:
            reader=csv.reader(archivo, delimiter=";")
            next(reader)
            
            for fila in reader:
                nom, cod, duracion=fila
                un_programa=programa(nom, cod, duracion)
                self.__programas.append(un_programa)
                
    def dar_cantidad(self):
        return len(self.__programas)
    def dar_prog(self, i):
        return self.__programas[i]
    
    def buscar(self, nom):
        band=False
        i=0
        while band==False and i<len(self.__programas):
            if self.__programas[i].dar_nom()==nom:
                band=True
            else:
                i+=1
        
        return band, i
    
    def mostar_empl(self, i):
        self.__programas[i].empleados()