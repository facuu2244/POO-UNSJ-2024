import random
import json
import datetime
from tkinter import *    
from tkinter import messagebox
from gestor_jugadores import gestor

class aplicacion(Tk):
    __secuencia:list
    __entrada_usuario:list
    __puntos:object
    __ventana_nombre_jugador:object
    __nombre_jugador:object
    
    def __init__(self):
        super().__init__()
        self.__secuencia=[]
        self.__entrada_usuario=[]
        self.__puntos=IntVar()
        self.__puntos.set(0)
        self.__nombre_jugador=StringVar()
        self.ventana_nombre()
        #Creacion y configuracion de botones, se tratan como atributos para ser referenciados luego 
        self.boton_verde=Button(self,relief="raised", cursor="hand2", bg="green", width=20, height=10, command=lambda: self.agregar_entrada("verde"))
        self.boton_rojo=Button(self,relief="raised", cursor="hand2", bg="red", width=20, height=10, command=lambda: self.agregar_entrada("rojo"))
        self.boton_amarillo=Button(self,relief="raised", cursor="hand2", bg="yellow", width=20, height=10, command=lambda: self.agregar_entrada("amarillo"))
        self.boton_azul=Button(self,relief="raised", cursor="hand2", bg="blue", width=20, height=10, command=lambda: self.agregar_entrada("azul"))
        
    def ventana_nombre(self):
        self.__ventana_nombre_jugador=Toplevel()
        self.__ventana_nombre_jugador.resizable(0,0)
        texto_nombre=Label(self.__ventana_nombre_jugador, text="Nombre del jugador")
        texto_nombre.grid(row=0, column=0)
        entry_nombre=Entry(self.__ventana_nombre_jugador)
        entry_nombre.grid(row=0, column=1)
        boton_empezar=Button(self.__ventana_nombre_jugador, text="Empezar", command=lambda: self.ventana_principal(entry_nombre.get()))
        boton_empezar.grid(row=1, column=0, columnspan=2)

        
    def ventana_principal(self, nom):
        #Configuracion de ventana principal y label de datos del jugador
        self.__nombre_jugador.set(nom)
        self.__ventana_nombre_jugador.destroy()
        self.title("Py-Python")
        self.geometry("308x395")
        self.resizable(0,0)
        
        barra_menu=Menu(self)#Barra menu superior
        self.config(menu=barra_menu)
        puntajes=Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Puntajes", menu=puntajes)
        puntajes.add_command(label="Ver puntajes", command=lambda: self.mostrar_puntajes())
        puntajes.add_command(label="Salir", command=lambda: self.quit())
        
        #Frame datos del jugador
        datos_jugador=LabelFrame(self, padx=5, pady=5)
        datos_jugador.grid(row=0, column=0, columnspan=2)
        
        label_nombre=Label(datos_jugador, textvariable=self.__nombre_jugador, font="bold")
        label_nombre.grid(row=0, column=0)
        label_puntaje=Label(datos_jugador, text="puntaje:", font="bold")
        label_puntaje.grid(row=0, column=1)
        puntos=Label(datos_jugador, textvariable=self.__puntos)
        puntos.grid(row=0, column=2)
    
        #Posicionamiento de botones 
        self.boton_verde.grid(row=1, column=0, padx=2, pady=2)
        self.boton_rojo.grid(row=1, column=1, padx=2, pady=2)
        self.boton_amarillo.grid(row=2, column=0, padx=2, pady=2)
        self.boton_azul.grid(row=2, column=1, padx=2, pady=2)
        #Empieza el juego
        self.generar_secuencia()
        self.mostrar_secuencia()
            
    #     self.boton_amarillo.bind('<ButtonPress>', self.cambiar_color)
    #     self.boton_amarillo.bind('<ButtonRelease>', self.restaurar)
        
    # def cambiar_color(self, event):
    #     print("Botón amarillo presionado")
    #     self.boton_amarillo.config(bg="red")
    # def restaurar(self, event):
    #     print("Botón amarillo liberado")
    #     self.boton_amarillo.config(bg="yellow")
    
    #--------------------funcionamiento---------------
    def mostrar_puntajes(self):
        #Ventana emergente para mostrar puntajes
        ventana_puntos=Toplevel()
        ventana_puntos.resizable(0,0)
        labelframe_principal=LabelFrame(ventana_puntos, text="Galeria de puntajes")
        labelframe_principal.grid(row=0,column=0)
        label_jugador=Label(labelframe_principal, text="Jugador")
        label_fecha=Label(labelframe_principal, text="Fecha")
        label_hora=Label(labelframe_principal, text="Hora")
        label_puntos=Label(labelframe_principal, text="Puntos")
        
        label_jugador.grid(row=0, column=0)
        label_fecha.grid(row=0, column=1)
        label_hora.grid(row=0, column=2)
        label_puntos.grid(row=0, column=3)
        
        cuadro_texto=Text(labelframe_principal, height=10)
        cuadro_texto.grid(row=1, column=0, columnspan=4)
        
        #Crea, carga y ordena el gestor
        gest=gestor()
        gest.cargar()
        gest.ordenar()
        lista_jugadores=gest.listar()
        for jugador in lista_jugadores:
            cuadro_texto.insert(END, jugador+"\n")#Escribe cada jugador en el cuadro de texto
            
        cuadro_texto.config(state=DISABLED)#Impide que el usuario escriba en el cuadro    
        self.wait_window(ventana_puntos)
    
    def cargar_partida(self):
        partidas=[]#sera lista de diccionarios
        with open("pysimonpuntajes.json", "r") as archivo:#cargo en la lista las partidas del archivo
            lector=json.load(archivo)
            for jugador in lector:
                nombre=jugador.get("nombre")
                puntos=jugador.get("puntos")
                fecha=jugador.get("fecha")
                hora=jugador.get("hora")
                una_partida={"nombre": nombre, "puntos":puntos, "fecha":fecha, "hora":hora}
                partidas.append(una_partida)
                
        #cargo la partida actual
        nombre=self.__nombre_jugador.get()
        puntos=self.__puntos.get()
        fecha_hora_actual=datetime.datetime.now()
        fecha=fecha_hora_actual.strftime("%Y-%m-%d")
        hora=fecha_hora_actual.strftime("%H:%M")
        una_partida={"nombre": nombre, "puntos":puntos, "fecha":fecha, "hora":hora}
        partidas.append(una_partida)
        
        with open("pysimonpuntajes.json", "w") as archi:#carga en el archivo la lista de diccionarios
            json.dump(partidas, archi, indent=3)
            
    def generar_secuencia(self):
        botones = [0,1,2,3]
    
        elegido=random.choice(botones)
        self.__secuencia.append(elegido)
        
    def mostrar_secuencia(self):
        for boton in self.__secuencia:
            if boton==0:
                self.boton_verde.config(relief="sunken", bg="#009C00")
                self.update()  # Actualiza la ventana para que se vean los cambios
                self.after(500)  # Espera 1 segundo
                self.boton_verde.config(relief="raised", bg="green")
                self.update()
                self.after(500)
                    
            elif boton==1:
                self.boton_rojo.config(relief="sunken", bg="#C90000")
                self.update()  # Actualiza la ventana para que se vean los cambios
                self.after(500)  # Espera 1 segundo
                self.boton_rojo.config(relief="raised", bg="red")
                self.update()
                self.after(500)
            
            elif boton==2:
                self.boton_amarillo.config(relief="sunken", bg="#CAD100")
                self.update()  # Actualiza la ventana para que se vean los cambios
                self.after(500)  # Espera 1 segundo
                self.boton_amarillo.config(relief="raised", bg="yellow")
                self.update()
                self.after(500)
                    
            elif boton==3:
                self.boton_azul.config(relief="sunken", bg="#00009E")
                self.update()  # Actualiza la ventana para que se vean los cambios
                self.after(500)  # Espera 1 segundo
                self.boton_azul.config(relief="raised", bg="blue")
                self.update()
                self.after(500)
                
        
    def agregar_entrada(self, color):
        if color=="verde":
            self.__entrada_usuario.append(0)
            self.validar_secuencia()
        elif color=="rojo":
            self.__entrada_usuario.append(1)
            self.validar_secuencia()
        elif color=="amarillo":
            self.__entrada_usuario.append(2)
            self.validar_secuencia()
        else:
            self.__entrada_usuario.append(3)
            self.validar_secuencia()
                
    def validar_secuencia(self):
        if len(self.__entrada_usuario)==len(self.__secuencia)and self.__secuencia==self.__entrada_usuario: #verifica que la secuencia ingresada sea la correcta
            self.__puntos.set(self.__puntos.get()+1)
            self.__entrada_usuario=[] #Reinicia la lista generada por la entrada del usuario
            self.generar_secuencia()
            self.mostrar_secuencia()
        else:
            long_secuencia_usuario=len(self.__entrada_usuario)#Guarda la longitud de la secuencia ingresada por el usuario
            if self.__entrada_usuario[-1]!=self.__secuencia[long_secuencia_usuario-1]:#Verifica si la ultima entrada del usuario es diferentena la de la secuencia generada segun el largo de la secuencia del usuario
                respuesta=messagebox.askquestion("Game Over", f"Puntaje obtenido: {self.__puntos.get()}. Deseas volver a jugar?")
                if respuesta=="yes":
                    #Reinicia el juego
                    self.cargar_partida()
                    self.__secuencia=[]
                    self.__entrada_usuario=[]
                    self.__puntos.set(0)
                    self.generar_secuencia()
                    self.mostrar_secuencia()
                else:
                    #Cierra la aplicacion
                    self.cargar_partida()
                    self.quit()