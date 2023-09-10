import threading

n = 5  # Número de filósofos
tenedores = [threading.Semaphore(1) for _ in range(n)]

def filosofo(fil_id):
    while True:
        pensar(fil_id)
        tomar_tenedores(fil_id)
        comer(fil_id)
        dejar_tenedores(fil_id)

def pensar(fil_id):
    print(f'Filósofo {fil_id} está pensando')

def tomar_tenedores(fil_id):
    tenedores[fil_id].acquire()
    tenedores[(fil_id + 1) % n].acquire()

def comer(fil_id):
    print(f'Filósofo {fil_id} está comiendo')

def dejar_tenedores(fil_id):
    tenedores[fil_id].release()
    tenedores[(fil_id + 1) % n].release()

# Crear e iniciar hilos para cada filósofo
filosofos = [threading.Thread(target=filosofo, args=(i,)) for i in range(n)]
for filosofo in filosofos:
    filosofo.start()
