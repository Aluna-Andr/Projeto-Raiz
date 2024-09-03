import math
import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  #ordenando em ordem crescente
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def dividir_vetor(vetor):
    n = len(vetor)
    tamanho_parte = math.floor(math.sqrt(n))  #calcular chão de raiz de ->n
    partes = [vetor[i:i + tamanho_parte] for i in range(0, n, tamanho_parte)]
    return partes




def sqrtsort_com_insertion(vetor):
    partes = dividir_vetor(vetor)
    vetor_solucao = []
    for parte in partes:
        parte = insertion_sort(parte)
    while any(partes):  #aqui enquanto houver elementos nas partes
        maiores = []
        for parte in partes:
            if parte:
                maiores.append(parte[-1])  #aqui pega o maior elemento de cada parte
        
        maior_valor = max(maiores)  #seleciona o maior dentre os maiores elementos
        vetor_solucao.append(maior_valor)
        
        # depois remover o maior elemento da parte correspondente
        for i in range(len(partes)):
            if partes[i] and partes[i][-1] == maior_valor:
                partes[i].pop()
                break

    return vetor_solucao



def salvar_em_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        for item in dados:
            f.write(f"{item}\n")

def processar_tamanho(tamanho):
    intervalo_maximo = tamanho * 10  #intervalo que ira  garantir o TAm a amostra
    vetor_aleatorio = random.sample(range(1, intervalo_maximo), tamanho)

    start_time = time.time()  #inicio da medição do tempo
    vetor_ordenado = sqrtsort_com_insertion(vetor_aleatorio)
    end_time = time.time()  #fim

    #salvar em arquivos
    salvar_em_arquivo(f'vetor_aleatorio_{tamanho}.txt', vetor_aleatorio)
    salvar_em_arquivo(f'vetor_ordenado_{tamanho}.txt', vetor_ordenado)

    print(f"Arquivo 'vetor_aleatorio_{tamanho}.txt' criado com o vetor aleatório.")
    print(f"Arquivo 'vetor_ordenado_{tamanho}.txt' criado com o vetor ordenado.")
    print(f"Tempo de execução para vetor de tamanho {tamanho}: {end_time - start_time:.4f} segundos")

#escolher tamanhos dos vetores 10^3  ate 10^6
tamanhos = [1000,10000,100000,1000000,10000000]


for tamanho in tamanhos:
    processar_tamanho(tamanho)
