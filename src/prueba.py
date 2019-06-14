import threading, time
from socket import *
import struct

import ruta

HOST = '224.3.29.72'
ports = [2001 + i * 0 for i in range(0,11)]
sockets = [[] for i in range(0,6)] #Indice 0 es para el socket que envia y el indice 1 es para el socket que recibe datos

# Instancias de tabla de rutas
tablaRuta1 = []
tablaRuta2 = []
tablaRuta3 = []
tablaRuta4 = []
tablaRuta5 = []
kill3 = False



def compartir():
    nombre = threading.current_thread().getName()
    count = 0
    if (threading.current_thread().getName() == 'comparte3'):
        while (count < 3):
            print('COMPARTE3')
            # Send tablaRutas3
            sent = sockets[3][0].sendto("Prueba", (HOST,2001))
            count += 1

    else:
        while (count < 10):
            if (threading.current_thread().getName() == 'comparte1'):
                sent = sockets[1][0].sendto("Prueba", (HOST, 2001))
                print('COMPARTE1')
                # Send tablaRutas1
            elif (threading.current_thread().getName() == 'comparte2'):
                sent = sockets[2][0].sendto("Prueba", (HOST, 2002))
                print('COMPARTE2')
                # Send tablaRutas2
            elif (threading.current_thread().getName() == 'comparte4'):
                sent = sockets[4][0].sendto("Prueba", (HOST, 2004))
                print('COMPARTE4')
                # Send tablaRutas4
            elif (threading.current_thread().getName() == 'comparte5'):
                sent = sockets[5][0].sendto("Prueba", (HOST, 2005))
                print('COMPARTE5')
                # Send tablaRutas5
            count += 1
            time.sleep(3)

def recibir():
    count = 0

    if (threading.current_thread().getName() == 'recibe3'):
        while (count < 3):
            print('recibe3')
            # Send tablaRutas3
            count += 1

    else:
        while (count < 100):
            try:
                if (threading.current_thread().getName() == 'recibe1'):
                    print("recibe1")
                    dato, address = sockets[1][1].recvfrom(1024)
                    print("Recibe 1 exitoso")
                    print(dato)
                    # Send tablaRutas1
                elif (threading.current_thread().getName() == 'recibe2'):
                    print("recibe2")
                    dato , address = sockets[2][1].recvfrom(1024)
                    print("Recibe 2 exitoso")
                    print(dato)
                    # Send tablaRutas2
                elif (threading.current_thread().getName() == 'recibe43'):

                    #sockets[4][1].bind(server_address)
                    dato, address = sockets[4][1].recvfrom(1024)
                    print(dato)
                    # Send tablaRutas4
                elif (threading.current_thread().getName() == 'recibe53'):

                    #sockets[5][1].bind(server_address)
                    dato, address = sockets[5][1].recvfrom(1024)
                    print(dato)
                    # Send tablaRuta
            except:
                pass
            count += 1
            time.sleep(3)

for num_hilo in range(1,6):

    #Crea la informacion de los sockets que envian y reciben del router actual
    grupo_envio = (HOST,ports[num_hilo])
    sock_envio = socket(AF_INET, SOCK_DGRAM)
    #sock_envio.settimeout(0.2)
    ttl = struct.pack('b', 5)
    sock_envio.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)

    grupo_recepcion = (HOST, 2001)
    sock_recibido = socket(AF_INET, SOCK_DGRAM)
    #settimeout(0.2)
    ttl = struct.pack('b', 1)
    sock_recibido.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, ttl)
    sock_recibido.setblocking(0)

    group = inet_aton(HOST)
    mreq = struct.pack('4sL', group, INADDR_ANY)
    sock_recibido.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)


    print(num_hilo)
    sockets[num_hilo].append(sock_envio)
    sockets[num_hilo].append(sock_recibido)



    server_address = ('', ports[11-num_hilo])
    server_address2 = ('', ports[11 - num_hilo])
    server_address3 = ('', ports[11 - num_hilo])
    server_address4 = ('', ports[11 - num_hilo])
    server_address5 = ('', ports[11 - num_hilo])



    if(num_hilo == 1):
        sockets[num_hilo][1].setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sockets[1][1].bind(server_address)
    if(num_hilo == 2):
        sockets[2][1].setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sockets[2][1].bind(server_address2)


    #

    hilo1 = threading.Thread(name='comparte%s' % num_hilo,
                            target=compartir)
    hilo2 = threading.Thread(name='recibe%s' % num_hilo,
                            target=recibir)
    hilo1.start()
    hilo2.start()



