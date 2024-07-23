import numpy as np
from gestor import gestor

if __name__ == '__main__':
    gestor=gestor()
    
    seguir=1
    
    print("---------MENU DE OPCIONES---------")
    
    while seguir!=0:
        print("1.Cargar venta: \n")
        print("2.Calcular total por sucursal: \n")
        print("3.Sucursal que mas facturo: \n")
        print("4.Ver sucursal con menos facturacion: \n")
        print("5.Ver total facturado por cada sucursal: \n")
        
        opcion=int(input("Ingrese opcion ('0' para salir): "))
    
        if opcion==1:
            dia=int(input("\nIngrese dia de la semana: "))
            num=int(input("\nNumero de sucursal: "))
            imp=float(input("\nImporte de la factura: "))
            gestor.cargar(dia, num, imp)
            gestor.mostrar()
        
        elif opcion==2:
            num=int(input("\nNumero de sucursal: "))
            gestor.total_suc(num)
        
        elif opcion==3:
            dia=int(input("\nIngrese dia: "))
            gestor.calc_dia(dia)
        
        elif opcion==4:
            gestor.menos_factu()
        
        elif opcion==5:
            gestor.total_sucu()
            
        else:
            print("Opcion Invalida")
            
        seguir=int(input("Seguir? (Ingrese distinto de '0' para seguir): "))