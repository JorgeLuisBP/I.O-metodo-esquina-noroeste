#Autor: BAQUE PILOSO JORGE LUIS
#METODO ESQUINA NOROESTE.
matriz = []
matriz2= []

filas = int(input('Ingrese el numero de filas. ')) +1
columnas = int(input('Ingrese el numero de columnas. ')) +1

for i in range(filas):
    matriz.append([0]*columnas)
    matriz2.append([0]*columnas)

print('Ingrese Ofertas y Demandas. ')
sumaF, sumaC = 0, 0
while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        matriz[f][columnas-1] = int(input('Ingrese Oferta [%d]: ' %(f+1)))
        matriz2[f][columnas-1] = matriz[f][columnas-1]
        sumaF += matriz[f][columnas-1]
    for c in range(columnas-1):
        matriz[filas-1][c] = int(input('Ingrese Demanda [%d]: ' %(c+1)))
        matriz2[filas-1][c] = matriz[filas-1][c]
        sumaC += matriz[filas-1][c]
    if(sumaF == sumaC):
        break
    else:
        print('Ingrese nuevamente los valores...... -*nota: recuerda que la suma de ofertas debe ser igual a la demanda')
print('Ingrese inventario/Stock/Almacen.** ')
for f in range(filas-1):
    for c in range(columnas-1):
        matriz[f][c] = int(input('Ingrese Elemento [%d,%d]: ' %(f,c)))

print('Calcular Movimientos ---> Matriz2')
posF, posC = 0, 0
vo, vi = 0, 0
mayor, menor, igual = 0, 0, 0

while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        sumaF += matriz2[f][posC]
    for c in range(columnas-1):
        sumaC += matriz2[posF][c]

    vo = matriz[filas-1][posC] - sumaF
    vi = matriz[posF][columnas-1] - sumaC

    if(vo < vi):
        menor = vo
        matriz2[posF][posC] = menor
        mayor += matriz2[posF][posC]*matriz[posF][posC]
        posC += 1

    elif(vi < vo):
        menor = vi
        matriz2[posF][posC] = menor
        mayor += matriz2[posF][posC]*matriz[posF][posC]
        posF +=1

    elif(vo == vi):
        igual = (vo+vi)//2
        matriz2[posF][posC] = igual
        mayor += matriz2[posF][posC]*matriz[posF][posC]
        posF += 1
        posC += 1

    if(posF == filas-1 or posC == columnas-1):
        break

print('Matriz: --> Inventario.')
for p in range(filas):
    print(matriz[p])

print('Matriz: --> movimientos.')
for p in range(filas):
    print(matriz2[p])

print('El gasto total es de: ' , mayor)
