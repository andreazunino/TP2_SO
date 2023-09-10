import multiprocessing

def proceso_hijo(mensaje):
    print(f'Hijo recibe el mensaje: {mensaje}')

if __name__ == '__main__':
    mensaje = "Hola, mundo!"
    
    # Crear un proceso hijo y pasarle un mensaje
    proceso = multiprocessing.Process(target=proceso_hijo, args=(mensaje,))
    proceso.start()
    proceso.join()

    print('Proceso principal ha terminado')
