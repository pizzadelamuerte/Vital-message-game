import os
import random
import string
import time
from pyfiglet import Figlet
from colorama import Fore

os.system('cls||clear')

#iniciamos creando el título del juego con ASCII, se usa Figlet como librería
#posterior a eso se pinta el texto de todo el juego en amarillo usando la librería colorama

texto = Figlet(font="standard")
colorTexto = texto.renderText("Mensaje Vital")
resultado_txt = Fore.YELLOW + colorTexto

print(resultado_txt)

#Nivel de dificultad del juego, dependiendo del número que asignemos será el número de caracteres que se deberán memorizar
while True:
    dificultad = int(input('¿QUÉ NIVEL DE DIFICULTAD DESEAS? (4 - 10)'))
    if dificultad >= 4 and dificultad <= 10:
        break

#Se crea una variable para dejar en blanco para asignar los caracteres a memorizar, con un for
#donde se recorre con un random de string en mayúsculas hasta completar lo dicho en el while anterior

mensaje = ''

for i in range(dificultad):
    mensaje += random.choice(string.ascii_uppercase)

#Se limpia la pantalla y se imprime un mensaje donde se genera el random de caracteres que fue rellenado en la variable 'mensaje'

os.system('cls||clear')

print ('ESCRIBE ESTE MENSAJE:'
       '\n'
       '\n', mensaje)

#Un tiempo de espera de 0.5 segundos en relación al nivel de dificultad implementado
time.sleep(0.5*dificultad)

os.system('cls||clear')

#Se genera una variable input donde se insertará lo escrito por el jugador
#Después se crea un if donde si el mensaje (variable 'resultado') escrito por el jugador es igual los caracteres generados de forma random en la variable mensaje, se gana el juego
#de lo contrario se genera un mensaje de que se ha perdido el juego y se muestra la variable mensaje

print('Escribe el mensaje:'
      '\n')

resultado = input('')

if resultado == mensaje:
    print('MENSAJE CORRECTO'
          '\n' 'LA GUERRA HA TERMINADO!')
else:
    print('MENSAJE INCORRECTO'
          '\n' 'LA GUERRA CONTINÚA HASTA EL FINAL DE LOS TIEMPOS'
          '\n' 'EL MENSAJE CORRECTO ERA:'
          '\n', mensaje)