
class Usuario:
    def __init__(self, nombre: str, cc: str, dinero: float) -> None:

        self.nombre = nombre
        self.cc = cc
        self.dinero = dinero

class Banco:
    def __init__(self, nombre_banco: str) -> None:

        self.nombre_banco = nombre_banco

class Negocio:
    def __init__(self, nombre_negocio: str, tipo_negocio: str) -> None:

        self.nombre_negocio: nombre_negocio
        self.tipo_negocio: tipo_negocio

