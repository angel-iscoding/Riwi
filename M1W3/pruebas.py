def UI_parseInt(promp: str) -> int:
    try: 
        value = int(input(f"{UI(promp)}\nUsuario -> ")) 

        if value < 0 and not value is None:
            print(UI("Debe ingresar un numero entero positivo. Intente nuevamente."))
            return UI_parseInt(promp)

        return value 
    except:
        print(UI("Debe ingresar un numero valido. Intente nuevamente."))
        return UI_parseInt(promp)

def UI (msj: str) -> str:
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
            #Agrega un espacio para que todos coincidan
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

print(UI_parseInt("Digite un numero entero: "))