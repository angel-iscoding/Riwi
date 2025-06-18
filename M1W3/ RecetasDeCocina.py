variable = {
    "receta": "sandwich",
    "salsa": {
        "pimienta_negra" : False,
        "sal" : "al gusto",
        "zumo_limon" : "10 ml"
    },
    "presentacion_pollo" : "normal",
    "ingredientes": ["pan de sándwich", "queso", "lechuga", "tomate"],
    "pasos": ["Tostar ligeramente el pan", "Colocar el pollo”, “Colocar queso”, “agregar salsa" ]
}

def preparar_ensalada_cesar():
    print("Preparando ensala Cesar")

    variable["receta"] = "Ensalada Cesar"
    variable["salsa"]["pimienta_negra"] = preparar_ensalada_cesar()
    variable


def preparar_wrap_cesar():
    print("Preparando ensalada Wrap")

def preparar_sandwich_pollo():
    print("Preparando sandwinch")



def preparar_pollo_a_la_plancha(presentacion):
    print("Preparando pollo a la plancha")

def definir_ingredientes():
    pass

def aplicar_sal():
    pass

def preparar_salsa_cesar() -> bool:
    return True



def emplatado():
    pass

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

def menu() -> bool:
    option = int(input(UI("Digite una opcion. 1. 2. 3. 4.")))

    match option:
        case 1:
            preparar_ensalada_cesar()
        case 2:
            preparar_wrap_cesar()
        case 3:
            preparar_sandwich_pollo()
    return True

def main():
    menu()
    
if __name__ == "__main__":
    main()