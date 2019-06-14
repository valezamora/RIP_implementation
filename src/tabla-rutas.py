import ruta

class TablaRutas:
    rutas = []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    # Convierte la tabla de rutas a un string
    def string_rutas(self):
        string = ''
        for r in range(len(self.rutas)):
            string += self.rutas[r].ruta_to_string()
            string += ';'
        print(string)

    # Convierte un string a una tabla de rutas
    def string_to_tabla(self):
        print('string to tabla')

    # Recibe una tabla de rutas y actualiza la tabla propia con la informacion recibida
    def actualizarTabla(self, tabla):
        print('actualizando tabla')
        for r in self.rutas:
            print('recibiendo ')


# Start execution
rr = ruta.Ruta('1', '2', '3', '4')
tabla = TablaRutas()
tabla.agregar_ruta(rr)
tabla.string_rutas()
