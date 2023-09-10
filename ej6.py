import threading

class Monitor:
    def __init__(self):
        self.semaphore = threading.Semaphore(1)
        self.data = 0

    def modificar_data(self, nuevo_valor):
        with self.semaphore:
            self.data = nuevo_valor

    def obtener_data(self):
        with self.semaphore:
            return self.data

def hilo_modificar(monitor):
    for i in range(5):
        nuevo_valor = monitor.obtener_data() + 1
        monitor.modificar_data(nuevo_valor)
        print(f'Hilo Modificar: Data = {nuevo_valor}')

def hilo_leer(monitor):
    for i in range(5):
        data_actual = monitor.obtener_data()
        print(f'Hilo Leer: Data = {data_actual}')

# Crear una instancia del monitor
mi_monitor = Monitor()

# Crear hilos que modifican y leen la data del monitor
hilo_mod = threading.Thread(target=hilo_modificar, args=(mi_monitor,))
hilo_lectura = threading.Thread(target=hilo_leer, args=(mi_monitor,))

# Iniciar los hilos
hilo_mod.start()
hilo_lectura.start()

# Esperar a que los hilos terminen
hilo_mod.join()
hilo_lectura.join()
