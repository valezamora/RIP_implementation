import ruta
import socket
import struct
from threading import Timer,Thread


class Router(Thread):
    tablaDeRutas = []
    listaDeAdyacencia = []

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        puerto = 7075

        #Prepara los datos requeridos para el socket de envio de informacion
        self.multicast_group = ('224.3.29.71', 10000)
        self.server_address = ('', 10000)
        self.socket_envio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ttl = struct.pack('b', 1)
        self.socket_envio.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.ttl)


    def compartir(self):
        print("Inicializando envio del nodo " + str(self.id))
        while 1:
            sent = self.socket_envio.sendto("mensaje".encode(), self.multicast_group)
            print("Nodo " + str(self.id) + " ha enviado un mensaje")
            timer_compartir = Timer(2, lambda: int()) #El timer requiere una funcion. Se escoge arbitrariamente int() pero no afecta
            timer_compartir.start()
            timer_compartir.join()


    def actualizarTabla(self):
        return None

    def imprimirTabla(self):
        return None

    def leerVecinos(self):
        while 1:
            print("Leyendo Vecinos")
            timer_leer = Timer(2, lambda: int()) #El timer requiere una funcion. Se escoge arbitrariamente int() pero no afecta
            timer_leer.start()
            timer_leer.join()


    def splitHorizon(self):
        return None

    def run(self):
        '''
        Metodo obligatorio de toda clase Thread
        Se ejecuta al hacerle start() o run() a la instancia de la clase
        :return: None
        '''

        thread_compartir = Thread(target=self.compartir())
        thread_compartir.start()
        print("Empezando segundo hilo")
        thread_leerVecinos = Thread(target=self.leerVecinos())
        thread_leerVecinos.start()



r = Router(1)
r.start()