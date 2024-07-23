from clasemoto import *
from clasepedido import *
import csv

if __name__ == '__main__':
    #abre los archivos y omite la primer linea
    archi_moto=open("datosMoto.csv", "r")
    archi_pedi=open("Practica/Unidad 2/Ejercicio 4/datos/datosPedido.csv", "r")
    reader_moto=csv.reader(archi_moto, delimiter=";")
    reader_pedi=csv.reader(archi_pedi, delimiter=";")
    
    next(reader_moto)
    next(reader_pedi)
    
    #instancia la clase gestor(crea las listas)
    gestor_mo=gestor_motos()
    gestor_ped=gestor_pedidos()

    #carga el gestor con los datos de las motos
    for fila in reader_moto:
        patente, marca, conductor, km = fila
        una_moto=moto(patente, marca, conductor,km)
        gestor_mo.cargar(una_moto)

    #carga los datos de los pedidos
    for fila in reader_pedi:
        pate, id, comidas, tiemp_est, _, precio = fila
        un_pedido=pedido(pate, id, comidas, tiemp_est, precio)
        gestor_ped.cargar(un_pedido)
    archi_moto.close()
    archi_pedi.close()
    
    #menu de opciones
    seguir=1
    while seguir!=0:
        print("1.Cargar pedido: \n")
        print("2.Actualizar tiempo de entrega: \n")
        print("3.Mostrar datos del conductor: \n")
        
        opcion=int(input("Ingrese opcion ('0' para salir): "))
        
        if opcion==1:
            print("\nDATOS DEL PEDIDO:\n")
            id=int(input("\nId: "))
            comidas=input("\nComidas: ")
            tiemp_est=int(input("\nTiempo estimado de entrega: "))
            precio=float(input("\nPrecio: "))
            
            #Validar patente
            validar=False
            while validar!=True:
                patente_verif=input("\nAsignar a la moto (patente): ")
                validar=gestor_mo.validar_patente(patente_verif)
                if validar == True:
                    un_pedido=pedido(patente_verif, id, comidas, tiemp_est, precio)
                    gestor_ped.cargar(un_pedido)
                    #gestor_ped.agregar_arch()         
                    print("\nPEDIDO ASIGNADO")
                else:
                    print("La patente no es valida o no existe")
    
        elif opcion==2:
            gestor_ped.actu_tiempr()
        
        elif opcion==3:
            pate=gestor_mo.validar_conduct()
            prom=gestor_ped.calc_promedio(pate)
            print (f"Promedio de tiempo de entrega: {prom}")
            
        elif opcion==4:
            pass
        else:
            print("Opcion invalida")
            
        seguir=int(input("Seguir?('0' para finalizar): "))