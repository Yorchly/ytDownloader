import os
from tkinter import Tk
from tkinter import filedialog


# Cuando la ruta es por ejemplo: /${HOME}/Ejemplo 1,
# al haber un espacio entre Ejemplo y 1, youtube-dl no funciona bien.
# Esta funcion sirve para añadir \ en los espacios.
def transform_path(path):
    path_split = path.split(" ")
    sol = ""
    for i in range(len(path_split)):
        if i < (len(path_split) - 1):
            sol += path_split[i] + "\\ "
        else:
            sol += path_split[i]
    return sol


# Obtiene la key de la url introducida por teclado
def get_key(url):
    try:
        url_split = url.split("=", 1)
        key = url_split[1]
        return key
    except:
        os.system("clear")
        print("URL invalida.")
        return ""


# Obtiene el path donde se va a almacenar la canción o el video
def get_path(music_directory):
    Tk().withdraw()
    # El bucle controla que no se introduzca una respuesta que pueda dar error.
    while True:
        resp = input("¿Desea seleccionar el directorio donde guardar " +
                     "audio/video/lista (por defecto se guardará en " + music_directory + ")?(s/n): ")
        if resp == 'S' or resp == 's' or resp == 'N' or resp == 'n':
            break
        else:
            print("Respuesta introducida incorrecta.")
    if resp == 'S' or resp == 's':
        # seleccionar directorio donde guardar.
        path = filedialog.askdirectory(initialdir=music_directory)
        # Si le da al boton cancelar recibirá una tupla vacía.
        # Se hace la comprobación para que no haya errores a la
        # hora de transformar el path.
        if path:
            directory = transform_path(path)
        else:
            directory = music_directory

    else:
        directory = music_directory

    return directory


def get_file(url, directory, type_of_file="mp3"):
    types_of_file = ["mp3", "mp4", "list"]
    is_download = False

    if type_of_file not in types_of_file:
        raise ValueError("Error el tipo de fichero no es ni mp3 ni mp4")

    # TODO
    # Completar con youtube-dl ya que pytube no funciona bien.
