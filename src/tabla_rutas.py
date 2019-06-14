import ruta


class TablaRutas:
    rutas = []
    id = None

    def __init__(self, i):
        self.id = i

    # Agrega una ruta a la tabla de rutas
    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    # Verifica si una ruta existe dentro de la tabla de rutas
    def existe(self, ruta2):
        print('running existe ruta?')

    # Convierte la tabla de rutas a un string
    # Retorna: String que contiene la información de la tabla de rutas
    def string_rutas(self):
        string = ''
        for r in range(len(self.rutas)):
            string += self.rutas[r].ruta_to_string()
            string += ';'
        print(string)
        return string

    # Convierte un string a una tabla de rutas
    def string_to_tabla(self, s):
        print('string to tabla')
        splitted = s

    # Recibe un string de tabla de rutas y actualiza la tabla propia con la informacion recibida
    def actualizar_tabla(self, tabla_string):
        print('actualizando tabla')
        self.string_to_tabla(tabla_string)
        for r in self.rutas:
            print('recibiendo ')

    # Imprime la tabla de rutas
    def imprimirTabla(self):
        print('imprimirTabla')


# Start execution
rr = ruta.Ruta('1', '2', '3', '4')
tabla = TablaRutas()
tabla.agregar_ruta(rr)
tabla.string_rutas()
