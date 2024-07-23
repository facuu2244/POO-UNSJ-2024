from gestor_empleados import gestor_empl
from gestor_programas import gestor_prog
from gestor_matriculas import gestor_matri

if __name__ == '__main__':
    ruta_emp="datosEmpleados.csv"
    ruta_prog="datosProgramas.csv"
    ruta_mat="datosMatriculas.csv"
    
    lista_empleados=gestor_empl()
    lista_programas=gestor_prog()
    lista_matriculas=gestor_matri()
    
    lista_empleados.cargar(ruta_emp)
    lista_programas.cargar(ruta_prog)
    lista_matriculas.cargar_fechas(ruta_mat)
    lista_matriculas.asignar_matriculas(lista_empleados, lista_programas)
    
    opcion=-1
    while opcion != 0:
        print('\n---------------MENU DE OPCIONES---------------')
        print('1. Datos de programas de un empleado')
        print('2. Mostrar empleados matriculados a un programa')
        print('3. Mostrar empleados que no fueron matriculados  a ningun programa')
        print('0. Salir')
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            entero=False
            while entero==False:
                try:
                    id=int(input("Ingrese id del empleado: "))
                    band, i=lista_empleados.buscar(id)
                    assert band == True
                    lista_empleados.mostar_prog(i)
                    entero=True
                    
                except AssertionError:
                    print("No se encontro empleado")
                except ValueError:
                    print("Se espera un entero...")
                    
        elif opcion==2:
            programa=False
            while programa==False:
                try:
                    nom=input("Ingrese nombre del programa:") 
                    
                    band, i=lista_programas.buscar(nom)
                    assert band == True
                    lista_programas.mostar_empl(i)
                    programa=True
                    
                except AssertionError:
                    print("Nombre invalido o no se encontro el programa")
                    
        elif opcion==3:
            lista_empleados.empl_nomatri()
        elif opcion==0:
           pass
        else:
            print('Opcion invalida')