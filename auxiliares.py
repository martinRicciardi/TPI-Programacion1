def leer_entero(mensaje):

    try:
        return int(input(mensaje))
    except ValueError:
        # Captura el error y lo lanza con otro mensaje
        raise ValueError('Debe ingresar un número entero.')


def pedir_nombre():

    nombre = input('Nombre de la herramienta: ').strip()
    if nombre == '':
        raise ValueError('El nombre no puede estar vacío.')
    return nombre


def buscar_herramienta(inventario, nombre):

    nombre_buscado = nombre.strip().lower()
    for producto in inventario:
        if producto['herramienta'].lower() == nombre_buscado:
            return producto
    return None


def pedir_nombre_nuevo(inventario):

    nombre = pedir_nombre()
    if buscar_herramienta(inventario, nombre) is not None:
        raise ValueError(f'La herramienta "{nombre}" ya existe en el inventario.')
    return nombre


def pedir_stock_inicial():

    stock = leer_entero('Stock inicial: ')
    if stock < 0:
        raise ValueError('El stock inicial no puede ser negativo.')
    return stock


def pedir_unidades():

    unidades = leer_entero('Unidades del movimiento: ')
    if unidades <= 0:
        raise ValueError('Las unidades deben ser un número mayor que 0.')
    return unidades


def mostrar_menu():

    print('\n=== CONTROL DE INVENTARIO - FERRETERÍA ===')
    print('1. Carga de herramientas')
    print('2. Visualización de inventario')
    print('3. Consulta de stock')
    print('4. Reporte de agotados')
    print('5. Alta de nuevo producto')
    print('6. Actualización de stock (venta / ingreso)')
    print('7. Salir')