from aplicacion import aplicacion
from tkinter import *

def cerrar(nombre, ventana):
    global nom
    nom=nombre
    ventana.destroy()
    
def ventana_nombre():
    ventana=Tk()
    ventana.resizable(0,0)
    texto_nombre=Label(ventana, text="Nombre del jugador")
    texto_nombre.grid(row=0, column=0)
    entry_nombre=Entry(ventana)
    entry_nombre.grid(row=0, column=1)
    boton_empezar=Button(ventana, text="Empezar", command=lambda: cerrar(entry_nombre.get(), ventana))
    boton_empezar.grid(row=1, column=0, columnspan=2)
    ventana.mainloop()
    
if __name__ == '__main__':
    nom:str
    ventana_nombre()
    app=aplicacion(nom)
    app.mainloop()