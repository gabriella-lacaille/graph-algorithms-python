cidades = [
    "Caminha", "V. Castelo", "Leixões", "Aveiro",
    "F. da Foz", "Nazaré", "Peniche", "Cascais",
    "Lisboa", "Sesimbra", "Setúbal", "Sines",
    "Baleeira", "Lagos", "Portimão", "Vilamoura",
    "C. Sta. Maria", "Tavira", "VRS António"
]

triangular = [
    [],
    [12],
    [43, 31],
    [75, 63, 32],
    [105, 93, 63, 31],
    [138, 126, 96, 64, 34],
    [156, 144, 116, 85, 56, 23],
    [201, 189, 160, 129, 100, 65, 45],
    [206, 194, 172, 141, 112, 79, 57, 5],
    [221, 209, 181, 150, 121, 88, 66, 26, 23],
    [233, 221, 193, 162, 133, 100, 78, 35, 32, 10],
    [249, 237, 209, 178, 149, 116, 94, 49, 47, 32, 33],
    [302, 290, 262, 231, 202, 169, 147, 112, 111, 92, 95, 63],
    [315, 303, 275, 244, 215, 181, 160, 123, 122, 107, 109, 77, 14],
    [322, 310, 282, 251, 222, 189, 167, 133, 132, 112, 115, 83, 20, 7],
    [342, 330, 302, 271, 242, 209, 187, 154, 153, 130, 133, 101, 39, 26, 20],
    [356, 344, 316, 285, 256, 223, 201, 166, 165, 142, 145, 113, 50, 40, 33, 15],
    [373, 361, 333, 302, 273, 240, 218, 174, 173, 158, 161, 129, 66, 56, 49, 31, 16],
    [384, 372, 344, 313, 284, 251, 229, 191, 190, 170, 172, 141, 76, 66, 59, 41, 26, 11]
]

# Construção da matriz de adjacência
matriz = []

for i in range(len(cidades)):
    linha = []
    for j in range(len(cidades)):
        linha.append(0)
    matriz.append(linha)

for i in range(len(cidades)):
    for j in range(i):
        matriz[i][j] = triangular[i][j]
        matriz[j][i] = triangular[i][j]


n = len(matriz)

distancias = [float('inf')] * n
visitados = [False] * n

anteriores = [-1] * n

# Leixões é a origem (índice 2)
origem = cidades.index("Leixões")
destino = cidades.index("Tavira")

distancias[origem] = 0

for k in range(n):
    menor_distancia = float('inf')
    atual = -1

    for j in range(n):
        if visitados[j] == False:
            if distancias[j] < menor_distancia:
                atual = j
                menor_distancia = distancias[j]

    if atual == -1:
        break

    visitados[atual] = True

    for j in range(n):
        if visitados[j] == False:
            if matriz[atual][j] != 0:
                if distancias[atual] + matriz[atual][j] < distancias[j]:
                    distancias[j] = distancias[atual] + matriz[atual][j]

                    # registra de onde viemos
                    anteriores[j] = atual


# RECONSTRUÇÃO DA ROTA

rota = []
atual = destino

while atual != -1:
    rota.append(atual)

    if atual == origem:
        break

    atual = anteriores[atual]

rota.reverse()


#EXIBIÇÃO DO RESULTADO

if len(rota) > 0 and rota[0] == origem:
    print("Melhor rota entre Leixões e Tavira:")

    for i in range(len(rota)):
        print(cidades[rota[i]], end="")

        if i < len(rota) - 1:
            print(" -> ", end="")

    print()
    print("Distância mínima:", distancias[destino])
else:
    print("Não existe caminho entre Leixões e Tavira.")