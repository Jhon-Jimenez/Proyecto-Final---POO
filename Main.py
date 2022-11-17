from Classes import Usuario, lista_usuarios, lista_movimientos, registrar_usuario, ver_lista_usuarios, buscar_usuario, ingresar_dinero, retirar_dinero, enviar_dinero, ahorro_dinero, ver_historial_movimientos

def main() -> None:
    sw = True
    while sw == True:
        print("*****************************************************")
        print("Bienvenido usuario :)")
        print("Esta es la app de su banco de confianza: Money House")
        print("*****************************************************")
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
            print("\nTenga en cuenta que para utilizar esta opción su amigo debe estar registrado como un usuario en nuestro banco\n")
            cont2 = int(input("¿Aún asi desea continuar? Ingrese 1 para si o 2 para no\n"))
            if cont2 == 1:
                print("\nUsted seleccionó enviar dinero a un amigo.")
                dinero = float(input("Ingrese la cantidad de dinero que va a enviar a su amigo. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))
            else:
                quit()
            enviar_dinero(dinero)
        elif opcion == 7:
            print("\nPara utilizar esta opción ingrese:\n")
            dinero = float(input("La cantidad de dinero que va ahorrar. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))
            meses = int(input("La cantidad de meses que va a ahorrar su dinero. Tenga en cuenta que mientras sean más meses mayor será su ganancia\n"))
            ahorro_dinero(dinero, meses)
        elif opcion == 8:
            ver_historial_movimientos()
        elif opcion == 9:
            print("\nGracias por usar mi banco Money House, su banco de confianza :)")
            quit()

        print("\n¿Quieres escoger otra opción?")
        cont = int(input("Ingrese 1 para si o 2 para no\n"))
        if cont == 2:
            print("\nGracias por usar mi banco Money House, su banco de confianza :)")
            sw = False
        else:
            while cont < 1 or cont > 2:
                print("\nEl valor ingresado es incorrecto, ingrese solo 1 o 2")
                cont = int(input("Ingrese 1 para si o 2 para no\n")) 

if __name__ == '__main__':
    main()            