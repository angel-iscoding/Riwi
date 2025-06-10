#Entrada de datos para digitar una palabra
palabra = input ("Ingrese una palabra. \nUsuario -> ")

#print("\n\nPalabra: ", palabra, f"\nLetras: {len(palabra)}\n\n")

#Variable para comprobar si es palindromo
palindromo = True

for i in range(len(palabra)-1, -1, -1):
    #Verifica si la primera letra de la palabra y la ultima son diferentes
    if not (palabra[i] == palabra[((len(palabra)-1)-i)]):
        #Si no lo son, entonces no es palindromo
        palindromo = False
    
#Confirma al usuario si es palidromo   
print("Es palindromo" if palindromo else "No es palindromo")
