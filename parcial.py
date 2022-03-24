from asyncio import protocols
from math import prod
from os import remove
from traceback import print_tb


opcion = 1
productos=[]

print('Digite 1 para ingresar (Codigo, Nombre, Precio) de un producto')
print('Digite 2 para mostrar todos los productos registrados')
print('Digite 3 para buscar por codigo un producto y editar su precio')
print('Digite 4 para buscar por codigo un producto y eliminarlo')
print('Digite 0 para salir')

while (opcion != 0):
    opcion = int(input('Digite una opcion: '))
    if (opcion == 1):
        producto={}
        #llenando el diccionario
        producto['codigo']=input('  Ingrese el codigo del producto: ')
        producto['nombre']=input('  Ingrese el nombre del producto: ')
        producto['precio']=int(input('  Ingrese el precio del producto: '))
        #llenando la lista
        productos.append(producto)
    elif (opcion == 2):
        print(productos)
    elif (opcion == 3):
        bandera = True
        opcionCodigo=input('  Ingrese el codigo: ')
        for producto in productos:
            if(producto['codigo'] == opcionCodigo):
                producto['precio']=int(input('   Ingrese el nuevo precio del producto: '))
                bandera=True
                break 
            else:
                bandera=False
        if(bandera == False):
            print('   Producto no encontrado')
    elif (opcion == 4):
        bandera = True
        opcionCodigo=input('  Ingrese el codigo: ')
        for producto in productos:
            if(producto['codigo'] == opcionCodigo):
                productos.remove(producto)
                print('--Se ha eliminado el producto')
                bandera = True
                break
            else:
                bandera=False
        if(bandera == False):
            print('--El producto no existe')
    else:
        print('')
