from ruta import Ruta

class TablaRutas:
    rutas = []
    id = None

    def __init__(self, i):
        self.id = i

    # Agrega una ruta a la tabla de rutas
    def agregar_ruta(self, ruta2):
        encontrado = False
        for ruta in self.rutas:
            # La ruta ya esta en la tabla, actualiza la distancia si es menor que la que esta actualmente
            if ruta.red == ruta2.red and (ruta2.distancia + 1) < ruta.distancia:
                ruta.siguiente = ruta2.siguiente
                ruta.distancia = ruta2.distancia + 1
                encontrado = True

        if not encontrado:
            # Revisar cual es el siguiente que tiene que agregar
            self.rutas.append(Ruta(ruta2.red, ruta2.mascara, ruta2.siguiente, ruta2.distancia+1))

    # Verifica si una ruta existe dentro de la tabla de rutas
    def existe(self, ruta2):
        found = False
        for ruta in self.rutas:
            if ruta.red == ruta2.red:
                found = True
        return found

    # Convierte la tabla de rutas a un string
    # Retorna: String que contiene la informacion de la tabla de rutas cada ruta separada por un ';'
    def get_rutas(self):
        string = ''
        for r in range(len(self.rutas)):
            string += self.rutas[r].ruta_to_string()
            string += ';'
        string = string[:-1]
        return string

    # Convierte un string a una tabla de rutas
    def string_to_tabla(self, s):
        splitted = s.split(';')
        new_routes = []
        for r in splitted:
            data = r.split(',')
            if len(data) == 4:
                new_routes.append(Ruta(data[0], data[1], data[2], int(data[3])))

        return new_routes

    # Recibe un string de tabla de rutas y actualiza la tabla propia con la informacion recibida
    def actualizar_tabla(self, tabla_string):
        received_routes = self.string_to_tabla(tabla_string)
        for r in received_routes:
            self.agregar_ruta(r)

    # Imprimir tabla de rutas
    def imprimir_tabla(self):
        print('\nTabla ' + str(self.id))
        print('Cantidad de rutas: ', len(self.rutas))
        print('Direccion\tMascara\t\t\tSiguiente\t\tDistancia')
        for ruta in self.rutas:
            print(ruta.red + '\t' + ruta.mascara + '\t' + ruta.siguiente + '\t\t' + str(ruta.distancia))


# Start execution
# rr = Ruta('10.0.1.0', '255.255.255.0', '192.111.111.11', '4')
# tabla = TablaRutas(1)
# tabla.agregar_ruta(rr)
# tabla.get_rutas()
# tabla.actualizar_tabla('10.0.1.0,255.255.255.0,1,1;2,255.255.255.0,2,2')
