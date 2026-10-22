def dfs(arestas, caminho, vertice, visitados):
    visitados.append(vertice)
 
    ligacoes = []
    for aresta in arestas:
        if aresta[0] == vertice:
            # registra todas as conexões com o vértice
            ligacoes.append(aresta[1]) 
        
    if 'B' in ligacoes:
        print('labirinto resolvido! caminho: ')
        return True
    
    for item in ligacoes:
        if item not in visitados:
            encontrou = dfs(arestas, caminho, item, visitados)
            if(encontrou):
                caminho.insert(0, item)
                return True   

arestas = [
    ['A', 1],['A', 4],
    [1, 6],
    [6, 7],
    [7, 2],[7, 8],
    [2, 3],
    [8, 15],
    [15, 14],[15, 21],
    [4, 5],[4, 9],
    [9, 10],[9, 29],
    [10, 16],
    [16, 17],
    [17, 12],
    [12, 11],[12, 13],
    [29, 30],
    [30, 51],
    [51, 52],[51, 58],
    [58, 57],
    [57, 36],
    [52, 59],[52, 47],
    [47, 31],[47, 48],
    [31, 32],
    [32, 23],
    [23, 22],
    [48, 54],
    [54, 53],
    [53, 60],
    [60, 61],
    [61, 55],
    [55, 56],
    [5, 19],
    [19, 18],[19, 20],
    [18, 24],
    [24, 25],
    [25, 34],
    [34, 33],
    [33, 38],
    [38, 37],
    [37, 41],
    [41, 42],
    [20, 27],
    [27, 26],[27, 28],
    [28, 46],
    [46, 45],
    [45, 35],
    [26, 40],
    [40, 39],
    [39, 43],
    [43, 44],
    [44, 49],
    [49, 50],
    [50, 'B'],
    ['B', 63],
    [63, 62]
]
caminho = []

dfs(arestas, caminho, 'A', visitados = [])
print('A')
for item in caminho:
    print(item)
print('B')
