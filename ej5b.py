import threading

resource = 0
readers = 0
mutex = threading.Semaphore(1)
rw_mutex = threading.Semaphore(1)

def lector():
    global resource, readers
    while True:
        mutex.acquire()
        readers += 1
        if readers == 1:
            rw_mutex.acquire()
        mutex.release()
        
        # Leer el recurso compartido
        print(f'Lector leyendo: {resource}')
        
        mutex.acquire()
        readers -= 1
        if readers == 0:
            rw_mutex.release()
        mutex.release()

def escritor():
    global resource
    while True:
        rw_mutex.acquire()
        
        # Modificar el recurso compartido
        resource += 1
        print(f'Escritor escribiendo: {resource}')
        
        rw_mutex.release()
