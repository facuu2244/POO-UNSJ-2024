from calseCajaAhorro import cajaDeAhorro

def test():
    lista=[]
    print("CREANDO OBJETOS:\n")
    
    for i in range(2):
        print("Datos caja ", i+1)
        numcaja=i+1
        nombre=input("Ingrese nombre del titular: ")
        ape=input("Apellido: ")
        cuil=input("Ingrese ciul:")
        
        lista.append(cajaDeAhorro(numcaja, nombre, ape, cuil))
    
    seguir=1
    
    while seguir!=0:     
        print("MENU DE OPCIONES: \n")
        print("1.Mostrar datos de cuenta: \n")
        print("2.Exreaer plata: \n")
        print("3.Depositar: \n")
        print("4.Verificar CUIL: \n")
        
        opcion=int(input("Ingrese opcion: "))
        cuenta=int(input("Numero de cuenta que desea realiar la opcion: "))
        
        if opcion==1:
            lista[cuenta-1].mostrar()
            
        elif opcion==2:
            monto=float(input("Monto que desea extraer: "))
            lista[cuenta-1].extraer(monto)
        
        elif opcion==3:
            depo=float(input("Monto que desea depositar: "))
            lista[cuenta-1].depositar(depo)
        
        elif opcion==4:
            cuil=input("Cuil a validar: ")
            lista[cuenta-1].validar(cuil)
            
        else:
            print("Opcion invalida:")
            
        seguir=int(input("Seguir? (Ingrese '1' para seguir o distinto de '1' para finalizar): "))

    
if __name__ == "__main__":  
    test()