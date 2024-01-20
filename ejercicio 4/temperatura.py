#define la variable celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius): #faltaba el signo :
 #devuelve el valor y realiza la operaion de conversion
    return (celsius * 9/5) + 32 #faltaba e signo +

#variables de tipo float
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
#imprime el resultado de la conversión
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
