from modelos.producto import Producto

class Bebida(Producto):
    def _init_(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
    ) -> None:
        # Se reutiliza el constructor de Producto para no repetir codigo
        super()._init_(codigo, nombre, categoria, precio)
        self.tamano: str = tamano

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el metodo de Producto para incluir el tamano de la
        bebida. Este es el polimorfismo que se usa en el listado de
        productos: el servicio llama a mostrar_informacion() sin saber
        si el objeto es un Producto o una Bebida.
        """
        info_producto = super().mostrar_informacion()
        return f"{info_producto} | Tamano: {self.tamano} (Bebida)"