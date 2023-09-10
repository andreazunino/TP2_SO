import threading
import time

BUFFER_SIZE = 5
buffer = []
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def productor():
    while True:
        item = produce_item()  # Generar un elemento
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        mutex.release()
        full.release()
        time.sleep(1)  # Simular el proceso de producción

def consumidor():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        mutex.release()
        empty.release()
        consume_item(item)  # Procesar el elemento retirado
        time.sleep(1)  # Simular el proceso de consumo
