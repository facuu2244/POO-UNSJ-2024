import csv

class fecha:
    __fechapar=str
    __ideqlocal=int
    __ideqvisi=int
    __canteqlocal=int
    __canteqvisi=int
    
    def __init__(self, fechapar, ideqlocal, ideqvisi, canteqlocal, canteqvisi):
        self.__fechapar=fechapar
        self.__ideqlocal=ideqlocal
        self.__ideqvisi=ideqvisi
        self.__canteqlocal=canteqlocal
        self.__canteqvisi=canteqvisi
    def __del__(self):
        print("Objeto eliminado")
        
    def dar_idlocal(self):
        return self.__ideqlocal
    def dar_idvisi(self):
        return self.__ideqvisi
    def dar_canteqlocal(self):
        return int(self.__canteqlocal)
    def dar_canteqvisi(self):
        return int(self.__canteqvisi)
    def dar_fecha(self):
        return self.__fechapar
    def dar_difloc(self):
        return (int(self.__canteqlocal)-int(self.__canteqvisi))
    def dar_difvisi(self):
        return (int(self.__canteqvisi)-int(self.__canteqlocal))
    
    
class gestor_fe:
    __gestor:list
    
    def __init__(self):
        self.__gestor=[]
        
    def cargar_gestor(self):
        archi_equipos=open("fechas2024.csv", "r")
        reader=csv.reader(archi_equipos)
        next(reader)
    
        for row in reader:
            fechapar, ideqlocal, ideqvisi, canteqlocal, canteqvisi=row
            
            una_fecha=fecha(fechapar, ideqlocal, ideqvisi, canteqlocal, canteqvisi)
            self.__gestor.append(una_fecha)
    
    def tabla(self, equi, id):
        print(f"Equipo: {equi}")
        print('''Fecha         goles a favor         goles en contra         dif de goles         puntos''')
        
        for fecha in self.__gestor:
                
            if id==fecha.dar_idlocal():
                if fecha.dar_difloc()<0:
                    puntos=0
                elif fecha.dar_difloc()==0:
                    puntos=1
                else:
                    puntos=3
                print(f"{fecha.dar_fecha()}           {fecha.dar_canteqlocal()}                  {fecha.dar_canteqvisi()}                       {fecha.dar_difloc()}                  {puntos}")
            
            elif id==fecha.dar_idvisi():
                print(f"{fecha.dar_fecha()}           {fecha.dar_canteqvisi()}                  {fecha.dar_canteqlocal()}                       {fecha.dar_canteqvisi()-fecha.dar_canteqlocal()}                  {puntos}")
                
                
    def agregar_fechas(self):
        #se agrega una fecha al gestor
        fechapar=input("Ingrese fecha del partido: ")
        ideqlocal=input("Id del equipo local: ")
        canteqlocal=input("Goles equipo local: ")
        ideqvisi=input("Id del equipo visitante: ")
        canteqvisi=input("Goles equipo visitante: ")

        una_fecha=fecha(fechapar, ideqlocal, ideqvisi, canteqlocal, canteqvisi)
        self.__gestor.append(una_fecha)
        
    def datos_paratabla(self, id):
        golesf=0
        golesc=0
        dif=0
        puntos=0
        for fe in self.__gestor:
            
            if id==fe.dar_idlocal():
                if fe.dar_difloc()<0:
                    puntos+=0
                elif fe.dar_difloc()==0:
                    puntos+=1
                else:
                    puntos+=3
                    
                dif+=fe.dar_difloc()
                golesf+=fe.dar_canteqlocal()
                golesc+=int(fe.dar_canteqvisi())
                
            elif id==fe.dar_idvisi():
                if fe.dar_difvisi()<0:
                    puntos+=0
                elif fe.dar_difvisi()==0:
                    puntos+=1
                else:
                    puntos+=3
                    
                dif+=fe.dar_difvisi()
                golesf+=fe.dar_canteqvisi()
                golesc+=fe.dar_canteqlocal()
            
        return golesf, golesc, dif, puntos