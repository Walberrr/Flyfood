#Bachalerado em Sistemas de Informação
# #Universidade Federal Rural de Pernambuco
#Projeto Interdisciplinar Para Sistemas de Informação
#Walbert Pereira de Lima


import time
inicio = time.time()

coordenadas = []
pontos = [] #lista que vai armazenar os pontos de entrega
rotas = []

for i in range(int(n)):
    linha = linhas[i].split()
    for j in linha:
        if j != "0":
            coordenadas = (i, linha.index(j))
            coordenadas.append(coordenadas)
            pontos.append(j)
indice = pontos.index("R") #Acessa um elemento da lista
ponto_R = coordenadas[indice]
coordenadas.pop(coordenadas[indice])
pontos.pop("R") #Remove o R

todas_as_rotas = []
def permutation(pontos, i=0):
    if i == len(pontos):
        todas_as_rotas.append('R'+''.join(pontos)+'R') #Insere um registro após o último elemento

    for j in range(i, len(pontos)):
            rotas = [i for i in pontos]
            rotas[i], rotas[j] = rotas[j], rotas[i]
            permutation(rotas, i+1)
    return todas_as_rotas #Vai retornar a lista de permutação

    PontosEntrega = {}

    with open("matriz.txt") as matriz:
        matriz.read()
        valor = matriz.readlines()
        valor.pop(0)

        for linhas in valor:
            matriz.append(linhas.split())

        for i, line in enumerate(matriz):
            for j, ponto in enumerate(line):
                if ponto.isnumeric() == False:
                    PontosEntrega[ponto] = [i, j]

    def distancia(rotas, pontos):
        menor_rota = 0
        melhor_rota = ()
        for rotas in rotas:
            valor_total = 0
            pontos_ordernados = []

            for point in rotas
                for x in pontos:
                    if point == x[0]:
                        pontos_ordernados.append(x)
            for point in pontos:
                if ponto[0] == 'R':
                    pontos_ordernados.insert(0, point)
                    pontos_ordernados.append(point)

            for i in range(len(pontos_ordernados) - 1):
                soma1 = abs(pontos_ordernados[i][1] - pontos_ordernados[i+1][1])
                soma2 = abs(pontos_ordernados[i][2] - pontos_ordernados[i+1][2])
                distancia = soma1 + soma2
                valor_total += distancia

            if menor_rota == 0:
                menor_rota = valor_total
            if valor_total <= menor_rota:
                menor_rota = valor_total
                melhor_rota = route
                return melhor_rota, menor_rota

    fim = time.time()
    matriz.close()

    print("a menor distancia é: {fim - inicio}")



