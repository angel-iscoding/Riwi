chars = [".", "⎢", "⎥", "∙", "⎯"]

def menu (msj: str):
    chars = [" ", "⎢", "⎥", "∙", "⎯"]
    
    #Separa el mensaje dentro de una lista
    separed = msj.splitlines()

    print(separed)
    
    #Tamaño del menu
    size = 100

    #Head del menu
    menu = f"{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    #Bucle para recorrer la lista
    for line in separed:
        menu+="\n"

        caracteres = len(line)

        porcentaje = caracteres / size

        posicion = 0

        print(porcentaje)

        if porcentaje*100 >= 0 and porcentaje*100 <= 10:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.41))
        
        if porcentaje*100 > 10 and porcentaje*100 <= 20:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.38))
        
        if porcentaje*100 > 30 and porcentaje*100 <= 40:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.50))
        
        if porcentaje*100 > 40 and porcentaje*100 <= 50:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.40))
        
        if porcentaje*100 > 50 and porcentaje*100 <= 60:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.30))
        
        if porcentaje*100 > 60 and porcentaje*100 <= 70:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.20))
        
        if porcentaje*100 > 80 and porcentaje*100 <= 90:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.10))
        
        if porcentaje*100 > 90 and porcentaje*100 <= 100:
            print(f"Es un porcentaje de: {porcentaje}. Es decir: {porcentaje*100}%")
            posicion = int(round(size*0.00))

      

        #Total de caracteres
        total = (caracteres+1)/2

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
        if not (caracteres - 2) % 4 == 0:
            lado2 -= 2

        #Condicion para que el menu se vea bien
        if caracteres % 2 == 1: 
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

mensaje = """Bienvenido a su Ecommerce favorito. Elija una opcion\n
(1) Mostrar carrito\n
(2) Agregar productos\n
(3) Eliminar productos\n
(4) Comprar carrito\n
"""

prueba = "123456789123456789"
new = menu(prueba)

print(new)

