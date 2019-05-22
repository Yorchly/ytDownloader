#!/bin/bash
echo "MENU"
echo "1. Instalar sistemas con gestor de paquetes APT"
echo "2. Instalar sistemas con gestor de paquete pacman"
read opcion
convert=false
if [ "$opcion" = 1 ]; then
	echo "Instalando intérprete python 3"
	sudo apt install python3
	echo "Instalando youtube-dl desde repositorios"
	sudo apt install youtube-dl -y
	echo "Instalando pip3 desde repositorios"
	sudo apt install python3-pip -y
	echo "Actualizando librerias de youtube-dl"
	sudo pip3 install --upgrade youtube-dl
	echo "Instalando tkinter"
	sudo apt install python3-tk -y
	echo "Instalando ffmpeg"
	sudo apt install ffmpeg -y
	clear
	convert=true
elif [ "$opcion" = 2 ]; then
	echo "Instalando intérprete python 3"
	sudo pacman -S python3
	echo "Instalando pip3 desde repositorios"
	sudo pacman -S python-pip
	echo "Instalando tkinter"
	sudo pacman -S tk
	echo "Instalando youtube-dl"
	sudo pacman -S youtube-dl
	echo "Actualizando youtube-dl"
	sudo pip3 install --upgrade youtube-dl
	echo "Instalando ffmpeg"
	sudo pacman -S ffmpeg
	convert=true	
else
	echo "No se ha reconocido la entrada, saliendo del script"
fi

if [ "$convert" = true ]; then
	echo "Convirtiendo el fichero en una herramienta del sistema"
	cp ytDownloader.py ytDownloader
	chmod u+x ytDownloader
	sudo mv ytDownloader /usr/local/bin
	echo "ytDownloader se encuentra ahora en /usr/local/bin/"
	echo "Para ejecutarla tan sólo tienes que abrir la terminal y escribir ytDownloader"
fi


