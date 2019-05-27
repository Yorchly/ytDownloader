#!/usr/bin/env python3.7
"""
En Manjaro tengo instalada una version 3.6.8 a parte de la versión 3.7 
instalada y cuando pongo python3 coge esta versión que está en 
/usr/local/bin en por lo que muchos paquetes de /usr/bin no 
los detecta. Si no funciona bien cambiar el shebang de 
#!/usr/bin/env python3.7 -> #!/usr/bin/env python3.
-------------------------------------------------------------------------------
Este programa esta diseñado para funcionar en python 3, además se debe 
tener instalado la herramienta pip para descarga de paquetes y tkinter.
Si no se dispone del interprete, pip y tkinter, ejecutar el script 
installer.sh.
Version funcional en ubuntu 18.04 LTS y en Manjaro 18.0.4
"""
import os
from tkinter import Tk
from tkinter import filedialog
from pathlib import Path


# Cuando la ruta es por ejemplo: /${HOME}/Ejemplo 1, 
# al haber un espacio entre Ejemplo y 1, youtube-dl no funciona bien. 
# Esta funcion sirve para añadir \ en los espacios.
def transformPath(path):
	pathSplit = path.split(" ")
	sol = ""
	for i in range(len(pathSplit)):
		if i < (len(pathSplit) - 1):
			sol += pathSplit[i] + "\\ "
		else:
			sol += pathSplit[i]
	return sol


# Obtiene la key de la url introducida por teclado
def getKey(url):
	try:
		urlSplit = url.split("=", 1)
		key = urlSplit[1]
		return key
	except:
		os.system("clear")
		print("URL invalida.")
		return ""


# Obtiene el path donde se va a almacenar la canción o el video
def getPath():
	Tk().withdraw()
	resp = ""
	# El bucle controla que no se introduzca una respuesta que pueda dar error.
	while True:
		resp = input("¿Desea seleccionar el directorio donde guardar "+
		"audio/video/lista (por defecto se guardará en "+music+")?(s/n): ")
		if resp == 'S' or resp == 's' or resp == 'N' or resp == 'n':
			break
		else:
			print("Respuesta introducida incorrecta.")
	if resp == 'S' or resp == 's':
		# seleccionar directorio donde guardar.
		path = filedialog.askdirectory(initialdir=music)
		# Si le da al boton cancelar recibirá una tupla vacía.
		# Se hace la comprobación para que no haya errores a la
		# hora de transformar el path.
		if path:
			directory = transformPath(path)
		else:
			directory = music
		
	else:
		directory = music

	return directory

directory = ""
invalida = False
lista = False

# Evita posibles errores a la hora de intentar descargar una cancion 
# y no estar actualizado youtube-dl
print("Comprobando si hay actualizaciones para youtube-dl.")
os.system("sudo pip3 install --upgrade youtube-dl")

# Obtiene el path de la carpeta Musica donde por defecto guardará 
# las canciones y vídeos que se descargue. Si no encuentra
# la carpeta Musica la busca como Music (solo contempla de 
# momento el español y el ingles)
music = str(Path.home())+"/Musica"
if os.path.exists(music) is False:
	music = str(Path.home())+"/Music"

while True:
	print("MENU")
	print("1.- Descargar audio")
	print("2.- Descargar video")
	print("3.- Descarga lista en el directorio actual")
	print("4.- Salir")
	opcion = int(input("Introduce opcion: "))
	os.system("clear")

	# Obtención de audio.
	if opcion == 1:
		url = input("Introduce url: ")
		key = getKey(url=url)

		if key != "":
			directory = getPath()
			res = os.system("youtube-dl -x --audio-format mp3 --audio-quality 0 -o"+
			directory+"/'%(title)s.%(ext)s'"+" "+key)
			if res == 256:
				print("Se ha producido un error en la conversion")
				print()
			elif res == 0:
				print("La conversion se ha realizado con exito y se ha guardado en"+
				"el directorio: "+directory)
				print()
		elif key == "":
			print("No se ha podido obtener el valor de la key.")
	# Obtención de vídeo		
	elif opcion == 2:
		url = input("Introduce url: ")
		key = getKey(url=url)

		if key != "":
			directory = getPath()
			res = os.system("youtube-dl -f mp4 -o "+directory+"/'%(title)s.%(ext)s'"+
			" "+key)
			if res == 256:
				print("Se ha producido un error en la conversion")
				print()
			elif res == 0:
				print("La conversion se ha realizado con exito y se ha guardado en"+
				"el directorio: "+directory)
				print()
		elif key == "":
			print("No se ha podido obtener el valor de la key.")
	# Obtención de lista			
	elif opcion==3:
		url = input("Introduce url: ")
		try:
			urlSplit = url.split("list=", 1)
			key = urlSplit[1]
		except:
			os.system("clear")
			print("URL invalida.")
			invalida = True
		lista = True
		break
	# Salida del programa
	elif opcion==4:
		break

if lista:
	os.system("youtube-dl -i -x --audio-format mp3 --audio-quality 0 "+key)
	# TODO 
	# Arreglar que la descarga de la lista no se pueda interrumpir con CTRL C cuando se le añade un directorio
	# donde guardar las canciones descargadas. 
	# res = os.system("youtube-dl -i -x --audio-format mp3 --audio-quality 0 -o "+directory+"/'%(title)s.%(ext)s'"+" "+key)

	
