import csv
from clase_nodo import nodo
from clase_libro import libro
from clase_cd  import cd
class lista:
    __comienzo:nodo
    __largo:int
    def __init__(self):
        self.__comienzo=None
        self.__largo=0
    
    def cargar(self, ruta_cd, ruta_libros):
        with open(ruta_cd, "r") as archi_cd: #carga los cd
            reader=csv.reader(archi_cd)
            next(reader)
            for fila in reader:
                titulo, cate, precio,tiempo,nom=fila                
                un_cd=cd(titulo, cate, precio,tiempo,nom)
                un_nodo=nodo(un_cd)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
                self.__largo+=1

        with open(ruta_libros, "r") as archi_libros:#carga los libros
            reader=csv.reader(archi_libros)
            next(reader)
            for fila in reader:
                titulo, cate, precio,nom, fecha, cant=fila                
                un_libro=libro(titulo, cate, precio,nom, fecha, cant)
                un_nodo=nodo(un_libro)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
                self.__largo+=1
                
    def agregar(self):
        valido=0
        while valido==0:
            tipo=input("Tipo de publicacion(libro o cd): ")
            
            if tipo.lower()=="libro":
                valido=1
                titulo=input("Titulo del libro: ")
                cate=input("Categoria: ")
                precio=input("Precio base del libro: ")
                nom=input("Nombre del autor: ")
                fecha=input("Fecha de edicion: ")
                cant=input("Cantidad de paginas: ")
                
                un_libro=libro(titulo, cate, precio,nom, fecha, cant)
                un_nodo=nodo(un_libro)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
                self.__largo+=1
                
                print("\nLIBRO AGREGADO\n")

            
            elif tipo.lower()=="cd" or tipo.lower()=="audiolibro":
                valido=1
                titulo=input("Titulo del audiolibro: ")
                cate=input("Categoria: ")
                precio=input("Precio base: ")
                tiempo=input("Tiempo de reprodiccion en munutos: ")
                nom=input("Nombre del narrador: ")
                
                un_cd=cd(titulo, cate, precio,tiempo,nom)
                un_nodo=nodo(un_cd)
                un_nodo.set_siguiente(self.__comienzo)
                self.__comienzo=un_nodo
                self.__largo+=1
                
                print("\CD AGREGADO\n")
                
            else:
                print("Tipo de publicacion invalida")
                
        
    def consultar(self):
        valido=0
        while valido==0:
            try:
                posicion=int(input("Posicion de la lista: "))
                assert posicion<=self.__largo

                aux=self.__comienzo
                cont=0
                while cont!=posicion:#Se recorre la lista hasta la posicion indicada
                    aux=aux.dar_siguiente()
                    cont+=1
                
                if isinstance(aux.dar_publicacion(), libro):
                     valido=1
                     print("La publicacion es un libro")
                elif isinstance(aux.dar_publicacion(), cd):
                     valido=1
                     print("La publicacion es un audiolibro (cd)")
                           
            except AssertionError:
                print("El valor indicado esta fuera del alcance de la lista")
            except ValueError:
                print("Tipo de valor incorrecto")
                
                
    def contar_tipos(self):
        cont_libros=0
        cont_cd=0
        
        aux=self.__comienzo
        
        while aux!=None:
            if isinstance(aux.dar_publicacion(), libro):
                cont_libros+=1
            else: 
                cont_cd+=1
            aux=aux.dar_siguiente()
                
        print(f"Hay en total: {cont_libros} libros y {cont_cd} audiolibros (CDs)")
        
    def mostrar(self):
        print("\nTitulo, Categoria, Importe de venta:\n")
        
        aux=self.__comienzo
        
        while aux!=None:
            publi=aux.dar_publicacion()
            publi.mostrar_publi()
            aux=aux.dar_siguiente()        