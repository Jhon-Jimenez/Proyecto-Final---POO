    
def main() -> None:
        print("Bienvenido usuario")
        print("Esta es mi app de simulación de banco: Money House")
        print("¿Que te gustaria hacer hoy?")
        opcion = int(input("Ingrese el numero de una opción para relizar alguna operación especifica:"))

        while opcion < 1 or opcion > 6:
            print("El valor ingresado es incorrecto, intentelo de nuevo")    

if __name__ == '__main__':
    main()            