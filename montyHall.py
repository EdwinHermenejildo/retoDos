# Monty Hall problem
import random
import sys
import re
import settings

# Array with coches of the puertas
def puerta_aleatoria(cantidad_puertas):
  puertas = []
  for x in range(cantidad_puertas):
    puertas.append(x)
    puertas[x] = "cabra"
  puertas[random.randint(0, (cantidad_puertas - 1))] = "coche"
  return puertas

# Monty Hall abrir una puerta
def abrir_puerta(jugador_sel, puertas):
  abrir = jugador_sel
  if (puertas[jugador_sel] == "coche"):
    abrir = random.randint(0, 2)
    while (abrir == jugador_sel):
      abrir = random.randint(0, 2)
    puertas[abrir] = "abrir"
  else:
    index = puertas.index("coche")
    while ((abrir == jugador_sel) or (abrir == index)):
      abrir = random.randint(0, 2)
    puertas[abrir] = "abrir"

  return puertas

def check_is_digit(input_str):
    if input_str.strip().isdigit():
      return True
    else:
      print("El valor esperado es un número.")
      return False

def obtener_numero_puertas():
  while True:
    numero_puertas = input("Por favor vuelva a intentarlo: ")
    if check_is_digit(numero_puertas):
      if int(numero_puertas) >= 3:
        break
      else:
        print("El valor esperado debe ser mayor a 3.")
  return int(numero_puertas)


def main(argv):
  try:
    if check_is_digit(argv[0]):
      numero_puertas = int(argv[0])
      if numero_puertas >= 3:
        pass
      else:
        numero_puertas = obtener_numero_puertas()
    else:
      numero_puertas = obtener_numero_puertas()

    intentos = settings.intentos
    victorias = 0
    derrotas   = 0

    for i in range(intentos):
      # Generar cantidad de puertas
      puertas = puerta_aleatoria(numero_puertas)

      # El jugador selecciona una puerta
      seleccion_jugador = random.randint(0, (numero_puertas-1))

      # Monty Hall abrir una puerta con una cabra
      puertas = abrir_puerta(seleccion_jugador, puertas)

      # El jugador cambia de puerta
      if (seleccion_jugador == puertas.index("coche")):
        seleccion_jugador = puertas.index("cabra")

      elif (seleccion_jugador == puertas.index("cabra")):
        seleccion_jugador = puertas.index("coche")

      # Contador de victorias y derrotas
      if puertas[seleccion_jugador] == "coche":
        victorias = victorias + 1
      else:
        derrotas = derrotas + 1

    print(f"{intentos} intentos")
    print(f"Ganaste {victorias} veces.")
    print(f"Perdiste {derrotas} veces.")

    print("Porcentaje de ganancia: {:.2f}%".format(((victorias/intentos)*100)))
  except:
    print("Es necesario pasar como parámetros la cantidad de puertas.")

if __name__ == "__main__":
  main(sys.argv[1:])