from gestor_ladrillo import gestor_lad
from gestor_material import gestor_mat

if __name__ == '__main__':
    lista_ladrillos=gestor_lad()
    lista_materiales=gestor_mat()
    
    ruta_ladri="ladrillos.csv"
    ruta_mate="materiales.csv"
    
    lista_ladrillos.carga(ruta_ladri)
    lista_materiales.carga(ruta_mate)
    
    lista_ladrillos.asignar_materiales(lista_materiales)
    
    seguir = 1
    while seguir != 0:
        print('---------------MENU DE OPCIONES---------------')
        print('1. Ver caracteristicas del ladrillo')
        print('2. Costo de pedido por cada ladrillo')
        print('3. Tabla con detalles de cada ladrillo ')
        print('0. Salir')
        
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            try:
                id=int(input("Ingrese id del ladrillo: "))
                band=lista_ladrillos.validar(id)
                if band==False:
                    print("Ladrillo no encontrado")
            except ValueError:
                print("Se espera un entero")
                
        elif opcion==2:
            lista_ladrillos.costo_pedido()
            
        elif opcion==3:
            lista_ladrillos.tabla()
        elif opcion==0:
            break
        else:
            print('Opcion invalida')

        seguir = int(input('Seguir?(Distinto de 0 para seguir): '))