from gestor_lista_elnlazada import lista
from clase_cd import cd
from clase_libro import libro

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
            cont_libros, cont_cd=0, 0
            for publi in lista_publicaciones:
                if isinstance(publi, libro):
                    cont_libros+=1
                else:
                    cont_cd+=1

            print(f"Hay en total: {cont_libros} libros y {cont_cd} audiolibros (CDs)")
            
        elif opcion==4:
            print("\nTitulo, Categoria, Importe de venta:\n")
            
            for publi in lista_publicaciones:
                publi.mostrar_publi()
        
        elif opcion==0:
            break
        else:
            print('Opcion invalida')