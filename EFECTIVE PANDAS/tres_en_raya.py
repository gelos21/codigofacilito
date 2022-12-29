# Crear la matriz del tablero
tablero = [['-' for x in range(3)] for y in range(3)]

# Función para imprimir el tablero en pantalla
def imprimir_tablero():
  print("  0 1 2")
  for fila in range(3):
    print(fila, end=' ')
    for columna in range(3):
      print(tablero[fila][columna], end=' ')
    print()

# Función para validar un movimiento
def es_movimiento_valido(fila, columna):
  if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2:
    return tablero[fila][columna] == '-'
  else:
    return False

# Función para determinar si hay ganador
def hay_ganador():
  for fila in range(3):
    # Verificar si hay una fila completa
    if tablero[fila][0] != '-' and tablero[fila][0] == tablero[fila][1] and tablero[fila][1] == tablero[fila][2]:
      return tablero[fila][0]
  for columna in range(3):
    # Verificar si hay una columna completa
    if tablero[0][columna] != '-' and tablero[0][columna] == tablero[1][columna] and tablero[1][columna] == tablero[2][columna]:
      return tablero[0][columna]
  # Verificar si hay una diagonal completa
  if tablero[0][0] != '-' and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
    return tablero[0][0]
  if tablero[0][2] != '-' and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
    return tablero[0][2]
  # Verificar si hay empate
  for fila in range(3):
    for columna in range(3):
      if tablero[fila][columna] == '-':
        return None
  return '-'

#
