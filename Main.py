    
def main() -> None:
        print("Bienvenido usuario")
        print("Esta es mi app de simulación de un banco: Money House")
        print("")
        print("¿Que te gustaria hacer hoy?")
        print("1. Registrar un nuevo cliente")
        print("2. Buscar un cliente")
        print("3. Ver la lista de clientes")
        print("4. Ingresar dinero")
        print("5. Retirar dinero")
        print("6. Historial de transacciones")
        
        print("")
        opcion = int(input("Ingrese el numero de una opción para relizar alguna operación especifica:"))

        while opcion < 1 or opcion > 6:
            print("El valor ingresado es incorrecto, intentelo de nuevo")

        if opcion == 1:
            print("1")
        elif opcion == 2:
            print("2")
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("5")
        elif opcion == 6:
            print("6")      

if __name__ == '__main__':
    main()            