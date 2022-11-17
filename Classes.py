
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

lista_usuarios = [] # Lista para almacenar los usuarios registrados

def registrar_usuario() -> None:
    """
    Metodo para registrar nuevos usuarios.
    """
    print("\nHola usuario")
    print("Usted seleccionó registrar un nuevo usuario")
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
    print("\nHola usuario")
    print("Usted seleccionó buscar usuario")
    cc = int(input("Ingrese el número de cuenta o cedula del usuario a buscar\n"))

    for nuevo in lista_usuarios: # Se recorre la lista de usuarios con un for
        if cc == nuevo.cc: # Se compara el número de cedula ingresado
            nuevo.registros_usuarios() # Se llama al metodo ver_registros_usuarios para organizar y mostrar la información

class Banco:
    def __init__(self, ingreso: float, retiro: float) -> None:
        self.ingreso = ingreso
        self.retiro = retiro



def ahorro_dinero(self, cantidad: float, años: int) -> None:
           pass

class Negocio:
    def __init__(self, nombre_negocio: str, tipo_negocio: str) -> None:

        self.nombre_negocio: nombre_negocio
        self.tipo_negocio: tipo_negocio
        
            


