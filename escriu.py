# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys
import os
import subprocess
import pyttsx
from gtts import gTTS
import readchar
from PIL import Image

ordinals = ["primera", "segona", "tercera", "quarta", "cinquena", "sisena", "setena", "vuitena", "novena", "desena"]

def digues(frase):
    tts = gTTS(text=frase, lang='ca')
    tts.save("frase.mp3")
    os.system("vlc --play-and-exit --quiet frase.mp3")
    return

def ordinal(numero):
    if numero < 10:
        return ordinals[numero]
    else:
        return "següent"


print("JDH 27/08/2016 Bogotà")
print("Programa per ensenyar al Martí i a la Laia a escriure el seu nom (o un altre) en un teclat d'ordinador")
print("Command Line Arguments:" + str(len(sys.argv)))
print("Command Line Arguments List:" + str(sys.argv))

if len(sys.argv) != 2:
    print("Per funcionar s'ha de cridar el programa amb un nom. Per exemple: $ python joc-escriu-nom.py MARTI")
    sys.exit()

nom = sys.argv[1].upper()
if len(nom) < 2:
    print("El nom ha de ser de 2 lletres o mes")
    sys.exit()

index = 0
nomEscrit = "";
#imgOK = Image.open("bb8.png")
#imgKO = Image.open("darkvader.jpg")
digues("Escriu la " + ordinal(index) + " lletra")
while index < len(nom):
    print("Has d'escriure \"" + nom + "\" i has escrit \"" + nomEscrit + "\". Escriu una lletra:")
    print(nom + " -> " + nomEscrit)
    keyPressed = readchar.readchar().upper()
    if keyPressed == "EXIT":
        sys.exit()

    if len(keyPressed) > 1:
        #imgKO.show()
        p = subprocess.Popen(["display", "darkvader.jpg"])
        digues("Només has d'escriure una lletra. Torna-ho a provar")
        p.kill()
        #imgKO.close()
    else:
        if nom[index] != keyPressed:
            #imgKO.show()
            p = subprocess.Popen(["display", "darkvader.jpg"])
            digues("No has escrit la lletra correcte. Torna-ho a provar")
            p.kill()
            #imgKO.close()
        else:
            if index < (len(nom) - 1):
                nomEscrit = nomEscrit + keyPressed
                index = index + 1
                digues("Perfecte. Ara escriu la " + ordinal(index) + " lletra") 
            else:
                #imgOK.show()
                p = subprocess.Popen(["display", "bb8.png"])
                digues("Ja has acabat. Ho has fet molt bé")
                p.kill()
                #imgOK.close()
                index = index + 1
        
print("Fi del joc. Torna-ho a provar amb un altre nom")
digues("Fi del jòc. Si vols, torna-ho a provar amb un altre nòm")

