import csv
from clase_fechas import *

class equipo:
    __id=int
    __nom=str
    __golesfav=int
    __golescont=int
    __difgoles=int
    __puntos=int
  
    def __init__(self, id, nom, golesfav, golescont, difgoles, puntos):
        self.__id=id
        self.__nom=nom
        self.__golesfav=golesfav
        self.__golescont=golescont
        self.__difgoles=difgoles
        self.__puntos=puntos
    
    def __str__(self):
        return f'''{self.__nom}:     goles a favor         goles en contra         dif de goles         puntos
                 {self.__golesfav}                   {self.__golescont}                       {self.__difgoles}                 {self.__puntos}'''
    
    def __gt__(self, otro):
        if int(self.__puntos)>int(otro.dar_puntos()):
            return False
        elif self.__puntos==int(otro.dar_puntos()):
            if self.__golesfav>otro.dar_golesfav():
                return False
            else:
                return True
        else:
            return True
    
    def dar_nom(self):
        return self.__nom
    def dar_id(self):
        return self.__id
    def dar_puntos(self):
        return self.__puntos
    def dar_golesfav(self):
        return self.__golesfav
    
    def actualizar(self, gf,gc,di,pu):
        self.__golesfav=gf
        self.__golescont=gc
        self.__difgoles=di
        self.__puntos=pu
        
    def listar(self):
        lista=[self.__id, self.__nom, self.__golesfav, self.__golescont, self.__difgoles, self.__puntos]
        return lista
class gestor_eq:
    __gestor:list
    
    def __init__(self):
        self.__gestor=[]
    
    def cargar_gestor(self):
        archi_equipos=open("equipos2024.csv", "r")
        reader=csv.reader(archi_equipos)
        next(reader)
    
        for row in reader:
            id, nom, golesfav, golescont, difgoles, puntos=row
            un_equipo=equipo(id, nom, golesfav, golescont, difgoles, puntos)
            self.__gestor.append(un_equipo)
            
    def validar_equipo(self):
        band=False
        i=0
        equi=input("Nombre del equipo: ")
        while band==False and i<len(self.__gestor):
            if equi==self.__gestor[i].dar_nom():
                band=True
                id=self.__gestor[i].dar_id()
                return equi, id
            i+=1
        if band==False:
            return None, None
    
    def generar_tablas(self, gestor_fecha):
        for eq in self.__gestor:
            id= eq.dar_id()
            gf,gc,di,pu=gestor_fecha.datos_paratabla(id)
            
            eq.actualizar(gf, gc, di, pu)
            print(eq)
            
    def ordenar(self):
        self.__gestor.sort()
        for eq in self.__gestor:
            print(eq)
            
    def archivar(self):
        cabecera=[]
        with open("equipos2024.csv", "r+") as archi_equipos:
            reader=csv.reader(archi_equipos, lineterminator="\n")
            cabecera=next(reader)
            
        with open("equipos2024.csv", "w") as archi_equipos:
            writer=csv.writer(archi_equipos, lineterminator="\n")
            writer.writerow(cabecera)
            for eq in self.__gestor:
                writer.writerow(eq.listar())