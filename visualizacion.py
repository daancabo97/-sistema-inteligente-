import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation



def visualizar_grafo(grafo, recorrido, ruta_optima):
        """Visualiza el grafo y la ruta seguida por el algoritmo A*."""
        plt.close('all')  

        G = nx.Graph()
        for nodo, vecinos in grafo.items():
            for vecino, peso in vecinos.items():
                G.add_edge(nodo, vecino, weight=peso)

        pos = nx.spring_layout(G)
        fig, ax = plt.subplots(figsize=(10, 8))

        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        """ Verificar que el recorrido tenga elementos antes de crear la animación """
        if len(recorrido) == 0:
            print("Error: El recorrido está vacío. No se puede generar el grafico del recorrido.")
            return






        def actualizar(frame):
                ax.clear()
                nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgrey')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

                """ Dibujar la ruta óptima al final """
                if frame == len(recorrido) - 1:
                    nx.draw_networkx_nodes(G, pos, nodelist=ruta_optima, node_color='green')
                    nx.draw_networkx_edges(G, pos, edgelist=[(ruta_optima[i], ruta_optima[i+1]) for i in range(len(ruta_optima)-1)],
                                        edge_color='green', width=2)





        """ Crear la animación solo si el recorrido tiene elementos """
        anim = FuncAnimation(fig, actualizar, frames=len(recorrido), interval=50, repeat=False)
        plt.show()
