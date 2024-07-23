import random
import csv
from clase_empleado import empleado
from clase_programa_capacitacion import programa
from clase_matricula import matricula

class gestor_matri:
    __matriculas:list
    __fechas:list
    
    def __init__(self):
        self.__matriculas=[]
        self.__fechas=[]
        
    def cargar_fechas(self, ruta):
        with open (ruta, "r") as archivo:
            reader=csv.reader(archivo, delimiter=";")
            next(reader)
            
            for fila in reader:
                una_fecha=fila
                self.__fechas.append(una_fecha)
        
    def verificar_mat(self, una_matricula):
        band=False
        i=0
        while band==False and i<len(self.__matriculas):
            if (una_matricula.dar_empl()==self.__matriculas[i].dar_empl()) and (una_matricula.dar_prog()==self.__matriculas[i].dar_prog()):
                band=True
            else:
                i+=1
        return band
    
    def asignar_matriculas(self, g_empelados, g_programas):
        indice_emp=list(range(g_empelados.dar_cantidad()))
        indice_prog=list(range(g_programas.dar_cantidad()))
        indice_fechas=list(range(len(self.__fechas)))
        
        for i in range(7):
            empl_random=random.choice(indice_emp)
            prog_random=random.choice(indice_prog)
            fecha_random=random.choice(indice_fechas)
        
            una_matricula=matricula(self.__fechas[fecha_random], g_empelados.dar_empl(empl_random), g_programas.dar_prog(prog_random))
            
            if self.verificar_mat(una_matricula)==False:
                self.__matriculas.append(una_matricula)
                g_empelados.dar_empl(empl_random).matricular(una_matricula)
                g_programas.dar_prog(prog_random).matricular(una_matricula)
                print(f"Se matriculo a {(g_empelados.dar_empl(empl_random)).dar_nya()} en el programa '{(g_programas.dar_prog(prog_random)).dar_nom()}'")
                
            else:
                print(f"{(g_empelados.dar_empl(empl_random)).dar_nya()} ya estaba matriculado en el programa '{(g_programas.dar_prog(prog_random)).dar_nom()}'")
            