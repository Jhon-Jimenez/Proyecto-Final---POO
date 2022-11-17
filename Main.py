    
def main() -> None:
        print("Bienvenido usuario :)")
        print("Esta es mi app de simulación de un banco: Money House")
        print("")
        print("¿Que te gustaria hacer hoy?")
        print("1. Registrar un nuevo usuario")
        print("2. Buscar un usuario")
        print("3. Ver la lista de usuarios")
        print("4. Ingresar dinero")
        print("5. Retirar dinero")
        print("6. Ver el historial de transacciones")
        opcion = int(input("\nIngrese el numero de una opción para relizar alguna operación especifica:\n"))

        while opcion < 1 or opcion > 6:
            print("\nEl valor ingresado es incorrecto, intentelo de nuevo")
            opcion = int(input("Ingrese el numero de una opción para relizar alguna operación especifica:\n"))

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass   

if __name__ == '__main__':
    main()            