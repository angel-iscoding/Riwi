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
    "price": float,
    "stock": int
}

"""

products = []

"""
Funciones claves para el manejo de inventario.
Permiten agregar, buscar, actualizar y eliminar productos. (CRUD).
"""

def add_product(name: str, price: float, stock: int) -> None:
    """
    Agrega un nuevo producto.
    
    :param name: Nombre del producto.
    :param price: Precio del producto.
    :param stock: Cantidad disponible.
    """

    products.append({
        "name": name,
        "price": price,
        "stock": stock
    })

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

def update_product(name: str, price: float = None, stock: int = None) -> bool:
    """
    Actualiza los datos de un producto si es encontrado.
    
    :param name: Nombre del producto para actualizar (Necesario para buscar producto).
    :param price: Nuevo precio del producto (optional).
    :param stock: Nueva cantidad de productos disponibles (optional).
    """

    for product in products:
        if product["name"] == name:
            if price is not None:
                product["price"] = price
            if stock is not None:
                product["stock"] = stock
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
Funcion de compra de carrito.
"""

def buy_cart() -> None:
    """
    Simula la compra del carrito de compras.
    
    Suma el precio de todos los productos dentro del carrito y pide confirmación del usuario.
    """

"""
Funciones de utilidad para el manejo de interfaz para el usuario.
"""

def clear(): 
    os.system("clear")

def IU (msj: str) -> str:
    # Variables constantes en la elaboración del menú
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

"""
Main code.
"""

def main():
    print(IU("Hela"))

if __name__ == "__main__":
    main()