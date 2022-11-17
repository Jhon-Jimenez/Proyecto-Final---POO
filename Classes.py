
class Usuario:
    def __init__(self, nombre: str, apellido: str, cc: int, dinero: float) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.cc = cc
        self.dinero = dinero

    def registrar_cliente(self) -> None:
        print("Hola usuario")
        print("Usted seleccionó registrar un nuevo cliente")
        print("Por favor ingrese los siguientes datos:")
        nombre = str(input("\nIngrese su nombre\n"))
        apellido = str(input("\nIngrese su apellido\n"))
        cc = int(input("\nIngrese su cedula\n"))
        dinero = float(input("\nIngrese la cantidad de dinero al abrir su cuenta\n"))
        print("\nNuevo cliente registrado\n")

        lista_clientes = []
        nuevo = Usuario(nombre,apellido,cc,dinero)
        lista_clientes.append(nuevo)

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


