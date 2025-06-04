cart = [
    {
        "name": "Manzana",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    },
    {
        "name": "Pera",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    },
    {
        "name": "Fresa",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    }
]

menu = """
(1) Ver carrito

(2) Agregar al carrito

(3) Eliminar del carrito

(4) Realizar compra

Seleccione una opcion: """

exit_aplication = 2

while exit_aplication == 2:
    
    print("¡Bienvenido a su Ecommerce favorito!")

    option = 0
    
    option = int(input(menu))

    if (option == 1):
        print("\nMostrando productos en el carrito\n")

        total = 0 
        discount = 0

        for index, product in enumerate(cart): 
            print(f"Producto #{index + 1}.")
            print(f"Nombre: {product['name']}")
            print(f"Precio: {product['price']}")
            print(f"Cantidad: {product['stock']}")
            print(f"Descuento: {product['discount']}\n")

            discount = product["price"] * product["discount"]/100
            total += product["price"] - discount

        print(f"Total carrito: {total}")

    elif (option == 2):
        print("\nAgregar nuevo producto.\n")

        name = input("Nombre del producto: ")
        price = input("Precio del producto: ")
        stock = input("Cantidad de products: ")
        discount = input("Descuento (Solo numero): ")

        new_product = {
            "name": name,
            "price": price,
            "stock": stock,
            "discount": discount
        }

        cart.append(new_product)

        print("¡Producto agregado con exito!: " + str(new_product))

    elif (option == 3):
        print("\nEliminar producto.\n")

        exit = 2

        while exit == 2:

            search = input("Nombre del producto: ")

            for product in (cart):
                if (search == product["name"]):
                    cart.remove(product)

            exit = int(input(
                "Producto eliminado con exito. ¿Desea salir? (1) Si / (2) No. "))
    elif (option == 4): 
        print("\nComprar carrito.\n")

        total = 0 
        discount = 0

        for product in cart:
            discount = price * product["discount"]/100
            total += product["price"] - discount

        confirm = int(input(f"¿Estas seguro de hacer esta compra por el total de ${total}? (1) Si / (2) No.\n"))

        if (confirm == 1):
            print("¡Compra realizada con exito!")
        elif (confirm == 2):
            continue
        else:
            print("Opcion no valida.")
            continue

    else:
        exit_aplication = int(input("Opcion no valida. ¿Desea salir? (1) Si / (2) No. "))
    

        