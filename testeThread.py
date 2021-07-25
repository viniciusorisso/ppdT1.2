import xmlrpc.client
import time
import random
import threading

# Número que seja divisível por 8,4,2
m = 80000

# Declaração do número de threads
maximum_threads = 8
number_of_threads = 8

list_values = []

# Função que usa as interfaces fornecidas pelo ServerSide.py
def funcao (init, end):
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        multi = xmlrpc.client.MultiCall(proxy)
        for i in range(init, end):
            multi.put(str(i), random.randint(0, m))
            multi.get(str(i))
        list_values.append(tuple(multi()))

timeSpent = time.time()
# Declaração do Cliente Side RPC
init = 0
end = int(m/maximum_threads)
for j in range (maximum_threads//number_of_threads):
    list_threads = []
    
    for t in range(0, number_of_threads):
        t = threading.Thread(target=funcao, args=(init, end))
        list_threads.append(t)
        init = end
        end += end
    
    for t in list_threads:
        t.start ()

    for t in list_threads:
        t.join ()

print(time.time() - timeSpent)  