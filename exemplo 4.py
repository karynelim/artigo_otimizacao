import random
import copy
import time

# Parâmetros do problema
M = 10
N = 50

# Prioridade de cada tarefa
p = [
    2,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,
    2,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,
    2,3,2,1,3,2,1,3,2,1
]

# Tempo necessário para cada tarefa
t = [
    4,6,5,3,7,5,2,8,4,3,7,5,2,6,5,3,6,4,3,7,
    4,6,5,3,7,5,2,8,4,3,7,5,2,6,5,3,6,4,3,7,
    4,6,5,3,7,5,2,8,4,3
]

# Proficiência de cada membro para cada tarefa (10 x 50)
prof = [
    [3,2,3,2,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,
     3,2,3,2,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,
     3,2,3,2,3,2,1,3,2,1],
    
    [2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,
     2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,
     2,3,2,3,2,3,2,3,2,3],
    
    [1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,
     1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,1,
     1,1,2,1,1,2,1,1,2,1],
    
    [2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,
     2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,
     2,1,3,2,1,3,2,1,3,2],
    
    [3,3,2,3,3,2,3,3,2,3,3,2,3,3,2,3,3,2,3,3,
     3,3,2,3,3,2,3,3,2,3,3,2,3,3,2,3,3,2,3,3,
     3,3,2,3,3,2,3,3,2,3],
    
    [2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,
     2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,3,2,2,
     2,2,3,2,2,3,2,2,3,2],
    
    [1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
     1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
     1,3,1,3,1,3,1,3,1,3],
    
    [3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,
     3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,
     3,2,1,3,2,1,3,2,1,3],
    
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
     2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
     2,1,2,1,2,1,2,1,2,1],
    
    [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,
     1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,
     1,2,3,1,2,3,1,2,3,1]
]

# Capacidade de horas disponíveis para cada membro
h = [40,35,30,30,35,40,35,30,40,35]

# Função objetivo
def calcula_beneficio(solucao):
    beneficio = 0
    for i in range(M):
        for j in range(N):
            if solucao[i][j] == 1:
                beneficio += p[j] * prof[i][j]
    return beneficio

# Verifica restrições
def respeita_restricoes(solucao):
    for j in range(N):
        if sum(solucao[i][j] for i in range(M)) != 1:
            return False
    for i in range(M):
        tempo_total = sum(t[j]*solucao[i][j] for j in range(N))
        if tempo_total > h[i]:
            return False
    return True

# Geração de solução inicial
def gera_solucao_inicial():
    solucao = [[0]*N for _ in range(M)]
    tarefas = list(range(N))
    random.shuffle(tarefas)
    for j in tarefas:
        membros = list(range(M))
        random.shuffle(membros)
        for i in membros:
            tempo_total = sum(t[k]*solucao[i][k] for k in range(N))
            if tempo_total + t[j] <= h[i]:
                solucao[i][j] = 1
                break
    return solucao

# Busca local
def busca_local(solucao):
    melhor = copy.deepcopy(solucao)
    melhor_beneficio = calcula_beneficio(melhor)
    melhorou = True
    while melhorou:
        melhorou = False
        for i1 in range(M):
            for j in range(N):
                if melhor[i1][j] == 1:
                    for i2 in range(M):
                        if i2 != i1:
                            tempo_i2 = sum(t[k]*melhor[i2][k] for k in range(N))
                            if tempo_i2 + t[j] <= h[i2]:
                                nova = copy.deepcopy(melhor)
                                nova[i1][j] = 0
                                nova[i2][j] = 1
                                if respeita_restricoes(nova):
                                    novo_beneficio = calcula_beneficio(nova)
                                    if novo_beneficio > melhor_beneficio:
                                        melhor = nova
                                        melhor_beneficio = novo_beneficio
                                        melhorou = True
                                        break
                    if melhorou:
                        break
            if melhorou:
                break
    return melhor

# Perturbação
def perturba(solucao):
    nova = copy.deepcopy(solucao)
    j = random.randint(0,N-1)
    i_atual = [i for i in range(M) if nova[i][j]==1][0]
    i_novo = random.choice([i for i in range(M) if i != i_atual])
    nova[i_atual][j] = 0
    tempo_i_novo = sum(t[k]*nova[i_novo][k] for k in range(N))
    if tempo_i_novo + t[j] <= h[i_novo]:
        nova[i_novo][j] = 1
    else:
        nova[i_atual][j] = 1  # volta ao original
    return nova

# ILS principal
def ILS(max_iter=1000):
    melhor_solucao = gera_solucao_inicial()
    melhor_solucao = busca_local(melhor_solucao)
    melhor_beneficio = calcula_beneficio(melhor_solucao)

    for _ in range(max_iter):
        nova_solucao = perturba(melhor_solucao)
        nova_solucao = busca_local(nova_solucao)
        novo_beneficio = calcula_beneficio(nova_solucao)
        if novo_beneficio > melhor_beneficio:
            melhor_solucao = nova_solucao
            melhor_beneficio = novo_beneficio

    return melhor_solucao, melhor_beneficio

# Execução
start_time = time.time()
solucao_final, beneficio_final = ILS(max_iter=1000)
end_time = time.time()

# Saída
print("Melhor benefício encontrado:", beneficio_final)
for i in range(M):
    tarefas_alocadas = [j+1 for j in range(N) if solucao_final[i][j]==1]
    print(f"Membro {i+1}: Tarefas {tarefas_alocadas}")
print("Tempo de execução (segundos):", round(end_time - start_time, 4))
