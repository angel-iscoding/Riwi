users = [{
    "user": "1",
    "password": "1"
}, {
    "user": "AngelitoNormal",
    "password": "1234"
}]

products = [
    {
        "name": "Producto #1",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    },
    {
        "name": "Producto #2",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    },
    {
        "name": "Producto #3",
        "price": 1000,
        "stock": 10,
        "discount": 10,
    }
] 

menu_admin = """

(1) Agregar producto

(2) Modificar producto

(3) Eliminar producto

"""

menu_usuario = """

(1) Comprar producto

"""

while True : 
    print("¡Bienvenido a su Ecommerce favorito!")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    
    option = 0

    if (user == users[0]['user'] and password == users[0]['password']): 
        option = int(input(menu_admin))

        if (option == 1): 
            print("Crear nuevo producto.\n")

            name = input("Nombre del producto: ")
            price = input("Precio del producto: ")
            stock = input("Cantidad de products: ")
            discount = input("Descuento (Porcentaje): ")
            
            new_product = {
                "name": name,
                "price": price,
                "stock": stock,
                "discount": discount
            }

            products.append(new_product)

            print("¡Producto agregado con exito!: " + str(new_product))

        elif (option == 2):
            exit = 2 

            print("Modificar producto.")

            while exit == 2:

                search = input("Nombre del producto: ")

                for product in products:
                    if (search == product["name"]):
                        print("Producto encontrado.")

                        print(f"""
                            (1) Nombre: {product["name"]}
                            (2) Precio: {product["price"]}
                            (3) Cantidad: {product["stock"]}
                            (4) Descuento: {product["discount"]}%
                            """)
                        
                        objective = input("Digite lo que quiera cambiar: ")

                        if (objective == 1):
                            product["name"] = input("Nuevo nombre: ")
                        elif (objective == 2):
                            product["price"] = input("Nuevo precio: ")
                        elif (objective == 3):
                            product["stock"] = input("Nueva cantidad: ")
                        elif (objective == 4):
                            product["discount"] = input("Nuevo descuento: ")
                        else: 
                            print('Opcion no valida')

                        exit = input("¿Desea salir? (1) Si / (2) No")
                else: 
                    exit = input("Producto no encontrado. ¿Desea salir? (1) Si / (2) No")

        elif (option == 3):
            print("Eliminar producto.")
            
            exit = 2

            while exit == 2:

                search = input("Nombre del producto: ")

                for index, product in enumerate(products):
                    if (search == product["name"]):
                        products.remove(product)

                exit = input("Producto eliminado con exito. ¿Desea salir? (1) Si / (2) No")    

        else:
            print("Opcion no valida. ¿Desea salir? (1) Si / (2) No")

    
    break