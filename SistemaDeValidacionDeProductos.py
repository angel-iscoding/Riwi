import os
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
#Chars que conforman el menu
chars = [" ", "⎢", "⎥", "∙", "⎯"]
#Varibale de entrada de usuario
user = "Usuario -> "

#Funcion para limpiar consola
def clear(): 
    os.system("clear")

def menu (msj: str):
    #Separa el mensaje dentro de una lista
    separed = msj.splitlines()
    
    #Tamaño del menu
    size = 110
    
    #Head del menu
    menu = f"{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    #Bucle para recorrer la lista
    for line in separed:
        menu+="\n"

        #Posicion de los caracteres
        posicion = 18 if len(line) > 60 else 25

        #Total de caracteres
        total = (len(line)+1)/2

        #print (f"Caracteres: {len(line)}")
        #print (f"Caracteres + 1: {len(msj)+1}")
        #print (f"Total dividido: {total}")

        #Redondeo de total
        total = round(total)
        lado1 = int(round(size/2))
        lado2 = int(round(size/2))

        #print (f"Total redondeado: {total}")
        #print(f"Residuo: {len(msj) % 2}")

        #Condicion para que el menu se vea bien
        if not (len(line) - 2) % 4 == 0:
            lado2 -= 2

        #Condicion para que el menu se vea bien
        if len(line) % 2 == 1: 
            line += " "

        #print(f"Lado #1: {lado1-(total)}")
        #print (f"Caracteres en el msj: {total*2}")
        #print(f"Lado #2: {lado2-total}")

        #Calculo de la posicion del centro
        centro = lado1-posicion
        
        menu += f"{chars[1]}{chars[0]*((lado1)-centro)}{line}{chars[0]*((lado2-total*2)+centro)}{chars[2]}"

    #Footer del menu
    menu += f"\n{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    return menu

#El usuario podrá salir de la aplicacion si esta variable es igual a 1
exit_aplication = 2

#Buble While para que la aplicacion no se cierre
while exit_aplication != 1:
    #Clear para hacer mas legible la consola
    clear()
    #Bloque Try para cualquier error
    try:
        if (exit_aplication != 1 and exit_aplication != 2):
            print("Opcion no valida. Cerrando el programa...")
            break

        #Variable de opcion para el menu
        option = 0
        
        mensaje = """Bienvenido a su Ecommerce favorito. Por favor, elija una opcion.
        (1) Mostrar carrito.
        (2) Agregar productos.
        (3) Eliminar productos.
        (4) Comprar carrito.
        (5) Salir."""

        option = int(input(f"{menu(mensaje)}\n{user}"))

        #Pequeño bloque para ver los productos en el carrito
        if (option == 1):
            clear()
            print("\nMostrando productos en el carrito\n")

            msj_product = ""

            #Se inician variables que almacenan el valor total del carrito
            total = 0 
            discount = 0

            #Bloque for para pasar por cada elemento y un buen formato a la lista mostrada
            for index, product in enumerate(cart): 
                
                msj_product = f"""Producto #{index + 1}
                Nombre: {product['name']}
                Precio: {product['price']}
                Cantidad: {product['stock']}
                Descuento: {product['discount']}"""

                index+=1

                for i in range(1, product["stock"]):    
                    discount = product["price"] * product["discount"]/100
                    total += product["price"] - discount    

                print(menu(msj_product))

            print(f"\nTotal carrito: {total}\n")

            input()
    
        #Agregar productos al carrito
        elif (option == 2):
            clear()
            print("\nAgregar nuevo producto.\n")

            #Se hace los requisitos de la actividad
            #pidiendo los datos que después se guardan en el carrito
            name = input("Nombre del producto: ")
            price = int(input("Precio del producto: "))
            stock = int(input("Cantidad de productos: "))
            discount = int(input("Descuento (Solo numero): "))

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

            msj_product = f"""¡Producto agregado con exito!
            Nombre: {new_product['name']}
            Precio: {new_product['price']}
            Cantidad: {new_product['stock']}
            Descuento: {new_product['discount']}%"""

            #Se agrega a las lista "cart"
            cart.append(new_product)

            clear()

            print(menu(msj_product))

            input()

        elif (option == 3):
            clear()
            print("\nEliminar producto.\n")

            exit = 1

            #While para poder eliminar varios productos del carrito
            while exit == 1:

                search = input("Nombre del producto: ")

                eliminado = False
                #Busca el nombre del producto, almacena el diccionario en una variable y lo elimina
                for product in cart:
                    if (search.lower() == product["name"].lower()):
                        cart.remove(product)
                        eliminado = True

                clear()
                
                if eliminado:
                    exit = int(input(f"{menu(f"Producto eliminado con exito. ¿Desea eliminar mas? (1) Si / (2) No.\n")}\n{user}"))
                else:
                    exit = int(input(f"{menu(f"Producto no encontrado. ¿Desea eliminar mas? (1) Si / (2) No.\n")}\n{user}"))
        elif (option == 4): 
            clear()

            #Se inician variables que almacenan el valor total del carrito
            total = 0 
            discount = 0

            #Se recoge el precio de los productos y se les resta el descuento
            #para luego sumarlo al valor total
            for product in cart:
                for i in range(1, product["stock"]): 
                    discount = product["price"] * product["discount"]/100
                    total += product["price"] - discount

            confirm = int(input(f"{menu(f"¿Estas seguro de hacer esta compra por el total de ${total}? (1) Si / (2) No.")}\n{user}"))

            #¡Compra confirmada con exito!
            if (confirm == 1):
                print(menu("¡Compra realizada con exito!"))
                input()
                #Se reinicia el carrito 
                cart = []
            elif (confirm == 2):
                print(menu("Compra cancelada."))
                input()
            else:
                print(menu("Opcion no valida."))
                input()

        elif (option == 5):
            clear()
            print(menu("Gracias por usar nuestro programa."))
            input()
            exit_aplication = 1

        else:
            clear()
            #En caso de que el se digite una opcion no valida en el menu
            exit_aplication = int(input(f"{menu(f"Opcion no valida. ¿Desea salir? (1) Si / (2) No.")}\n{user}"))
    
    #Except para que en cualquier error el usuario pueda volver a ejecutar
    #Sin necesidad de reiniciar el programa
    except:
        try:
            clear()
            exit_aplication = int(input(f"{menu("Ha ocurrido un error durante la ejecucion.\n¿Desea salir de aplicacion? (1) Si / (2) No.")}\n{user}"))
            
        except:
            print(menu("Respuesta no valida. Cerrando la aplicacion..."))
            break