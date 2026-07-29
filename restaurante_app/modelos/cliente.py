class Cliente:
    def _init_(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | Correo: {self.correo}"
        )