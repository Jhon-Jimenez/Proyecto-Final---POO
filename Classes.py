
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
    print("\nHola usuario")
    print("Usted seleccionó ver la lista de usuarios registrados\n")

    for nuevo in lista_usuarios: # Se recorre la lista de usuarios con un for
        nuevo.ver_registros_usuarios() # Se llama al metodo ver_registros_usuarios para organizar y mostrar la información
        
def buscar_usuario() -> None:
    """
    Metodo para buscar un usuario por medio de número de cedula
    """
    print("\nUsted seleccionó buscar usuario")
    cc = int(input("Ingrese el número de cuenta o la cedula del usuario a buscar\n"))

    for nuevo in lista_usuarios: # Se recorre la lista de usuarios con un for
        if cc == nuevo.cc: # Se compara el número de cedula ingresado
            nuevo.ver_registros_usuarios() # Se llama al metodo ver_registros_usuarios para organizar y mostrar la información

lista_movimientos = []

def ingresar_dinero() -> None:
    print("\nUsted seleccionó ingresar dinero a su cuenta")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))
    
    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            ingreso = float(input("\nIngrese el valor a consignar en su cuenta"))
            print("Iniciando transacción...\n")
            ingreso + nuevo.dinero
            print("\nTransacción exitosa")
            print("La transacción hecha fue:\n")
            historial_transaccion = print("Ingreso: {}\nSaldo: {}".format(ingreso, nuevo.dinero))
            lista_movimientos.append(historial_transaccion)
            print("Luego de la transacción su cuenta quedó asi:\n")
            nuevo.ver_registros_usuarios()            

def retirar_dinero() -> None:
    print("\nUsted seleccionó retirar dinero a su cuenta")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))
    
    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            retiro = float(input("\nIngrese el valor a retirar en su cuenta"))
            print("Iniciando transacción...\n")
            retiro - nuevo.dinero
            print("\nTransacción exitosa")
            print("La transacción hecha fue:\n")
            historial_transaccion = print("Retiro: {}\nSaldo: {}".format(retiro, nuevo.dinero))
            lista_movimientos.append(historial_transaccion)
            print("Luego de la transacción su cuenta quedó asi:\n")
            nuevo.ver_registros_usuarios()

def enviar_dinero() -> None:
    pass

def ahorro_dinero(self, cantidad: float, años: int) -> None:
   pass

def ver_historial_movimientos() -> None:
    print("\nUsted seleccionó ver su historial de movimientos")
    num_cuenta = int(input("Ingrese su número de cuenta o su cedula\n"))

    for nuevo in lista_usuarios:
        if num_cuenta == nuevo.cc:
            for historial_transaccion in lista_movimientos:
                print("Movimiento:{}".format(historial_transaccion))

        
            


