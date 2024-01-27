# def es_palindromo(texto):: Define una función llamada es_palindromo que toma un parámetro llamado como texto
def es_palindromo(texto): #Error: Faltaba agregarle los :
# texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum()): Prepara el texto para ser evaluado: Elimina espacios y caracteres especiales. Convierte todas las letras a minúsculas.
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
# Compara el texto original con su versión al revés. Si son iguales, la función devuelve True (es un palíndromo), de lo contrario, devuelve False
    return texto == texto[::-1]

# Aquí se le da inicio a la entrada de texto que se imprimirá en pantalla
palabra_frase = input("Ingrese una palabra o frase: ") 
# Se aplican cpndicionales para definir un resultado
if es_palindromo(palabra_frase): #Error: No estaba definido el argumento (palabra_frase)
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
