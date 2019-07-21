#!/bin/bash
echo "MENU"
echo "1. Instalar sistemas con gestor de paquetes APT"
echo "2. Instalar sistemas con gestor de paquete pacman"
echo "Escribe la opcion: "
read opcion
convert=false
if [ "$opcion" = 1 ]; then
	echo "****INSTALANDO INTÉRPRETE PYTHON 3****"
	sudo apt install python3
	echo ""
	echo ""
	echo "****INSTALANDO YOUTUBE-DL****"
	sudo apt install youtube-dl -y
	echo ""
	echo ""
	echo "****INSTALANDO PIP 3****"
	sudo apt install python3-pip -y
	echo ""
	echo ""
	echo "****ACTUALIZANDO YOUTUBE-DL****"
	sudo pip3 install --upgrade youtube-dl
	echo ""
	echo ""
	echo "****INSTALANDO TKINTER****"
	sudo apt install python3-tk -y
	echo ""
	echo ""
	echo "****INSTALANDO FFMPEG****"
	sudo apt install ffmpeg -y
	echo ""
	echo ""
	clear
	convert=true
elif [ "$opcion" = 2 ]; then
	echo "****INSTALANDO INTÉRPRETE PYTHON 3****"
	sudo pacman -S python3
	echo ""
	echo ""
	echo "****INSTALANDO PIP 3****"
	sudo pacman -S python-pip
	echo ""
	echo ""
	echo "****INSTALANDO TKINTER****"
	sudo pacman -S tk
	echo ""
	echo ""
	echo "****INSTALANDO YOUTUBE-DL****"
	sudo pacman -S youtube-dl
	echo ""
	echo ""
	echo "****ACTUALIZANDO YOUTUBE-DL****"
	sudo pip3 install --upgrade youtube-dl
	echo ""
	echo ""
	echo "****INSTALANDO FFMPEG****"
	sudo pacman -S ffmpeg
	echo ""
	echo ""
	convert=true	
else
	echo "No se ha reconocido la entrada, saliendo del script"
fi

if [ "$convert" = true ]; then
	cp ytDownloader/ytDownloader.py ytDownloader/ytDownloader
	chmod u+x ytDownloader/ytDownloader
	sudo mv ytDownloader/ytDownloader /usr/local/bin
	echo "####################################### FINALIZADO #######################################"
	echo "Para ejecutar la aplicación, tan sólo tienes que abrir la terminal y escribir ytDownloader"
	echo "##########################################################################################"
fi


