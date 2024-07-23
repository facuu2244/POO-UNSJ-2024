from clase_equipos import *
from clase_fechas import *

if __name__ == '__main__':
    gestor_equipos=gestor_eq()
    gestor_fecha=gestor_fe()
    
    gestor_equipos.cargar_gestor()
    gestor_fecha.cargar_gestor()
    
    seguir=1
    
    while seguir!=0:
        print("---------------MENU DE OPCIONES---------------")
        print("1. Ver tabla de equipo")
        print("2. Actualizar tabla de equipos")
        print("3. Tabla de equipos")
        print("4. Tabla ordenada de equipos")
        
        opcion=int(input("Ingrese opcion: "))
        if opcion==1:
            equi, id= gestor_equipos.validar_equipo()
            if equi!=None and id != None:
                gestor_fecha.tabla(equi,id)
            else:
                print("Equipo no encontrado")
        
        elif opcion==2:
            gestor_fecha.agregar_fechas()
            print("Fecha agregada")
        
        elif opcion==3:
            gestor_equipos.generar_tablas(gestor_fecha)
        
        elif opcion==4:
            gestor_equipos.ordenar()
            gestor_equipos.archivar()
           
        seguir=(int(input("Seguir: ")))