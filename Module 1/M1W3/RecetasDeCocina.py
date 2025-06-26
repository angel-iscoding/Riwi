import os

receta = {
    "receta": str,
    "salsa": {
        "pimienta_negra" : bool,
        "sal" : str,
        "zumo_limon" : str,
    },
    "presentacion_pollo" : str,
    "ingredientes": [str],
    "pasos": [str]
}

ingredientes = [
    {
        "nombre": "Lechuga",
        "obligatorio": True
    },
    {
        "nombre": "Lechuga",
        "obligatorio": True
    }
    ,
    {
        "nombre": "Lechuga",
        "obligatorio": True
    }
    ,
    {
        "nombre": "Lechuga",
        "obligatorio": True
    }
    ,
    {
        "nombre": "Lechuga",
        "obligatorio": True
    }
]

"""
Funciones de preparacion de recetas.
"""

def preparar_ensalada_cesar():
    receta["receta"] = "Ensalada Cesar"
    receta["salsa"]["pimienta_negra"] = preparar_salsa_cesar()
    receta["salsa"]["sal"] = aplicar_condimento("sal")
    receta["salsa"]["zumo_limon"] = aplicar_condimento("zumo de limon")
    receta["presentacion_pollo"] = preparar_pollo_a_la_plancha()
    receta["ingredientes"] = confirmar_ingredientes(ingredientes)
    receta["pasos"] = [
        "Lavar y cortar la lechuga.",
        "Cocinar el pollo a la plancha.",
        "Preparar la salsa Cesar.",
        "Mezclar la lechuga con el pollo y la salsa.",
        "Servir en un plato."
    ]

    emplatado(receta)

def preparar_wrap_cesar():
    print("Preparando ensalada Wrap")

def preparar_sandwich_pollo():
    print("Preparando sandwinch")

"""
Funciones de proceso de preparacion
"""

def preparar_pollo_a_la_plancha():
    presensacion = ['Asado', 'Frito', 'Plancha']
    
    respuesta = input(UI("¿Cómo desea presentar el pollo? (Asado/Frito/Plancha): ")).strip().capitalize()
    
    if respuesta not in presensacion:
        print(UI("Presentación no válida. Por favor, elija entre Asado, Frito o Plancha."))
        preparar_pollo_a_la_plancha()
    else:
        return respuesta


def confirmar_ingredientes(ingredientes: list):
    ingredientes_confirmados = []
    for ingrediente in ingredientes:
        respuesta = input(UI(f"¿Tiene el ingrediente: {ingrediente["nombre"]}? (S/N)\n{""}")).strip().upper()

        if respuesta == 'S':
            ingredientes_confirmados.append(ingrediente)
            print(UI(f"Ingrediente {ingrediente} confirmado."))
        elif respuesta == 'N':
            print(UI(f"Ingrediente {ingrediente} no disponible."))

    return ingredientes_confirmados


def aplicar_condimento(ingrediente: str):
    sal = 0
    aplicar = input(UI(f"¿Desea aplicar {ingrediente} (S/N)")).strip().upper()
    if aplicar in ['S', 'N']:
        if aplicar == 'S':
            while True:
                sal = int(input(UI(f"¿Cuántas cucharadas de {ingrediente} desea aplicar? (0-5): ")))
                if 0 <= sal <= 5:
                    print(UI(f"Aplicando {sal} cucharadas de {ingrediente}."))
                    return sal
                else:
                    print(UI("Por favor, ingrese un número entre 0 y 5."))
        else:
            print(UI(f"No se aplicará {ingrediente}."))
            return 0
        
def preparar_salsa_cesar() -> bool:
    salsa = input(UI("¿Desea preparar la salsa Cesar? (S/N): ")).strip().upper()

    if salsa in ['S', 'N']:
        if salsa == 'S':
            input(UI("Preparando salsa Cesar..."))
            # Aquí se pueden agregar los pasos para preparar la salsa
            return True
        elif salsa == 'N':
            input(UI("No se preparará la salsa Cesar."))
            return False
        else:
            preparar_salsa_cesar()
    else:
        preparar_salsa_cesar()

#Emplatado de la receta

def emplatado(receta: dict):
    for clave, valor in receta.items():
        print(UI(f"{clave.capitalize()}: {valor}"))

#Funciones de utilidad

def clear(): 
    os.system("clear")

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

def UI_input(expected: str, input: any):
    if isinstance(input, expected):
        return input
    else:
        raise ValueError("Se ha proporcionado datos incorrectos.")

#Funciones principales

def menu():
    try: 
        option = 1
        while option in [1, 2, 3]:
            option = int(input(UI("Digite una opcion. 1. 2. 3. 4.")))
            match option:
                case 1:
                    preparar_ensalada_cesar()
                case 2:
                    preparar_wrap_cesar()
                case 3:
                    preparar_sandwich_pollo()
                case 4:
                    continue
                case _:
                    print(UI("Opcion no valida, por favor intente de nuevo."))
                    menu()
    except:
        print(UI("Ocurrió un error. Por favor, intente de nuevo."))
        menu()    
    finally:
        print(UI("Gracias por usar el sistema de recetas. ¡Hasta luego!"))

def main():
    menu()

if __name__ == "__main__":
    main()