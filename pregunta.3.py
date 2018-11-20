matriz = []
filas = int(input("Cantidad de filas: "))
columnas = int(input("Cantidad de columnas: "))

for i in range(filas):
    matriz.append([0]*columnas)
for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input("Elemento %d, %d : " % (f,c)))

print (matriz)
