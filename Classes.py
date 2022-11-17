
class Usuario:
    def __init__(self, nombre: str, apellido: str, cc: int, dinero: float) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.cc = cc
        self.dinero = dinero

    def registrar_usuario(self) -> None:
        print("Hola usuario")
        print("Usted seleccionó registrar un nuevo usuario")
        print("Por favor ingrese los siguientes datos:")
        nombre = str(input("\nIngrese su nombre\n"))
        apellido = str(input("\nIngrese su apellido\n"))
        cc = int(input("\nIngrese su cedula, tenga en cuenta que esta será su número de cuenta\n"))
        dinero = float(input("\nIngrese la cantidad de dinero al abrir su cuenta\n"))
        print("\nNuevo cliente registrado\n")

        lista_usuarios = []
        nuevo = Usuario(nombre,apellido,cc,dinero)
        lista_usuarios.append(nuevo)

    def ver_lista_usuarios(self) -> None:
        print("Hola usuario")
        print("Usted seleccionó ver la lista de usuarios registrados\n")
        
    def buscar_usuario(self) -> None:
        print("Hola usuario")
        print("Usted seleccionó buscar usuario")
        cc = int(input("Ingrese el número de cuenta o cedula del usuario a buscar"))
        

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


