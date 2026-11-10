from auxiliares import (
    leer_entero,
    pedir_nombre,
    buscar_herramienta,
    pedir_nombre_nuevo,
    pedir_stock_inicial,
    pedir_unidades,
)


def cargar_herramientas(inventario):
  
    # Paso 1. Cantidad de herramientas distintas a cargar
    total = 0
    while True:
        try:
            total = leer_entero('¿Cuántas herramientas distintas desea cargar? ')
            if total <= 0:
                raise ValueError('La cantidad de herramientas debe ser mayor que 0.')
            break
        except ValueError as e:
            print(f'Error: {e}')

    # Paso 2. Por cada herramienta: nombre y stock
    for numero in range(1, total + 1):
        print(f'\nHerramienta {numero} de {total}')

        # Nombre: se repite hasta que sea valido y no este duplicado
        nombre = ''
        while True:
            try:
                nombre = pedir_nombre_nuevo(inventario)
                break
            except ValueError as e:
                print(f'Error: {e}')

        # Stock: se repite solo el stock, conservando el nombre ingresado
        stock = 0
        while True:
            try:
                stock = pedir_stock_inicial()
                break
            except ValueError as e:
                print(f'Error: {e}')

        # Recien con nombre y stock validos se agrega al inventario
        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print(f'"{nombre}" cargada con {stock} unidades.')


def mostrar_inventario(inventario):

    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return
    print('\n--- Inventario actual ---')
    for producto in inventario:
        print(f'{producto["herramienta"]}: {producto["cantidad"]} unidades')


def consultar_stock(inventario):

    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return
    nombre = pedir_nombre()
    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print(f'La herramienta "{nombre}" no se encuentra en el catálogo.')
    else:
        print(f'Stock de {producto["herramienta"]}: {producto["cantidad"]} unidades.')


def reporte_agotados(inventario):

    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return
    agotados = 0
    print('\n--- Herramientas agotadas ---')
    for producto in inventario:
        if producto['cantidad'] == 0:
            print(producto['herramienta'])
            agotados += 1
    if agotados == 0:
        print('Ninguna herramienta tiene stock cero.')


def alta_producto(inventario):

    nombre = pedir_nombre_nuevo(inventario)
    stock = pedir_stock_inicial()
    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print(f'"{nombre}" agregada con {stock} unidades.')


def actualizar_stock(inventario):

    # Caso que el inventario este vacio
    if len(inventario) == 0:
        print('Todavía no hay herramientas cargadas.')
        return

    nombre = pedir_nombre()

    # Evalua que la herramienta exista
    producto = buscar_herramienta(inventario, nombre)
    if producto is None:
        print(f'La herramienta "{nombre}" no existe en el inventario.')
        return

    # Que movimiento se busca hacer
    print('Tipo de movimiento: 1) Venta  2) Ingreso')
    tipo = input('Elija el tipo de movimiento: ').strip().lower()
    es_venta = tipo == '1' or tipo == 'venta'
    es_ingreso = tipo == '2' or tipo == 'ingreso'
    if not es_venta and not es_ingreso:
        print('Tipo de movimiento inválido: solo se acepta venta o ingreso.')
        return

    # Funcion auxiliar que consulta cantidad de unidades
    unidades = pedir_unidades()

    # Validar stock suficiente y una vez validado modifica 
    if es_venta:
        if unidades > producto['cantidad']:
            raise ValueError(f'Stock insuficiente: hay {producto["cantidad"]} unidades y se intentan vender {unidades}.')
        producto['cantidad'] -= unidades
        print(f'Venta registrada. Stock de {producto["herramienta"]}: {producto["cantidad"]}.')
    else:
        producto['cantidad'] += unidades
        print(f'Ingreso registrado. Stock de {producto["herramienta"]}: {producto["cantidad"]}.')