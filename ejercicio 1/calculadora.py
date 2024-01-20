def calculadora():
    num1 = float(input("Ingrese el primer número: ")) #Error = no se habia puesto el valor input
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

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

    print("Resultado:" , resultado) #Error = faltaba una coma despues de la variable "Resultado:"

calculadora() #Error= la variable estaba mal escrita = anterior: "Calculdora" 
