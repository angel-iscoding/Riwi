### ACLARACION
#Aquí cumplo los requisitos del entregable pero le quise dar
#un toque más de "complejidad" haciendolo un pequeño programa
#para un carrito con funciones basicas, haciendolo algo más funcional
#y para un uso real

#Diccionario para almacenar los productos. Con algunos productos de prueba
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

#Menu en una varibale para no repetir codigo
menu = """
(1) Ver carrito

(2) Agregar al carrito

(3) Eliminar del carrito

(4) Realizar compra

Seleccione una opcion: """

#El usuario podrá salir de la aplicacion si esta variable es igual a 1
exit_aplication = 2

#Buble While para que la aplicacion no se cierre
while exit_aplication != 1:
    #Bloque Try para cualquier error
    try:
        if (exit_aplication != 1 and exit_aplication != 2):
            print("Opcion no valida. Cerrando el programa...")
            break


        print("\n¡Bienvenido a su Ecommerce favorito!")

        #Variable de opcion para el menu
        option = 0
        
        option = int(input(menu))

        #Pequeño bloque para ver los productos en el carrito
        if (option == 1):
            print("\nMostrando productos en el carrito\n")

            #Se inician variables que almacenan el valor total del carrito
            total = 0 
            discount = 0

            #Bloque for para pasar por cada elemento y un buen formato a la lista mostrada
            for index, product in enumerate(cart): 
                for i in range(1, product["stock"]):        
                    print(f"Producto #{index + 1}.")
                    print(f"Nombre: {product['name']}")
                    print(f"Precio: {product['price']}")
                    print(f"Cantidad: {product['stock']}")
                    print(f"Descuento: {product['discount']}\n")

                    discount = product["price"] * product["discount"]/100
                    total += product["price"] - discount

            print(f"Total carrito: {total}")
    
        #Agregar productos al carrito
        elif (option == 2):
            print("\nAgregar nuevo producto.\n")

            #Se hace los requisitos de la actividad
            #pidiendo los datos que después se guardan en el carrito
            name = input("Nombre del producto: ")
            price = input("Precio del producto: ")
            stock = input("Cantidad de productos: ")
            discount = input("Descuento (Solo numero): ")

            #Sería un problema que el usuario coloque un numero negativo 
            #Y ese numero negativo se reste al total
            if discount > 100 or discount < 0:
                while discount > 100 or discount < 0: 
                    discount = int(print("El descuento no puede ser mayor a 100% ni menor a 0%. Digite otro numero:"))
                

            if stock <= 0:
                while stock < 0:
                    stock = int(input("Debes pedir almenos un producto. Digite otra cantidad: "))
            
            #Se crea un nuevo diccionario con los datos digitados por el usuario
            new_product = {
                "name": name,
                "price": price,
                "stock": stock,
                "discount": discount
            }

            #Se agrega a las lista "cart"
            cart.append(new_product)

            print("¡Producto agregado con exito!: " + str(new_product))

        elif (option == 3):
            print("\nEliminar producto.\n")

            exit = 2

            #While para poder eliminar varios productos del carrito
            while exit == 2:

                search = input("Nombre del producto: ")

                #Busca el nombre del producto, almacena el diccionario en una variable y lo elimina
                for product in (cart):
                    if (search == product["name"]):
                        cart.remove(product)

                exit = int(input(
                    "Producto eliminado con exito. ¿Desea salir? (1) Si / (2) No. "))
                
        elif (option == 4): 
            print("\nComprar carrito.\n")

            #Se inician variables que almacenan el valor total del carrito
            total = 0 
            discount = 0

            #Se recoge el precio de los productos y se les resta el descuento
            #para luego sumarlo al valor total
            for product in cart:
                discount = product["price"] * product["discount"]/100
                total += product["price"] - discount

            confirm = int(input(f"¿Estas seguro de hacer esta compra por el total de ${total}? (1) Si / (2) No.\n"))

            #¡Compra confirmada con exito!
            if (confirm == 1):
                print("¡Compra realizada con exito!")
                #Se reinicia el carrito 
                cart = []
            else:
                print("Opcion no valida.")

        else:
            #En caso de que el se digite una opcion no valida en el menu
            exit_aplication = int(input("Opcion no valida. ¿Desea salir? (1) Si / (2) No. "))
    
    #Except para que en cualquier error el usuario pueda volver a ejecutar
    #Sin necesidad de reiniciar el programa
    except:
        try:
            exit_aplication = int(input("Ha ocurrido un error durante la ejecucion.\n¿Desea salir de aplicacion? (1) Si / (2) No. "))
            
        except:
            print("Respuesta no valida. Cerrando la aplicacion...")
            break
            
    