matriz = []

arquivo = open("/home/talita/UERJ/3 PERIODO/ED2/trabalho_av2/grafo.csv", "r")

for linha in arquivo:
   valores = linha.split(",")
   nova_linha = []
 
   for valor in valores:
     numero = int(valor)
     nova_linha.append(numero)

   matriz.append(nova_linha)

arquivo.close()

n = len(matriz)

visitados = []
arestas_agm = []
custo_total = 0

for i in range(n):
 visitados.append(False)

visitados[0] = True

for k in range(n-1):
  menor_peso = float('inf')
  d = -1
  o = -1
 
  for i in range(n):
   for j in range(n):
    if visitados[i] == True and visitados[j] == False:
     if matriz[i][j] != 0:
       if matriz[i][j] < menor_peso:
         menor_peso = matriz[i][j]
         d = j
         o = i
 
  if d!= -1:
   visitados[d] = True
   arestas_agm.append([o, d, menor_peso])
   custo_total += menor_peso       

if len(arestas_agm) != n - 1:
    print("O grafo é desconexo. Não existe árvore geradora mínima.")
else:
    print("Arestas da árvore geradora mínima:")

    for aresta in arestas_agm:
      print(aresta)

    print("Custo total:", custo_total)