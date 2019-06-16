class Ruta:
    def __init__(self, red, mascara, siguiente, distancia):
        self.red = red
        self.mascara = mascara
        self.siguiente = siguiente
        self.distancia = distancia

    def ruta_to_string(self):
        return self.red + ',' + self.mascara + ',' + self.siguiente + ',' + str(self.distancia)
