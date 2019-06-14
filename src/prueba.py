import threading, time
import socket
import ruta
from tabla_rutas import TablaRutas

HOST = '127.0.0.1'
ports = [2001, 2002, 2003, 2004, 2005]
# Instancias de tabla de rutas
tablaRutas1 = TablaRutas(1)
tablaRutas2 = TablaRutas(2)
tablaRutas3 = TablaRutas(3)
tablaRutas4 = TablaRutas(4)
tablaRutas5 = TablaRutas(5)
kill3 = False

def compartir():
    nombre = threading.current_thread().getName()
    count = 0
    if (threading.current_thread().getName() == 'comparte3'):
        while (count < 3):
            print('COMPARTE3')
            # Send tablaRutas3.string_rutas
            count += 1

    else:
        while (count < 3):
            if (threading.current_thread().getName() == 'comparte1'):
                print('COMPARTE1')
                # Send tablaRutas1.string_rutas
            elif (threading.current_thread().getName() == 'comparte2'):
                print('COMPARTE2')
                # Send tablaRutas2.string_rutas
            elif (threading.current_thread().getName() == 'comparte4'):
                print('COMPARTE4')
                # Send tablaRutas4.string_rutas
            elif (threading.current_thread().getName() == 'comparte5'):
                print('COMPARTE5')
                # Send tablaRutas5.string_rutas
            count += 1
            time.sleep(3)

def recibir():
    nombre = threading.current_thread().getName()
    print(nombre)
    time.sleep(2)

for num_hilo in range(1,6):
    hilo1 = threading.Thread(name='comparte%s' % num_hilo,
                            target=compartir)
    hilo2 = threading.Thread(name='recibe%s' % num_hilo,
                            target=recibir)
    hilo1.start()
    hilo2.start()
