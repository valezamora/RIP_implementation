import threading
import time
from socket import *
import struct

from tabla_rutas import TablaRutas

HOST = '224.3.29.72'
ports = [2001 + i * 0 for i in range(0, 11)]
sockets = [[] for i in range(0, 6)]  # Indice 0 es para el socket que envia y el indice 1 es para el socket que recibe datos
main_port = 2001


# Instancias de tabla de rutas
tablaRutas1 = TablaRutas(1)
tablaRutas2 = TablaRutas(2)
tablaRutas3 = TablaRutas(3)
tablaRutas4 = TablaRutas(4)
tablaRutas5 = TablaRutas(5)
kill3 = False

# Datos para inicializar routers
r1 = '10.0.1.0,255.255.255.0,10.0.1.1,1'
r2 = '10.0.3.0,255.255.255.0,10.0.3.1,1'
r4 = '10.0.2.0,255.255.255.0,10.0.2.1,1'
r5 = '10.0.4.0,255.255.255.0,10.0.4.1,1'

tablaRutas1.actualizar_tabla(r1)
tablaRutas2.actualizar_tabla(r2)
tablaRutas4.actualizar_tabla(r4)
tablaRutas5.actualizar_tabla(r5)

nodo = input('Digite el numero de nodo que desea desplegar (1-5): ')
print(nodo)

def compartir():
    nombre = threading.current_thread().getName()
    count = 0
    if (threading.current_thread().getName() == 'comparte3'):
        while (count < 3):
            print('COMPARTE3')
            # Send tablaRutas3
            sent = sockets[3][0].sendto(tablaRutas3.get_rutas().encode(), (HOST, main_port))
            count += 1

    else:
        while (count < 10):
            if threading.current_thread().getName() == 'comparte1':
                sent = sockets[1][0].sendto(tablaRutas1.get_rutas().encode(), (HOST, main_port))
                # Send tablaRutas1
            elif threading.current_thread().getName() == 'comparte2':
                sent = sockets[2][0].sendto(tablaRutas2.get_rutas().encode(), (HOST, main_port))
                # Send tablaRutas2
            elif threading.current_thread().getName() == 'comparte4':
                sent = sockets[4][0].sendto(tablaRutas4.get_rutas().encode(), (HOST, main_port))
                # Send tablaRutas4
            elif threading.current_thread().getName() == 'comparte5':
                sent = sockets[5][0].sendto(tablaRutas5.get_rutas().encode(), (HOST, main_port))
                # Send tablaRutas5
            count += 1

    time.sleep(10)  # Envia cada 10 segundos


def recibir():
    count = 0

    if threading.current_thread().getName() == 'recibe3':
        while (count < 3):
            dato, address = sockets[1][1].recvfrom(1024)
            dato = dato.decode()
            tablaRutas3.actualizar_tabla(dato)
            count += 1

    else:
        while (count < 10):
            try:
                if threading.current_thread().getName() == 'recibe1':
                    dato, address = sockets[1][1].recvfrom(1024)
                    dato = dato.decode()
                    tablaRutas1.actualizar_tabla(dato)

                elif threading.current_thread().getName() == 'recibe2':
                    dato , address = sockets[2][1].recvfrom(1024)
                    dato = dato.decode()
                    tablaRutas2.actualizar_tabla(dato)

                elif threading.current_thread().getName() == 'recibe4':
                    #sockets[4][1].bind(server_address)
                    dato, address = sockets[4][1].recvfrom(1024)
                    dato = dato.decode()
                    tablaRutas4.actualizar_tabla(dato)

                elif threading.current_thread().getName() == 'recibe5':
                    #sockets[5][1].bind(server_address)
                    dato, address = sockets[5][1].recvfrom(1024)
                    dato = dato.decode()
                    tablaRutas5.actualizar_tabla(dato)

                if nodo == 1:
                    tablaRutas1.imprimir_tabla()
                elif nodo == 2:
                    tablaRutas2.imprimir_tabla()
                elif nodo == 3:
                    tablaRutas3.imprimir_tabla()
                elif nodo == 4:
                    tablaRutas4.imprimir_tabla()
                elif nodo == 5:
                    tablaRutas5.imprimir_tabla()

            except:
                pass
            count += 1
            time.sleep(3)


for num_hilo in range(1, 6):
    # Crea la informacion de los sockets que envian y reciben del router actual
    grupo_envio = (HOST, ports[num_hilo])
    sock_envio = socket(AF_INET, SOCK_DGRAM)
    # sock_envio.settimeout(0.2)
    ttl = struct.pack('b', 5)
    sock_envio.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)

    grupo_recepcion = (HOST, main_port)
    sock_recibido = socket(AF_INET, SOCK_DGRAM)
    # settimeout(0.2)
    ttl = struct.pack('b', 1)
    sock_recibido.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)
    sock_recibido.setblocking(0)

    group = inet_aton(HOST)
    mreq = struct.pack('4sL', group, INADDR_ANY)
    sock_recibido.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

    sockets[num_hilo].append(sock_envio)
    sockets[num_hilo].append(sock_recibido)

    server_address = ('', ports[11 - num_hilo])
    print(num_hilo)
    sockets[num_hilo][1].setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockets[num_hilo][1].bind(server_address)

    hilo1 = threading.Thread(name='comparte%s' % num_hilo, target=compartir)
    hilo2 = threading.Thread(name='recibe%s' % num_hilo, target=recibir)
    hilo1.start()
    hilo2.start()
