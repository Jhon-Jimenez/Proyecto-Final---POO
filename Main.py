from Classes import Usuario, lista_usuarios, lista_movimientos, registrar_usuario, ver_lista_usuarios, buscar_usuario, ingresar_dinero, retirar_dinero, enviar_dinero, ahorro_dinero, ver_historial_movimientos

def main() -> None:
    sw = True
    print("*****************************************************")
    print("Bienvenido usuario :)")
    print("Esta es la app de su banco de confianza: Money House")
    print("*****************************************************")

    while sw == True:
        print("\n¿Que te gustaria hacer hoy?")
        print("1. Registrar un nuevo usuario")
        print("2. Buscar un usuario")
        print("3. Ver la lista de usuarios")
        print("4. Ingresar dinero")
        print("5. Retirar dinero")
        print("6. Enviar dinero a un amigo")
        print("7. Ahorrar dinero")
        print("8. Ver el historial de transacciones")
        print("9. Salir") 
        opcion = int(input("\nIngrese el numero de una opción para relizar alguna operación especifica:\n"))

        while opcion < 1 or opcion > 9:
            print("\nEl valor ingresado es incorrecto, intentelo de nuevo")
            opcion = int(input("Ingrese el numero de una opción para relizar alguna operación especifica:\n"))

        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            buscar_usuario()
        elif opcion == 3:
            ver_lista_usuarios()
        elif opcion == 4:
            ingresar_dinero()
        elif opcion == 5:
            retirar_dinero()
        elif opcion == 6:
            enviar_dinero()
        elif opcion == 7:
            ahorro_dinero()
        elif opcion == 8:
            ver_historial_movimientos()
        elif opcion == 9:
            print("\nGracias por usar los servicios del banco Money House, su banco de confianza :)")
            quit()

        print("\n¿Quieres escoger otra opción?")
        cont = int(input("Ingrese 1 para si o 2 para no\n"))
        if cont == 2:
            print("\nGracias por usar los servicios del banco Money House, su banco de confianza :)")
            sw = False
        else:
            while cont < 1 or cont > 2:
                print("\nEl valor ingresado es incorrecto, ingrese solo 1 o 2")
                cont = int(input("Ingrese 1 para si o 2 para no\n")) 

if __name__ == '__main__':
    main()            