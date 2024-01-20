#se definen variables
def contar_palabra(texto, palabra): #faltaba el signo :
    #return devuelve un valor
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto- Este texto tiene palabras repetidas."
palabra_buscada = "texto"

#imprime la palabra repetida
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") #añadí signos {} que faltaban a la syntaxis del texto
