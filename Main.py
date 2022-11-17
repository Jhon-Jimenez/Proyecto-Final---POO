from Classes import lista_usuarios, registrar_usuario, ver_lista_usuarios, buscar_usuario

def main() -> None:
    sw = True
    while sw == True:
        print("\nBienvenido usuario :)")
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
            registrar_usuario()
        elif opcion == 2:
            buscar_usuario()
        elif opcion == 3:
            ver_lista_usuarios()
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass 

        print("\n¿Quiere escoger otra opción?")
        cont = int(input("Ingrese 1 para si o 2 para no\n"))
        if cont == 2:
            sw = False
        else:
            while cont < 1 or cont > 2:
                print("\nEl valor ingresado es incorrecto, ingrese solo 1 o 2")
                cont = int(input("Ingrese 1 para si o 2 para no\n")) 

if __name__ == '__main__':
    main()            