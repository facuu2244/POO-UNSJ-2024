from clase_gestor import g_vehiculos

if __name__ == '__main__':
    ruta="vehiculos.csv"
    
    gestor=g_vehiculos()
    
    gestor.cargar(ruta)
    
    opcion=-1
    while opcion != 0:
        print()
        print('---------------MENU DE OPCIONES---------------')
        print('1. Agregar vehiculo a la coleccion')
        print('2. Consultar tipo de vehiculo')
        print('3. Mostrar la cantidad vehiculos de cada tipo')
        print('4. Mostrar datos de todos los vehiculos')
        print('0. Salir')
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            gestor.agregar()

        elif opcion==2:
            gestor.consultar()
            
        elif opcion==3:
            gestor.contar()    
        
        elif opcion==4:
            gestor.mostrar()
        
        elif opcion==0:
           pass
       
        else:
            print('Opcion invalida')