from clase_coleccion import coleccion

if __name__ == '__main__':
    lista=coleccion()

    opcion=-1
    while opcion != 0:
        print()
        print('---------------MENU DE OPCIONES---------------')
        print('1. Cargar un servicio')
        print('2. Mostrar servicios de transporte')
        print('3. Ver cantidad de servicios de embalaje con peso por unidad mayor a 50kg')
        print('4. Dar el tipo de servicio que mas contrataciones tuvo segun una fecha')
        print('0. Salir')
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            try:
                servicio=input("Tipo de servicio que desea cargar: ")
                assert servicio.lower()=="transporte" or servicio.lower()=="embalaje"
                
                lista.cargar(servicio)
            except AssertionError:
                print("Tipo de servicio invalido")
                
            except ValueError:
                print("Se esperaba una cadena de texto")
                
        elif opcion==2:
            lista.mostrar_transportes()
            
        elif opcion==3:
            lista.embalajes()
            
        elif opcion==4:
            lista.mas_contrataciones()
        elif opcion==0:
           pass
        else:
            print('Opcion invalida')