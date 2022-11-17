
class Usuario:
    """
    Clase para cada usuario del banco
    """
    def __init__(self, nombre: str, apellido: str, cc: int, dinero: float) -> None:
        """
        Constructor de la clase usuario con sus atributos a utilizar.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.cc = cc
        self.dinero = dinero

    def ver_registros_usuarios(self) -> None:
        """
        Metodo para organizar y presentar los registros guardados para cada usuario registrado.
        """
        print("Número de cuenta: {}-{} {}-Saldo: {} ".format(self.cc, self.nombre, self.apellido, self.dinero))

    def ver_registros_historial(self) -> None:
        """
        Metodo para
        """
        print("Número de cuenta: {}-{} {}-Saldo: {} ".format(self.cc, self.nombre, self.apellido, self.dinero))      

lista_usuarios = [] # Lista para almacenar los usuarios registrados

def registrar_usuario() -> None:
    """
    Metodo para registrar nuevos usuarios.
    """
    print("\nUsted seleccionó registrar un nuevo usuario")
    print("Por favor ingrese los siguientes datos:")
    nombre = str(input("\nIngrese su nombre\n"))
    apellido = str(input("\nIngrese su apellido\n"))
    cc = int(input("\nIngrese su cedula, tenga en cuenta que esta será su número de cuenta\n"))
    dinero = float(input("\nIngrese la cantidad de dinero al abrir su cuenta\n"))
    print("\nNuevo cliente registrado\n")

    nuevo = Usuario(nombre,apellido,cc,dinero) # Para cada nuevo usuario registrado se crea un objeto de la clase Usuario.
    lista_usuarios.append(nuevo) # Cada objeto creado se agrega a la lista de usuarios.

def ver_lista_usuarios() -> None:
    """
    Metodo para ver la lista de usuarios guardados
    """
    print("\nUsted seleccionó ver la lista de usuarios registrados\n")

    for nuevo in lista_usuarios: # Se recorre la lista de usuarios con un for
        if len(lista_usuarios) == 0:
            print("Lo sentimos :(")
            print("La lista de usuarios está vacia. Intenta agregar un nuevo usuario ;)")
        nuevo.ver_registros_usuarios() # Se llama al metodo ver_registros_usuarios para organizar y mostrar la información
        
def buscar_usuario() -> None:
    """
    Metodo para buscar un usuario por medio de número de cedula
    """
    print("\nUsted seleccionó buscar usuario")
    cc = int(input("Ingrese el número de cuenta o la cedula del usuario a buscar\n"))

    for nuevo in lista_usuarios: # Se recorre la lista de usuarios con un for
        if cc == nuevo.cc: # Se compara el número de cedula ingresado
            print("")
            nuevo.ver_registros_usuarios() # Se llama al metodo ver_registros_usuarios para organizar y mostrar la información
            break
        else:
            print("Lo sentimos :(")
            print("El número de cuenta ingresado no se encuentrado registrado en nuestro sistema")    

lista_movimientos = [] # Lista para almacenar los movimientos de los usuarios

def ingresar_dinero() -> None:
    """
    Metodo para ingresar dinero a la cuenta de un usuario
    """
    print("\nUsted seleccionó ingresar dinero a su cuenta")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))
    
    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            ingreso = float(input("\nIngrese el valor a consignar en su cuenta\n"))
            while ingreso < 0:
                print("\nEl valor ingresado es incorrecto, ingrese un valor positivo")
                ingreso = float(input("\nIngrese el valor a consignar en su cuenta\n"))
            nuevo.dinero += ingreso
            print("\nTransacción exitosa")
            print("La transacción hecha fue:\n")
            historial_transaccion = print("Ingreso: {} - Saldo: {}".format(ingreso, nuevo.dinero))
            lista_movimientos.append(historial_transaccion)
            print("\nLuego de la transacción su cuenta quedó asi:\n")
            nuevo.ver_registros_usuarios()            

def retirar_dinero() -> None:
    """
    Metodo para retirar dinero de la cuenta de un usuario
    """
    print("\nUsted seleccionó retirar dinero de su cuenta")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))
    
    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            retiro = float(input("\nIngrese el valor a retirar en su cuenta\n"))
            while retiro > nuevo.dinero:
                print("\nEl valor ingresado es incorrecto, ingrese un valor menor al que tiene en la cuenta")
                retiro = float(input("\nIngrese el valor a retirar en su cuenta\n"))
            nuevo.dinero -= retiro
            print("\nTransacción exitosa")
            print("La transacción hecha fue:\n")
            historial_transaccion = print("Retiro: {} - Saldo: {}".format(retiro, nuevo.dinero))
            lista_movimientos.append(historial_transaccion)
            print("\nLuego de la transacción su cuenta quedó asi:\n")
            nuevo.ver_registros_usuarios()

def enviar_dinero() -> None:
   """
    Metodo para enviar dinero a la cuenta registrada de un amigo
   """
   print("Usted seleccionó enviar dinero a un amigo.") 
   print("\nTenga en cuenta que para utilizar esta opción su amigo debe estar registrado como un usuario en nuestro banco\n")
   num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))
   num_cuenta_amigo = int(input("Ingrese el número de cuenta o la cedula de su amigo\n"))
   dinero_envio = float(input("Ingrese la cantidad de dinero que va a enviar a su amigo. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))

   for nuevo in lista_usuarios:
    if num_cuenta == nuevo.cc:
        while dinero_envio > nuevo.dinero:
                print("\nLo sentimos, la cantidad de dinero asignada para enviar es mayor a la que tiene en su cuenta. Vuelva a intentarlo\n")
                dinero_envio = float(input("Ingrese la cantidad de dinero que va a enviar a su amigo. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))
        nuevo.dinero -= dinero_envio
        print("\nTransacción exitosa")
        print("La transacción hecha fue:\n")
        #historial_transaccion = print("Retiro: {} - Saldo: {}".format(dinero_envio, nuevo.dinero))
        #lista_movimientos.append(historial_transaccion)
        print("\nLuego de la transacción su cuenta quedó asi:\n")
        nuevo.ver_registros_usuarios()

    if num_cuenta_amigo == nuevo.cc:
        nuevo.dinero += dinero_envio
        print("\nTransacción exitosa")
        print("La transacción hecha fue:\n")
        #historial_transaccion = print("Ingreso: {} - Saldo: {}".format(dinero_envio, nuevo.dinero))
        #lista_movimientos.append(historial_transaccion)
        print("\nLuego de la transacción la cuenta de su amigo quedó asi:\n")
        nuevo.ver_registros_usuarios()

def ahorro_dinero() -> None:
   """
    Metodo para calcular el interes al ahorrar una cantidad de dinero por una cantidad de meses
   """
   print("\nUsted seleccionó ahorrar su dinero")
   print("\nPara utilizar esta opción ingrese:\n")
   num_cuenta = int(input("Su número de cuenta o su cedula\n"))
   dinero_ahorro = float(input("La cantidad de dinero que va ahorrar. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))
   meses_ahorro = int(input("La cantidad de meses que va a ahorrar su dinero. Tenga en cuenta que mientras sean más meses mayor será su ganancia\n"))

   for nuevo in lista_usuarios:
    if num_cuenta == nuevo.cc:
        while dinero_ahorro > nuevo.dinero:
            print("\nLo sentimos, la cantidad de dinero asignada para ahorrar es mayor a la que tiene en su cuenta. Vuelva a intentarlo\n")
            dinero_ahorro = float(input("La cantidad de dinero que va ahorrar. Tenga en cuenta que esta cantidad de dinero debe ser menor o igual a la que tiene en su cuenta\n"))
        interes = dinero_ahorro * 0.10
        ahorro = interes * meses_ahorro
        nuevo.dinero += ahorro
        print("\nAhorro exitoso")
        print("El ahorro hecho fue:\n")
        #historial_transaccion = print("Ahorro: {} - Saldo: {}".format(ahorro, nuevo.dinero))
        #lista_movimientos.append(historial_transaccion)
        print("\nLuego del ahorro su cuenta quedó asi:\n")
        nuevo.ver_registros_usuarios()

def ver_historial_movimientos() -> None:
    """
    Metodo para buscar y mostrar el historial de movimientos de la cuenta de un usuario registrado
    """
    print("\nUsted seleccionó ver su historial de movimientos")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))

    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            for historial_transaccion in lista_movimientos:
                print("Movimiento:\n{}".format(historial_transaccion))

        
            


