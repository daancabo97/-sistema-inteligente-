import heapq
from base_conocimiento import BaseConocimiento  

class MotorInferencia:

        def __init__(self, base_conocimiento: BaseConocimiento):    
                self.bc = base_conocimiento
                self.recorrido = []  # Lista para registrar el recorrido de nodos




        def heuristica(self, nodo, objetivo):
                """Heurística simple basada en la distancia alfabética."""
                return abs(ord(objetivo) - ord(nodo))




        def busqueda_a_estrella(self, inicio, objetivo):
                """Implementa la búsqueda A* para encontrar la ruta óptima."""
                conjunto_abierto = []
                heapq.heappush(conjunto_abierto, (0, inicio))
                proveniente_de = {}
                costo_g = {nodo: float('inf') for nodo in self.bc.grafo}
                costo_g[inicio] = 0
                costo_f = {nodo: float('inf') for nodo in self.bc.grafo}
                costo_f[inicio] = self.heuristica(inicio, objetivo)

                while conjunto_abierto:
                    _, actual = heapq.heappop(conjunto_abierto)
                     
                    """ Asegurarse de que cada nodo visitado se agregue al recorrido """
                    self.recorrido.append(actual)

                    if actual == objetivo:
                        return self.reconstruir_camino(proveniente_de, actual)

                    for vecino, peso in self.bc.obtener_vecinos(actual):
                        costo_tentativo_g = costo_g[actual] + peso
                        if costo_tentativo_g < costo_g[vecino]:
                            proveniente_de[vecino] = actual
                            costo_g[vecino] = costo_tentativo_g
                            costo_f[vecino] = costo_g[vecino] + self.heuristica(vecino, objetivo)
                            heapq.heappush(conjunto_abierto, (costo_f[vecino], vecino))
           
                return None





        def reconstruir_camino(self, proveniente_de, actual):
                """Reconstruye el camino desde el nodo final al inicial."""
                camino = [actual]
                while actual in proveniente_de:
                    actual = proveniente_de[actual]
                    camino.append(actual)
                camino.reverse()
                return camino
