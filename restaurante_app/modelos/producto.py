class Producto:
    def _init_(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """
        Devuelve un texto con la informacion del producto.
        La clase Bebida sobrescribe este metodo (principio O y L de SOLID),
        por lo que el servicio puede llamar a este mismo metodo sin
        importar si el objeto es un Producto o una Bebida.
        """
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: ${self.precio:.2f}"
        )