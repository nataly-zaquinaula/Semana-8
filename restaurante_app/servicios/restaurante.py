from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def _init_(self) -> None:
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un Producto o una Bebida en la misma lista de
        productos (no se usan listas separadas). Valida que el codigo
        no este repetido.
        """
        if self._existe_codigo(producto.codigo):
            print(f"Error: ya existe un producto con el codigo '{producto.codigo}'.")
            return False

        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado correctamente.")
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente validando que la identificacion no se repita."""
        if self._existe_identificacion(cliente.identificacion):
            print(
                f"Error: ya existe un cliente con la identificacion "
                f"'{cliente.identificacion}'."
            )
            return False

        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado correctamente.")
        return True

    def listar_productos(self) -> None:
        """
        Lista todos los productos (incluye Productos y Bebidas juntos).
        Se llama a mostrar_informacion() de cada objeto sin usar
        condicionales para distinguir el tipo: esto es polimorfismo.
        """
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\n--- LISTADO DE PRODUCTOS ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print("\n--- LISTADO DE CLIENTES ---")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())

    def _existe_codigo(self, codigo: str) -> bool:
        """Metodo interno de apoyo para validar codigos duplicados."""
        return any(producto.codigo == codigo for producto in self.productos)

    def _existe_identificacion(self, identificacion: str) -> bool:
        """Metodo interno de apoyo para validar identificaciones duplicadas."""
        return any(
            cliente.identificacion == identificacion for cliente in self.clientes
        )