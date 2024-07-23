import csv
from claseCuentas import *
from claseTransfe import *

if __name__ == '__main__':
    #guardo la ruta de los archivos
    ruta_cuentas= "cuentasBilletera.csv"
    ruta_transfe= "transaccionesBilletera.csv"
    
    #instancio y cargo los gestores
    lista_cuentas=gestor_cuenta()
    lista_transfe=gestor_transferencia()
    
    lista_cuentas.cargar(ruta_cuentas)
    lista_transfe.cargar(ruta_transfe)
    
    seguir = 1
    while seguir != 0:
        print('---------------MENU DE OPCIONES---------------')
        print('1. Ver datos del cliente')
        print('2. Cambiar porcentaje anual de rendimiento')
    
        opcion=int(input('Ingrese opcion: '))
        
        if opcion==1:
            cliente=int(input("Dni del cliente: "))
            cvu=lista_cuentas.buscar_cvu(cliente) 
            if cvu!=None: #Verifica si se encontro o no el cliente
                nuevo_saldo=lista_transfe.nuevo_saldo(cvu)
                lista_cuentas.mostrar_cliente(cliente, nuevo_saldo)
            else:
                print("Cliente no encontrado")
                
        elif opcion==2:
            porc=float(input("Ingrese nuevo porcentaje de aumento: "))
            cuenta.cambiar_rendi(porc)
        elif opcion==3:
            pass
        seguir = int(input('Seguir: '))