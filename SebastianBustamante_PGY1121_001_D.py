import numpy as np

lista_asientos = [i for i in range (1,101)]
lista_asientos_comprados = []
cant = 0
ganancia_total = 0

def compra_entradas():
  cant = int(input("Ingrese la cantidad de entradas deseadas: "))
  while cant > 3 or cant < 1:
    print("Cantidad invalida, las entradas deben ser entre 1 y 3")
    cant = int(input("Ingrese la cantidad de entradas deseadas:"))
  return(cant)

def asignar_asiento(a):
  while a!=0:
    try:
      print(lista_asientos)
      asiento = int(input("Ingrese su asiento deseado: "))
      if asiento in lista_asientos:
        a -= 1
        rut = int(input("Ingrese su rut (sin puntos, ni digito verificador): "))
        lista_x = [asiento,rut]
        lista_asientos_comprados.append(lista_x)
        lista_asientos.pop(asiento-1)
        lista_asientos.insert(asiento-1,"x")
        print("Asignación completa.")
      elif asiento not in lista_asientos:
        print("Asiento no disponible") 
    except:
      ValueError
      print("Valor invalido, intente nuevamente")
  return (lista_asientos_comprados, lista_asientos)

def ganancias_totales():
  platinum = 0
  gold = 0
  silver = 0

  for i in lista_asientos_comprados:
    a = i[0]
    if a in range (1,21):
      platinum += 120000
    if a in range (22,51):
      gold += 80000
    if a in range (52,101):
      silver += 50000
  ganancias_totaless = platinum + silver + gold

  print(f"Las ganancias totales son: {ganancias_totaless}")


sw = 1
## MENU ##
print ("""
=------------ Creativos.cl ------------=

      1. Comprar entradas.
      2. Mostrar ubicaciones disponibles.
      3. Ver listado de asistentes
      4. Mostrar ganancias totales
      5. Salir.

=------------ Michael  Jam ------------=
""")
## OPCIONES ##
while sw == 1:
  try:
    op = int(input("Ingrese su opción deseada: "))
    if op == 1:
      print("""
=------------ Creativos.cl ------------=

             VALOR ENTRADAS

        PLATINUM = $120.000 PESOS (1-20)
        GOLD = $80.000 PESOS (21-50)
        SILVER = $50.000 PESOS (51-100)

=------------ Michael  Jam ------------=
      """)
      asignar_asiento(compra_entradas())
    if op == 2:
      print(lista_asientos)
    if op == 3:
      print("hola mundo!")
    if op == 4:
      ganancias_totales()
    if op == 5:
      sw = 0
      print("""
=------------ Creativos.cl ------------=

          SALIENDO DEL SISTEMA...



     Sebastian Bustamante 12-07-2023
     
=------------ Michael  Jam ------------=  
      """)
  except:
    ValueError
    print("Dato invalido, intente utilizar solo los números de las opciones.")