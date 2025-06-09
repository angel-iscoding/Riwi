def menu (msj: str):
    chars = [" ", "⎢", "⎥", "∙", "⎯"]
    
    #Separa el mensaje dentro de una lista
    separed = msj.splitlines()
    
    #Tamaño del menu
    size = 110
    
    #Head del menu
    menu = f"{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    #Bucle para recorrer la lista
    for line in separed:
        menu+="\n"

        #Posicion inicial de los caracteres
        posicion = int(round(size*0.15)) if len(line) > 60 else int(round(size*0.30))

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

menu_inicial = """Bienvenido al sistema de calificaciones de la institucion. Elija una opcion\n
(1) Verificar estado de evaluacion\n
(2) Calcular promedio de notas\n
(3) Estudiantes aprovados\n
(4) Buscar calificacion\n
"""

user_in = "Usuario -> "

salir = False

estudiantes = []

#Empieza el programa

while salir != False:

    option = input(f"{menu(menu_inicial)}\n{user_in}")

    if option == 1:
        print(option)
    elif option == 2:
        print(option)
    elif option == 3:
        print(option)
    elif option == 4:
        print(option)
