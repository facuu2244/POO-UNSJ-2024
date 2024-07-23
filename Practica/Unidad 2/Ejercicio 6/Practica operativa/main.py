from gestorClientes import gestor_cliente
from gestorMovimietos import gestor_movimiento

if __name__ == '__main__':
    
    ruta_clientes="ClientesFarmaCiudad.csv"
    ruta_movimientos="MovimientosAbril2024.csv"
    
    lista_clientes=gestor_cliente()
    lista_clientes.cargar(ruta_clientes)
    
    lista_movimientos=gestor_movimiento()
    lista_movimientos.cargar(ruta_movimientos)
    
    seguir = 1
    while seguir != 0:
        print('---------------MENU DE OPCIONES---------------')
        print('1. Ver datos del cliente')
        print('2. Consultar si un cliente tuvo movimientos')
        print('3. Ordenar movimientos por numero de cuenta')
    
        opcion=int(input('Ingrese opcion: '))
        if opcion==1:
            dni=int(input("Ingrese dni del cliente: "))
            cliente, num_cuenta, saldo=lista_clientes.verificar_cliente(dni)
            
            if cliente!=False:
                lista_movimientos.actu_saldo(num_cuenta, saldo)                
            else:
                print("Cliente no encontrado")
        elif opcion==2:
            dni=int(input("Ingrese DNI del cliente: "))
            num, nom, ape=lista_clientes.buscar(dni)
            lista_movimientos.validar_movi(num, nom, ape)
            
        elif opcion==3:
            lista_movimientos.ordenar()
        seguir = int(input('Seguir: '))