import threading, time
import socket

def compartir():
    nombre = threading.current_thread().getName()
    count = 0
    while (count < 10):
        print(nombre, ' - ', count)
        time.sleep(2)

def recibir():
    nombre = threading.current_thread().getName()
    print(nombre)
    time.sleep(2)

for num_hilo in range(5):
    hilo1 = threading.Thread(name='comparte%s' % num_hilo,
                            target=compartir)
    hilo2 = threading.Thread(name='recibe%s' % num_hilo,
                            target=recibir)
    hilo1.start()
    hilo2.start()
