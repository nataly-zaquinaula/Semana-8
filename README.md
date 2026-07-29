# Sistema de Restaurante
Estudiante: Nataly Zaquinaula.
## Descripcion del sistema
Sistema de consola en Python que gestiona productos, bebidas y clientes de un restaurante. Permite registrar y listar productos (incluyendo bebidas) y clientes mediante un menu interactivo.
## Responsabilidad de cada clase
Producto (modelos/producto.py): representa los datos comunes de un producto del restaurante (codigo, nombre, categoria, precio) y define el metodo mostrar_informacion().
Bebida (modelos/bebida.py): clase hija de Producto. Agrega el atributo tamano y sobrescribe mostrar_informacion() para mostrar su propia informacion.
Cliente (modelos/cliente.py): representa los datos de un cliente registrado (identificacion, nombre, correo). No tiene relacion de herencia con Producto.
Restaurante (servicios/restaurante.py): clase de servicio que administra las listas de productos y clientes, y sus operaciones de registro, validacion y listado.
main.py: punto de arranque del programa. Muestra el menu, solicita datos con input(), crea los objetos y llama a los metodos del servicio Restaurante.
## Relacion entre Producto y Bebida
Bebida hereda de Producto porque una bebida ES un tipo de producto del restaurante. Gracias a esta herencia, Producto y Bebida se pueden guardar en la misma lista, y al listarlos se llama al mismo metodo mostrar_informacion() sin necesidad de preguntar de que tipo es cada objeto (polimorfismo).
## Principios SOLID aplicados
S - Responsabilidad unica: Producto y Bebida representan productos, Cliente representa un cliente, Restaurante administra las colecciones, y main.py solo coordina la interaccion por consola.
O - Abierto/cerrado: Bebida amplia el sistema mediante una nueva implementacion (herencia) sin modificar la logica general del servicio Restaurante.
L - Sustitucion de Liskov: un objeto Bebida puede usarse como un Producto (por ejemplo, dentro de la lista de productos) sin generar errores ni alterar el comportamiento esperado del programa.
## Reflexion
Diseñar el proyecto separando modelos y servicios facilita el mantenimiento del sistema: si en el futuro se necesita agregar un nuevo tipo de producto (por ejemplo, un postre), basta con crear una nueva clase hija de Producto sin modificar el resto del codigo. Esto demuestra la importancia de aplicar principios SOLID desde el inicio de un proyecto.