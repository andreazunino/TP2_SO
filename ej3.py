import threading
import time

class Impresora:
    def __init__(self):
        self.semaphore = threading.Semaphore(1)  # Inicialmente, el semáforo se establece en 1

    def imprimir(self, documento):
        with self.semaphore:
            print(f'Imprimiendo: {documento}')
            time.sleep(1)  # Simula la impresión

def hilo_impresion(impresora, documento):
    while True:
        # Sección no crítica: Preparación del trabajo de impresión

        # Entrar en la sección crítica (llamada a imprimir)
        impresora.imprimir(documento)

        # Sección no crítica: Finalización del trabajo de impresión

if __name__ == "__main__":
    impresora = Impresora()

    hilo1 = threading.Thread(target=hilo_impresion, args=(impresora, "Documento A"))
    hilo2 = threading.Thread(target=hilo_impresion, args=(impresora, "Documento B"))

    hilo1.start()
    hilo2.start()
