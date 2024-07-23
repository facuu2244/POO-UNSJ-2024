import csv
from clase_libro import libro
from clase_cd  import cd
class gestor_publis:
    __publicaciones:list
    
    def __init__(self):
        self.__publicaciones=[]
    
    def cargar(self, ruta_cd, ruta_libros):
        with open(ruta_cd, "r") as archi_cd: #carga los cd
            reader=csv.reader(archi_cd)
            next(reader)
            for fila in reader:
                titulo, cate, precio,tiempo,nom=fila                
                un_cd=cd(titulo, cate, precio,tiempo,nom)
                self.__publicaciones.append(un_cd)
        
        with open(ruta_libros, "r") as archi_libros:#carga los libros
            reader=csv.reader(archi_libros)
            next(reader)
            for fila in reader:
                titulo, cate, precio,nom, fecha, cant=fila                
                un_libro=libro(titulo, cate, precio,nom, fecha, cant)
                self.__publicaciones.append(un_libro)
                
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
                self.__publicaciones.append(un_libro)
                
                print("\nLIBRO AGREGADO\n")
            
            elif tipo.lower()=="cd" or tipo.lower()=="audiolibro":
                valido=1
                titulo=input("Titulo del audiolibro: ")
                cate=input("Categoria: ")
                precio=input("Precio base: ")
                tiempo=input("Tiempo de reprodiccion en munutos: ")
                nom=input("Nombre del narrador: ")
                
                un_cd=cd(titulo, cate, precio,tiempo,nom)
                self.__publicaciones.append(un_cd)
                
                print("\CD AGREGADO\n")
                
            else:
                print("Tipo de publicacion invalida")
                
        
    def consultar(self):
        valido=0
        while valido==0:
            try:
                posicion=int(input("Posicion de la lista: "))
                assert posicion<=len(self.__publicaciones)
                
                if isinstance(self.__publicaciones[posicion-1], libro):
                    valido=1
                    print("La publicacion es un libro")
                    
                elif isinstance(self.__publicaciones[posicion-1], cd):
                    valido=1
                    print("La publicacion es un audiolibro (cd)")
                
            except AssertionError:
                print("El valor indicado esta fuera del alcance de la lista")
            except ValueError:
                print("Tipo de valor incorrecto")
                
    def contar_tipos(self):
        cont_libros=0
        cont_cd=0
        for publi in self.__publicaciones:
            if isinstance(publi, libro):
                cont_libros+=1
            else:
                cont_cd+=1
                
        print(f"Hay en total: {cont_libros} libros y {cont_cd} audiolibros (CDs)")
        
    def mostrar(self):
        print("\nTitulo, Categoria, Importe de venta:\n")
        # print("\nLibros:")
        
        for publi in self.__publicaciones:
            publi.mostrar_publi()
        
        # for publi in self.__publicaciones:
        #     if isinstance(publi, libro):
        #         publi.mostrar_publi(publi.dar_fecha())
                
        # print("\nCDs:")  
        # for publi in self.__publicaciones:
        #     if isinstance(publi, cd):
        #         publi.mostrar_publi()
        
    def getlista(self):
        return self.__publicaciones