from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia
from visualizacion import visualizar_grafo

def main():
    
    """ Función principal para ejecutar el sistema de búsqueda de rutas """
    base_conocimiento = BaseConocimiento()
    motor = MotorInferencia(base_conocimiento)



    print("Sistema Inteligente de Búsqueda de Rutas")



    inicio = input("Ingrese el punto de inicio: ").strip().upper()
    destino = input("Ingrese el punto de destino: ").strip().upper()



    """ Validar que los puntos ingresados existan en el grafo """
    if inicio not in base_conocimiento.grafo or destino not in base_conocimiento.grafo:
        print("Los puntos ingresados no son válidos en el sistema de transporte.")
        return




    """ Realizar la búsqueda A* para encontrar la mejor ruta """
    ruta_optima = motor.busqueda_a_estrella(inicio, destino)




    """ Mostrar la mejor ruta o indicar que no se encontró una ruta disponible """
    if ruta_optima:
        print(f"La mejor ruta desde {inicio} hasta {destino} es: {' -> '.join(ruta_optima)}")
        visualizar_grafo(base_conocimiento.grafo, motor.recorrido, ruta_optima)
    else:
        print("No se encontró una ruta disponible. La animación no se generará.")



if __name__ == "__main__":
    main()
