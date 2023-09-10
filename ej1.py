import threading

# Crear un semáforo para garantizar que solo un hilo acceda a la lista a la vez
semaphore = threading.Semaphore(1)

# Una lista compartida entre hilos
shared_list = []

def agregar_elemento(elemento):
    global shared_list
    with semaphore:
        shared_list.append(elemento)
        print(f"Elemento {elemento} agregado por el hilo {threading.currentThread().name}")

def main():
    # Crear tres hilos
    hilos = []
    for i in range(3):
        hilo = threading.Thread(target=agregar_elemento, args=(i,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print(f"Lista compartida final: {shared_list}")

if __name__ == "__main__":
    main()
