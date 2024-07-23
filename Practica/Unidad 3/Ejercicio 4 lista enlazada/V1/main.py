from gestor_lista_elnlazada import lista

if __name__ == '__main__':
    ruta_cd="cd.csv"
    ruta_libros="libros.csv"
    
    lista_publicaciones=lista()
    lista_publicaciones.cargar(ruta_cd, ruta_libros)
    
    opcion=-1
    while opcion != 0:
        print()
        print('---------------MENU DE OPCIONES---------------')
        print('1. Agregar publicacion')
        print('2. Consultar tipo de publicacion en la lista')
        print('3. Mostrar la cantidad de publicaciones de cada tipo')
        print('4. Mostrar todas las publicaciones')
        print('0. Salir')
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            lista_publicaciones.agregar()
            
        elif opcion==2:
            lista_publicaciones.consultar()
        
        elif opcion==3:
            lista_publicaciones.contar_tipos()
            
        elif opcion==4:
            lista_publicaciones.mostrar()
        
        elif opcion==0:
            break
        else:
            print('Opcion invalida')