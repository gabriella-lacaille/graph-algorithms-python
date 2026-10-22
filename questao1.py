matriz = []

for i in range(16):
    linha = []
    for j in range(16):
        linha.append(0)

    matriz.append(linha)    

arestas = [
      [0,4],
      [0,8],
      [0,3],
      [0,1],
      [4,9],
      [4,7],
      [4,5],
      [8,9],
      [8,10],
      [9,11],
      [10,11],
      [10,3],
      [11,7],
      [7,3],
      [7,6],
      [3,2],
      [1,2],
      [1,5],
      [1,12],
      [2,6],
      [2,14],
      [5,13],
      [5,6],
      [6,15],
      [12,13],
      [12,14],
      [13,15],
      [14,15]
    ]

for aresta in arestas:
    matriz[aresta[0]][aresta[1]] = 1
    matriz[aresta[1]][aresta[0]] = 1

cores = [-1] * 16

for cor_atual in range(16):
   for j in range(16):
      if cores[j] == -1:
         y = 0
         for x in range (16):
           if matriz[j][x] == 1 and cores[x] == cor_atual:
            y += 1
         if y==0:
          cores[j] = cor_atual     

print(cores)