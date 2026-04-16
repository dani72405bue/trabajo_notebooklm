# programa para saber el primer y ultimo numero de una lista 

def obtener_primero_ultimo(lista):
    if lista:
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return "la lista no tiene elementos suficientes"
    else:
        return "dato no valido. lista vacia"
    
lista_1 = [1,2,3,4,5]
resultado = obtener_primero_ultimo(lista_1)
print(resultado)