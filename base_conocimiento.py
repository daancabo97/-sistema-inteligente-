class BaseConocimiento:
    
    def __init__(self):

        """Cada nodo es una estación, y cada arista representa una conexión con su peso (distancia o tiempo)."""
        self.grafo = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'D': 1, 'E': 5},
            'C': {'A': 3, 'F': 6},
            'D': {'B': 1, 'G': 2},
            'E': {'B': 5, 'G': 1},
            'F': {'C': 6, 'G': 3},
            'G': {'D': 2, 'E': 1, 'F': 3}
        }

    def obtener_vecinos(self, nodo):
        """Retorna los vecinos del nodo junto con el peso de las aristas."""
        return self.grafo.get(nodo, {}).items()
