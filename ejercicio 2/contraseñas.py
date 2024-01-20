#import me funciona para elegir librerias
import random #Corregí la libreria rando por random, ya que estaba mal escrita
import string

#def me ayuda a definir la variable
#longitud=8 me ayuda a definir que la variable debe tener 8 caracteres
def generar_contraseña(longitud=8): #no estaba definida la variablle generar_contraseña

    #dos variables en string 
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña #corregi "retunr" por return, mal escrita.

print(generar_contraseña())
