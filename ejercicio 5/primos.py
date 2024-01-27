#se define la variable es_primo
def es_primo(numero):#faltaba el signo :
    #condicionales que forman una operacion
    if numero < 2: #faltaba el signo :
        return False
    for i in range(2, int(numero**0.5) + 1): #faltaba el signo :
        if numero % i == 0: #faltaba el signo :
            return False
    return True #en las lineas 6 y 7 se encuentra mal escrita la palabra retunr= return

#dos variables de tipo int
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)] #
#imprime el resultado
print("Números primos:", primos)
