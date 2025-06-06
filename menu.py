chars = [".", "⎢", "⎥", "∙", "⎯"]

def menu (msj: str):
    separed = msj.splitlines()
    
    menu = f"{chars[3]}{chars[4]*98}{chars[3]}"

    for line in separed:
        menu+="\n"

        posicion = 20 if len(line) > 50 else 30

        total = (len(line)+1)/2

        #print (f"Caracteres: {len(line)}")
        #print (f"Caracteres + 1: {len(msj)+1}")
        #print (f"Total dividido: {total}")

        total = round(total)
        lado1 = 50
        lado2 = 50

        #print (f"Total redondeado: {total}")
        #print(f"Residuo: {len(msj) % 2}")

        if not (len(line) - 2) % 4 == 0:
            lado2 -= 2

        if len(line) % 2 == 1: 
            line += " "

        #print(f"Lado #1: {lado1-(total)}")
        #print (f"Caracteres en el msj: {total*2}")
        #print(f"Lado #2: {lado2-total}")

        centro = lado1-posicion
        
        menu += f"{chars[1]}{chars[0]*((lado1)-centro)}{line}{chars[0]*((lado2-total*2)+centro)}{chars[2]}"

    menu += f"\n{chars[3]}{chars[4]*98}{chars[3]}"

    return menu

mensaje = """Bienvenido a su Ecommerce favorito. Elija una opcion\n
(1) Mostrar carrito\n
(2) Agregar productos\n
(3) Eliminar productos\n
(4) Comprar carrito\n
"""
new = menu(mensaje)

print(new)

