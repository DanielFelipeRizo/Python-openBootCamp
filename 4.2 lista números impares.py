numeroInicio = int(input('ingrese el numero inicial del rango: '))
numeroFin = int(input('ingrese el numero final del rango: '))
listaPares = []
listaImpares = []
for i in range(numeroInicio, numeroFin):
    if(i %2 != 0):
        listaImpares.append(i)
        continue
    listaPares.append(i)
print('Lista de numeros impares: ',listaImpares)
print('Lista de numeros pares: ',listaPares)


#salida
#ingrese el numero inicial del rango: 1
#ingrese el numero final del rango: 10
#Lista de numeros impares:  [1, 3, 5, 7, 9]
#Lista de numeros pares:  [2, 4, 6, 8]

#Process finished with exit code 0


