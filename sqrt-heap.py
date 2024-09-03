import math
import random
import time


#implementação do Heapsort e operações de heap
def heapify(vetor, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and vetor[left] > vetor[largest]:
        largest = left

    if right < n and vetor[right] > vetor[largest]:
        largest = right

    if largest != i:
        vetor[i], vetor[largest] = vetor[largest], vetor[i]
        heapify(vetor, n, largest)

def heapify_bottom_up(vetor,i):
    while i >0:
        p = (i-1)//2
        if vetor[p] < vetor[i]:
            vetor[p],vetor[i] = vetor[i],vetor[p]
        else:
            break
        i = p

#operação custa teta de (m)
def makeheap(vetor):
    n = len(vetor)
    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i)
    return vetor

def removeheap(vetor):
    n = len(vetor)
    if n == 0:
        return None
    #troca o maior elemento (raiz) com o último elemento
    vetor[0], vetor[n-1] = vetor[n-1], vetor[0]
    #remove o último elemento (que era a raiz)
    maior = vetor.pop()
    #reestrutura a heap
    if vetor:
        heapify(vetor, len(vetor), 0)
    return maior




def dividir_vetor(vetor):
    n = len(vetor)
    tamanho_parte = math.floor(math.sqrt(n)) #calcular chão de raiz de n
    partes = [vetor[i:i + tamanho_parte] for i in range(0, n, tamanho_parte)]
    return tamanho_parte, partes


def sqrtsort_com_heap(vetor):
    _, partes = dividir_vetor(vetor)  #dividir o vetor em partes
    
    maiores = []  #lista para armazenar os maiores elementos
    heaps = []
    for parte in partes:
        #criar uma heap para cada parte usando uma lista como base
        heap = list(parte)
        makeheap(heap)
        heaps.append(heap)

    # print(heaps)

    heap_m = makeheap([(removeheap(h),i) for i,h in enumerate(heaps)])
    resultado = []
    for i in range(len(vetor)):
        maior,idx = removeheap(heap_m)
        resultado.append(maior)
        if len(heaps[idx])>0:
            prox_maior = removeheap(heaps[idx])
            heap_m.append((prox_maior,idx))
            heapify_bottom_up(heap_m,len(heap_m)-1)
        

    return resultado


def salvar_em_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        for item in dados:
            f.write(f"{item}\n")

def processar_tamanho_com_heap(tamanho):
    intervalo_maximo = tamanho * 10
    vetor_aleatorio = random.sample(range(1, intervalo_maximo), tamanho)

    print(f"Processando vetor de tamanho {tamanho}...")

    start_time = time.time()  # Início da medição do tempo
    vetor_ordenado = sqrtsort_com_heap(vetor_aleatorio)
    end_time = time.time()  # Fim da medição do tempo

    # Salvar em arquivos
    salvar_em_arquivo(f'vetor_aleatorio_{tamanho}.txt', vetor_aleatorio)
    salvar_em_arquivo(f'vetor_ordenado_{tamanho}.txt', vetor_ordenado)

    print(f"Arquivo 'vetor_aleatorio_{tamanho}.txt' criado com o vetor aleatório.")
    print(f"Arquivo 'vetor_ordenado_{tamanho}.txt' criado com o vetor ordenado.")
    print(f"Tempo de execução para vetor de tamanho {tamanho}: {end_time - start_time:.4f} segundos")

# Escolher tamanhos dos vetores
tamanhos = [1000,10000,100000,1000000,10000000]

for tamanho in tamanhos:
    processar_tamanho_com_heap(tamanho)
