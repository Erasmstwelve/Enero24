#def define las variables a usar en el codigo
def calculadora():
    #Aqui se estan declarando las variables num1 y num 2 en float, al igual que se usa el input para recoger una entrada de texto
    num1 = float(input("Ingrese el primer número: ")) #Error = no se habia puesto el valor input
    num2 = float(input("Ingrese el segundo número: "))
    #Aqui se define la variable operacion que se usa para elegir que tipo de operación utilizaremos
    operacion = input("Ingrese la operación (+, -, *, /): ")

    #Condicionales para funcionamiento de la entrada de datos y su resultado
    if operacion == '+':
        resultado = num1 + num2 #Error= no se declaró la variable num, correccion Num1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 #Error= no se declaró la variable num, correccion Num1
    else:
        resultado = "Operación no válida"

    #Imprime el resultado de la operacion dada en la entrada de datos del usuario
    print("Resultado:" , resultado) #Error = faltaba una coma despues de la variable "Resultado:"

#cierra la variable calculadora
calculadora() #Error= la variable estaba mal escrita = anterior: "Calculdora" 
