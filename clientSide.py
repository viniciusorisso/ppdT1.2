import xmlrpc.client
import time
import random
import threading

# Número que seja divisível por 8,4,2
m = 800000

# Declaração do número de threads
number_of_threads = 2

# Declaração da lista de valores recebidos pelo get()
list_values = []

# Função que usa as interfaces fornecidas pelo ServerSide.py
def funcao (init, end):
    # Declaração do Cliente Side RPC    
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        for i in range(init, end):
            proxy.put(str(i), random.randint(0, m))
        for i in range (init, end):
            list_values.append(proxy.get(str(i)))

# Variável de tempo inicializada
timeSpent = time.time()

# Início e fim de cada thread dado o número m
init = 0
end = int(m/number_of_threads)

list_threads = []

# Instanciação e inicialização das threads passando seu início e atualizando seu fim
for t in range(0, number_of_threads):
    t = threading.Thread(target=funcao, args=(init, end))
    t.start()
    list_threads.append(t)
    init = end
    end += int(m/number_of_threads)

# Await das Threads finalizarem
for t in list_threads:
    t.join()

# Se quiser verificar quantos elementos foram recebidos do get()
# print(len(list_values))

print(time.time() - timeSpent)