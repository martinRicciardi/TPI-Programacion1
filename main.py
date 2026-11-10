# Programa principal

from auxiliares import leer_entero, mostrar_menu
from opciones_menu import (
    cargar_herramientas,
    mostrar_inventario,
    consultar_stock,
    reporte_agotados,
    alta_producto,
    actualizar_stock,
)


def main():

    inventario = []
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        try:
            opcion = leer_entero('Seleccione una opción: ')
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError('Opción fuera de rango (1 a 7).')
        except ValueError as e:
            print(f'Error: {e}')
    print('Sistema finalizado.')


main()