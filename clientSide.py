import xmlrpc.client
import time
import random
import threading

# Número que seja divisível por 8,4,2
m = 800000

# Declaração do número de threads
number_of_threads = 8

list_values = []

# Função que usa as interfaces fornecidas pelo ServerSide.py
def funcao (init, end):
    # Declaração do Cliente Side RPC    
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        # Declaração de multiCall
        multi = xmlrpc.client.MultiCall(proxy)
        for i in range(init, end):
            multi.put(str(i), random.randint(0, m))
        for i in range (init, end):
            multi.get(str(i))
        list_values.append(tuple(multi()))

timeSpent = time.time()
init = 0
end = int(m/number_of_threads)
list_threads = []
for t in range(0, number_of_threads):
    t = threading.Thread(target=funcao, args=(init, end))
    t.start()
    list_threads.append(t)
    init = end
    end += end

for t in list_threads:
    t.join()

print(time.time() - timeSpent)
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    # Limpar a Hash
    proxy.clear()