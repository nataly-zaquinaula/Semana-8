from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========================================")
    print("           SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")
    codigo: str = input("Codigo: ")
    nombre: str = input("Nombre: ")
    categoria: str = input("Categoria: ")
    precio: float = float(input("Precio: "))

    producto = Producto(codigo, nombre, categoria, precio)
    restaurante.registrar_producto(producto)


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\n--- Registrar bebida ---")
    codigo: str = input("Codigo: ")
    nombre: str = input("Nombre: ")
    categoria: str = input("Categoria: ")
    precio: float = float(input("Precio: "))
    tamano: str = input("Tamano (ej. pequena, mediana, grande): ")

    bebida = Bebida(codigo, nombre, categoria, precio, tamano)
    restaurante.registrar_producto(bebida)


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\n--- Registrar cliente ---")
    identificacion: str = input("Identificacion: ")
    nombre: str = input("Nombre: ")
    correo: str = input("Correo: ")

    cliente = Cliente(identificacion, nombre, correo)
    restaurante.registrar_cliente(cliente)


def main() -> None:
    restaurante = Restaurante()
    opcion: str = ""

    while opcion != "6":
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            restaurante.listar_productos()
        elif opcion == "5":
            restaurante.listar_clientes()
        elif opcion == "6":
            print("\nSaliendo del sistema...")
        else:
            print("\nOpcion invalida, intente de nuevo.")


if _name_ == "_main_":
    main()
    