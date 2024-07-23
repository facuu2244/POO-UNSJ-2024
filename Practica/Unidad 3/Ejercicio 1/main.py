from clase_gestor import gestor

if __name__ == '__main__':
    ruta_archi="EdificioNorte.csv"
    
    lista_edificios=gestor()
    lista_edificios.cargar(ruta_archi)
    
    seguir = 1
    while seguir != 0:
        print('---------------MENU DE OPCIONES---------------')
        print('1. Mostrar propietarios de departamentos de un edificio')
        print('2. Mostrar superficie cubierta por el edificio')
        print('3. Consultar tamano del departamento de un propietario')
        print('4. Mostrar departamentos con 3 habitaciones y mas de un baño en un piso')

        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            edif=input("Ingrese nombre del edificio >> ")
            band, i=lista_edificios.validar(edif)
            if band==True:
                lista_edificios.mostrar_deptos(i)
            else: 
                print("Edificio no encontrado")
        
        elif opcion==2:
            edif=input("Ingrese nombre del edificio >> ")
            band, i=lista_edificios.validar(edif)
            if band==True:
                lista_edificios.mostrar_sup(i)
            else: 
                print("Edificio no encontrado")
            
        elif opcion==3:
            try:
                lista_edificios.tam_depto() 
            except:
                print("Se pordujo un error")
                
        elif opcion==4:
            lista_edificios.buscar_deptos()
                        
        else:
            print("Opcion invalida")
        seguir = int(input('Seguir: '))
        
    lista_edificios.eliminar()