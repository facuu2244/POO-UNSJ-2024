from claseCajaAhorro import cajaDeAhorro
from contenedor import contenedor

def test():
    
    print("CREANDO OBJETOS:\n")
    conte=contenedor()
    conte.cargar()
    
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
            contenedor.lista[cuenta-1].mostrar()
            
        elif opcion==2:
            monto=float(input("Monto que desea extraer: "))
            contenedor.lista[cuenta-1].extraer(monto)
        
        elif opcion==3:
            depo=float(input("Monto que desea depositar: "))
            contenedor.lista[cuenta-1].depositar(depo)
        
        elif opcion==4:
            cuil=input("Cuil a validar: ")
            contenedor.lista[cuenta-1].validar(cuil)
            
        else:
            print("Opcion invalida:")
            
        seguir=int(input("Seguir? (Ingrese '1' para seguir o distinto de '1' para finalizar): "))

    
if __name__ == "__main__":  
    test()