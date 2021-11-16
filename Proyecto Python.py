from datetime import datetime
saldo=800
dolar=66000
hora=datetime.now()
print("\t.:MENU:.")
print("1. Recibir dinero")
print("2. Transferir")
print("3. Conocer valor actual")
print("4. Salir del programa")
opcion = int(input("Que desea Hacer (Ingrese una opción valida): "))
print()
if opcion==1:
    def monedadigital(cripto):
        criptos=["BTC", "LTC", "ETH"]
        if cripto in criptos:
            return True
        else:
            return False
    monedaDigital=""
    while not monedadigital(monedaDigital):
        monedaDigital = input("ingrese la moneda Digital a Recibir (BTC, LTC o ETH): ")
    cantidad=float(input("Ingrese la cantidad de " +monedaDigital+ " a Recibir: "))
    codigo=input("Ingrese Codigo de transacción: ")
    print("Transacción realizada con exito. Moneda recibida: " +monedaDigital+ " Cantidad: ", str(cantidad), ". El total en su Wallet es de: ", str(saldo + cantidad))
    print(hora.strftime("%A %D %B %Y"))
elif opcion==2:
    def monedadigital(cripto):
        criptos=["BTC", "LTC", "ETH"]
        if cripto in criptos:
            return True
        else:
            return False
    monedaDigital=""
    while not monedadigital(monedaDigital):
        monedaDigital = input("ingrese la moneda Digital a Transferir (BTC, LTC o ETH): ")
    cantidad=float(input("Ingrese la cantidad de " +monedaDigital+ " a Transferir: "))
    while cantidad>saldo:
        print("No tiene saldo suficiente")
        cantidad = float(input("Ingrese la cantidad de " + monedaDigital + " a Transferir: "))
    codigo=input("Ingrese Codigo de transacción: ")
    print("Transacción realizada con exito. Moneda Transferida: " +monedaDigital+ " Cantidad Transferida: ", str(cantidad), "Codigo: ", str(codigo), ". El total en su Wallet es de: ", str(saldo - cantidad))
    print(hora.strftime("%A %D %B %Y"))
elif opcion==3:
    def monedadigital(cripto):
        criptos=["BTC", "LTC", "ETH"]
        if cripto in criptos:
            return True
        else:
            return False
    monedaDigital=""
    while not monedadigital(monedaDigital):
        monedaDigital = input("ingrese una moneda Digital para conocer su valor (BTC, LTC o ETH): ")
    cantidad=float(input("ingrese la cantidad de " +monedaDigital+ " que desa calcular: "))
    print("La cantidad indicada corresponde a: ", str(dolar * cantidad), " USD")
    print(hora.strftime("%A %D %B %Y"))
else:
    print("Muchas gracias")