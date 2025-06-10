import os

def clear(): 
    os.system("clear")

def menu (msj: str):
    chars = [" ", "⎢", "⎥", "∙", "⎯"]
    
    #Separa el mensaje dentro de una lista
    separed = msj.splitlines()
    
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

        #Condicion que depende de los caracteres, se centra solo

        if porcentaje*100 >= 0 and porcentaje*100 <= 15:
            posicion = int(round(size*0.43))
        
        if porcentaje*100 > 15 and porcentaje*100 <= 30:
            posicion = int(round(size*0.34))
        
        if porcentaje*100 > 30 and porcentaje*100 <= 50:
            posicion = int(round(size*0.27))
        
        if porcentaje*100 > 50 and porcentaje*100 <= 65:
            posicion = int(round(size*0.18))

        if porcentaje*100 > 65 and porcentaje*100 <= 80:
            posicion = int(round(size*0.14))
        
        if porcentaje*100 > 80 and porcentaje*100 <= 100:
            posicion = int(round(size*0.03))

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

startmenu = """Bienvenido al sistema de calificaciones de la institucion. Elija una opcion\n
(1) Verificar evaluacion\n
(2) Calcular promedio de notas\n
(3) Estudiantes aprovados\n
(4) Buscar calificacion\n
"""

user_in = "Usuario -> "

exit = False

students = [6,6,6]

#Empieza el programa

while exit == False:

    try:
        option = int(input(f"{menu(startmenu)}\n{user_in}"))

        if option == 1:
            calificacion = 20
            
            while not calificacion <= 10 and calificacion >= 0: 
                calificacion = float(input(f"{menu("Ingrese una calificacion valida entre 0.0 y 10.0")}\n{user_in}"))

            students.append(calificacion)

            print(f"{menu(f"Calificacion ingresada: {students[-1]}")}")

            input()

        elif option == 2:
            total = 0.0

            for num in students:
                total += num

            print(menu(f"Promedio de notas: {total}"))

            input()

        elif option == 3:
            aprovados = 0

            for num in students:
                if num >= 6.0:
                    aproved+=1

            print(menu(f"Estudiantes aprovados: {aprovados}"))

            input()

        elif option == 4:
            search = float(input(f"{menu("Calificacion a buscar.")}\n{user_in}"))

            if search in students:
                print(menu(f"¡Elemento encontrado!"))
            else:
                print(menu(f"El elemento no fue encontrado."))

            input()    

    except:
        try:
            if not int(input(f"{menu(f"Ha digitado un valor incorrecto, ¿desea salir del programa?\n(1) Para salir. (2) Para quedarse.")}\n{user_in}")) == 1:
                exit == True
        except:
            print(menu("Ha digitado un valor incorrecto... Saliendo del programa."))
            exit = True
    finally:
        print(menu("Saliendo del programa..."))    
    