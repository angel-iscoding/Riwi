import os

"""
Módulo de gestión de inventarios.
Permite agregar, buscar, actualizar y eliminar productos de un inventario.
Contiene una funcion para simular la compra de un carrito de compras.
"""

"""
Lista de productos. Contiene un diccionario con la estructura de los productos.

product = {
    "name": str,
    "price": tuple,  
    "stock": int
}

"""

products = []

"""
Funciones claves para el manejo de inventario.
Permiten agregar, buscar, actualizar y eliminar productos. (CRUD).
"""

def add_product(name: str, price: tuple, stock: int) -> bool:
    """
    Agrega un nuevo producto.
    
    :param name: Nombre del producto.
    :param price: Precio del producto.
    :param stock: Cantidad disponible.
    """
    try:
        products.append({
            "name": name,
            "price": price,
            "stock": stock
        })
        return True
    
    except Exception as e:
        print(f"Error al agregar el producto: {e}")
        return False

def search_product(name: str) -> dict:
    """
    Busca un producto en el diccionario.
    
    :param name: Nombre del producto encontrado.
    :return: Retorna el diccionario, en caso contario, retorna None.
    """

    for product in products:
        if product["name"] == name:
            return product
        return None

def update_product(name: str, price: tuple = None, stock: int = None) -> bool:
    """
    Actualiza los datos de un producto si es encontrado.
    
    :param name: Nombre del producto para actualizar (Necesario para buscar producto).
    :param price: Nuevo precio del producto (optional).
    :param stock: Nueva cantidad de productos disponibles (optional).
    """

    for product in products:
        if product["name"] == name:
            if price is not None:
                product["price"] = (price)
            if stock is not None:
                product["stock"] = (stock)
            return True
    return False

def delete_product(name: str) -> bool:
    """
    Elimina un producto del diccionario.
    
    :param name: Nombre del producto a borrar.
    """

    for i, product in enumerate(products):
        if product["name"] == name:
            del products[i]
            return True
    return False


"""
Funcion de cálculo del precio total del inventario.
"""

def invetory_price() -> float:
    """
    Calcula el precio total del inventario usando una función lambda.
    Suma (precio_unitario * (1 - descuento/100)) * stock para cada producto.
    """
    return sum(
        map(
            lambda product: (product["price"][0] * (1 - product["price"][1] / 100)) * product["stock"],
            products
        )
    )

"""
Funciones de manejo de acciones del usuario.
"""

def option_add() -> None:
    """
    Permite al usuario agregar un nuevo producto al inventario.
    Solicita el nombre, precio unitario, porcentaje de descuento y stock del producto.
    """

    nombre = input(f"{UI(f"Ingrese el nombre del producto")}\nUsuario -> ")
    precio_unitario = float(f"{UI_parseInt("Ingrese el precio unitario del producto")}")
    descuento = float(f"{UI_parseInt("Ingrese el porcentaje descuento del producto")}")
    stock = UI_parseInt(f"Ingrese la cantidad de productos disponibles")

    precio = (precio_unitario, descuento)

    if not nombre:
        print(UI("El nombre del producto a eliminar no puede estar vacio."))
        input()
        return

    if search_product(nombre):
        print(UI(f"El producto {nombre} ya existe."))
        input()
        return 
    
    if precio_unitario < 0 or descuento < 0 or stock < 0:
        print(UI("El precio, el descuento y el stock deben ser mayores a 0."))
        input()
        return 

    if not nombre:
        print(UI("El nombre del producto no puede estar vacio."))
        input()
        return 

    if add_product(nombre, precio, stock):
        print(UI(f"Producto {nombre} agregado exitosamente."))
    else:
        print(UI("Error al agregar el producto. Intente nuevamente."))

    input()

def option_search() -> None:
    """
    Permite al usuario buscar un producto por su nombre.
    Solicita el nombre del producto a buscar.
    Si el producto es encontrado, muestra sus detalles.
    """
    nombre = input(f"{UI(f"Ingrese el nombre del producto\n")}\nUsuario -> ")

    if not nombre:
        print(UI("El nombre del producto a buscar no puede estar vacio."))
        input()
        return 

    product = search_product(nombre)

    if product:
        print(UI(f"Producto encontrado: {product}")) 
    else:
        print(UI(f"Producto {nombre} no encontrado."))
    input()

def option_update() -> None:
    """
    Permite al usuario actualizar un producto existente.
    Solicita el nombre del producto a actualizar y los nuevos valores (precio, descuento, stock).
    Si el producto es encontrado, actualiza sus detalles.
    """

    nombre = input(f"{UI(f"Ingrese el nombre del producto a actualizar")}\nUsuario -> ")

    if not nombre:
        print(UI("El nombre del producto a eliminar no puede estar vacio."))
        input()
        return

    if not search_product(nombre):
        print(UI(f"Producto {nombre} no encontrado."))
        input()
        return

    # Pedir los nuevos valores (pueden dejarse en blanco para no actualizar)
    precio_unitario = float(UI_parseInt("Ingrese el nuevo precio unitario del producto (Enter para omotir):\n"))
    descuento = float(UI_parseInt("Ingrese el nuevo porcentaje descuento del producto (Enter para omotir):\n"))
    stock = UI_parseInt("Ingrese la nueva cantidad de productos disponibles (Enter para omitir):\n")

    # Procesar los valores ingresados
    if precio_unitario < 0 or descuento < 0 or stock < 0:
        print(UI("Ningun valor puede estar por debajo de 0."))
        input()
        return

    if precio_unitario == 0 and descuento == 0:
        print(UI("No se ha ingresado un nuevo precio o descuento. No se actualizará el producto."))
        input()
        return

    precio = (precio_unitario, descuento)

    if stock == 0:
        print(UI("No se ha ingresado una nueva cantidad de productos disponibles. No se actualizará el producto."))
        input()
        return

    if update_product(nombre, precio, stock):
        print(UI(f"Producto {nombre} actualizado exitosamente."))
    else:
        print(UI("Error al actualizar el producto. Intente nuevamente."))
    
    input()

def option_delete() -> None:
    """
    Permite al usuario eliminar un producto del inventario.
    Solicita el nombre del producto a eliminar.
    Si el producto es encontrado, lo elimina del inventario.
    """

    nombre = input(f"{UI(f"Ingrese el nombre del producto a eliminar")}\nUsuario -> ")

    if not nombre:
        print(UI("El nombre del producto a eliminar no puede estar vacio."))
        input()
        return

    if not search_product(nombre):
        print(UI(f"Producto {nombre} no encontrado."))
        return 

    if delete_product(nombre):
        print(UI(f"Producto {nombre} eliminado exitosamente."))
    else:
        print(UI("Error al eliminar el producto. Intente nuevamente."))

    input()


"""
Funciones de utilidad para el manejo de interfaz para el usuario.
"""

def clear(): 
    os.system("clear")

def UI (msj: str) -> str:
    # Variables constantes en la elaboración del menú
    clear()
    size = 100
    border_char = "∙"
    fill_char = "⎯"
    line_char = " "
    side_char_l = "⎢"
    side_char_r = "⎥"
    
    # Construir encabezado del menú
    message = f"{border_char}{fill_char * (size - 2)}{border_char}"
    
    # Procesa cada línea del mensaje
    for line in msj.splitlines():
        line_length = len(line) 

        # Ajustar línea si es impar
        if line_length % 2 == 1:
            #Agrega un espacio para que todos coincidan
            line += " "
            
        line_length = len(line)
        
        # Calcular el padding
        total_padding = size - 2 - line_length
        padding = total_padding // 2
        
        # Agregar línea al menú
        message += f"\n{side_char_l}{line_char * padding}{line}{line_char * padding}{side_char_r}"
    
    # Construir pie del menú
    message += f"\n{border_char}{fill_char * (size - 2)}{border_char}"
    
    return message
    
def UI_parseInt(message: str) -> int:
    """
    Valida el tipo de dato ingresado por el usuario.
    
    :param message: Mensaje que se muestra al usuario para solicitar un dato.
    :return: Retorna el dato transformado en entero
    :raises: Si el dato ingresado no es un entero, se vuelve a solicitar al usuario.

    """
    clear()
    
    try: 
        value = int(input(f"{UI(message)}\nUsuario -> ")) 

        if value < 0 and not value is None:
            print(UI("Debe ingresar un numero entero positivo. Intente nuevamente."))
            input()
            return UI_parseInt(message)

        return value 

    except:
        print(UI("Debe ingresar un numero valido. Intente nuevamente."))
        input()
        return UI_parseInt(message)

"""
Main code.
"""

def menu(option: int = 0) -> bool:
    """
    Muestra el menú de opciones y maneja la selección del usuario.
    :param option: Opción seleccionada por el usuario.
    :return: Retorna True si el usuario desea continuar, False si desea salir.
    :raises: Si la opción no es válida, se vuelve a mostrar el menú.
    """
    
    try: 
        match option:
            case 0:
                return False
            case 1:
                option_add()    
            case 2:
                option_search()    
            case 3:
                option_update()    
            case 4:
                option_delete()    
            case 5:
                print(UI(f"El precio total del inventario es: {invetory_price()}"))
                pass
            case _:
                print(UI("Opcion no valida, por favor intente de nuevo."))
        
        # Preguntar al usuario si desea continuar
        continue_option = input(f"{UI("¿Desea continuar? (s/n): ")}\nUsuario -> ").strip().lower()
        
        if continue_option == 's':
            return True
        elif continue_option == 'n':
            input("true")
            return False
        else:
            print(UI("Opcion no valida... Se reiniciara el menu."))
            input()
            return True
    except:
        # Si ocurre un error, preguntar al usuario si desea salir del programa
        while not input(f"{UI("Opcion no valida. ¿Desea salir del programa? (s/n)")}\nUsuario -> ").strip().lower() in ['s', 'n']:
            print(UI("Opcion no valida. Por favor, intente de nuevo."))
        
        if continue_option == 's':
            return False
        else:
            return True

def main():
    """
    Función principal que inicia el programa de gestión de inventarios.
    Muestra un mensaje de bienvenida y el menú de opciones."""
    msj_menu = ("Bienvenido al sistema de gestion de inventarios.\n\n"
            "Seleccione una opcion:\n\n"
            "1. Agregar producto\n"
            "2. Buscar producto\n"
            "3. Actualizar producto\n"
            "4. Eliminar producto\n"
            "5. Ver precio total del inventario\n"
            "0. Salir del programa\n\n")

    #Si la funcion menu retorna True, se vuelve a mostrar el menu
    #Si retorna False, se sale del programa
    while menu(UI_parseInt(msj_menu)):
        pass


    print(UI("Gracias por usar el sistema de gestion de inventarios."))
    input()   

if __name__ == "__main__":
    main()