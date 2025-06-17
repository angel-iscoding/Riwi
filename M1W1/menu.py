

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

        if porcentaje*100 >= 0 and porcentaje*100 <= 15:
            posicion = int(round(size*0.43))
        
        if porcentaje*100 > 15 and porcentaje*100 <= 30:
            posicion = int(round(size*0.37))
        
        if porcentaje*100 > 30 and porcentaje*100 <= 50:
            posicion = int(round(size*0.20))
        
        if porcentaje*100 > 50 and porcentaje*100 <= 65:
            posicion = int(round(size*0.15))

        if porcentaje*100 > 65 and porcentaje*100 <= 80:
            posicion = int(round(size*0.1))
        
        if porcentaje*100 > 80 and porcentaje*100 <= 100:
            posicion = int(round(size*0.03))

        print(f"La posicion es: {posicion}")

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

def menu2 (msj: str):
    # Constantes
    size = 100
    border_char = "∙"
    fill_char = "⎯"
    line_char = " "
    side_char_l = "⎢"
    side_char_r = "⎥"
    
    # Construir encabezado del menú
    menu = f"{border_char}{fill_char * (size - 2)}{border_char}"
    
    # Procesar cada línea del mensaje
    for line in msj.splitlines():
        line_length = len(line)
        # Ajustar línea si es impar
        if line_length % 2 == 1:
            line += " "
            
        line_length = len(line)
        
        # Calcular el padding izquierdo y derecho
        total_padding = size - 2 - line_length
        padding = total_padding // 2
        
        # Agregar línea al menú
        menu += f"\n{side_char_l}{line_char * padding}{line}{line_char * padding}{side_char_r}"
    
    # Construir pie del menú
    menu += f"\n{border_char}{fill_char * (size - 2)}{border_char}"
    
    return menu


mensaje = """Bienvenido a su Ecommerce favorito. Elija una opcion\n
(1) Mostrar carrito\n
(2) Agregar productos\n
(3) Eliminar productos\n
(4) Comprar carrito\n
"""

prueba = "12345"
new = menu2(prueba)

print(new)

