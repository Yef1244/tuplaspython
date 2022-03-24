#LISTAS
from traceback import print_tb


valores = [1,2,3,4,5]

#TUPLA
valoresTupla = (1,2,3,4,5)
print(valoresTupla)

for valor in valoresTupla:
    print(valor)

#ACCEDIENDO A ELEMENTO TUPLA
print(valoresTupla[0])
#valoresTupla.append(6)
#print(valoresTupla)


#TRANSFORMEMOS UNA TUPLA EN LA LISTA

listaValores=list(valoresTupla)
print(listaValores)
listaValores.append(6)
valoresTupla=tuple(listaValores)
print(valoresTupla)



numeros = (50,42,20,30,40,87)

#convierto la lista
listaNumeros=list(numeros)

#recorro la lista
listaNumerosMayores=[]
for numero in numeros:
    if (numero > 40):
        listaNumerosMayores.append(numero)
print(listaNumerosMayores)



numeros = (50,42,20,30,40,87)

listaNumeros=list(numeros)

listaNumerosPares=[]
for numero in numeros:
    if(numero % 2 == 0):
        listaNumerosPares.append(numero)
print(listaNumerosPares)
