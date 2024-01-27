def factorial(n): #Faltaba el signo :
    if n == 0 or n == 1:
        return 1 #Estaba mal escrito (retunr)
    else:
        return n * factorial(n - 1) #Estaba mal escrito (retunr)


numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}") #Faltaba el argumento (numero)
