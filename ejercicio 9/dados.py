import random #Estaba mal escrito

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado): #No tenía el def y le faltaban los :
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados #La palabra retunr estaba mal escrita

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado) #Le faltaba definir otro argumento
print(f"Resultados del lanzamiento: {lanzamientos}")

