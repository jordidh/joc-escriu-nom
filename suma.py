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

def isIntFrom1To9(value):
    try: 
        iValue = int(value)
        if iValue < 0 or iValue > 9:
            return False
        return True
    except ValueError:
        return False

def isInt(value):
    try: 
        iValue = int(value)
        return True
    except ValueError:
        return False

print("JDH 03/10/2017 Barcelona")
print("Programa per ensenyar al Martí i a la Laia a sumar")
print("Command Line Arguments:" + str(len(sys.argv)))
print("Command Line Arguments List:" + str(sys.argv))

if len(sys.argv) != 3:
    print("Per funcionar s'ha de cridar el programa amb dos valors. Per exemple: $ python joc-suma.py 2 3")
    sys.exit()

valor1 = sys.argv[1].upper()
if isIntFrom1To9(valor1) == False:
    print("El primer valor ha de ser un número del 1 al 9")
    sys.exit()

valor2 = sys.argv[2].upper()
if isIntFrom1To9(valor2) == False:
    print("El segón valor ha de ser un número del 1 al 9")
    sys.exit()

valorEscrit = 0;
valorEsperat = int(valor1) + int(valor2)
while valorEscrit != valorEsperat:
    digues("Quan sumen " + valor1 + " i " + valor2)
    valor = raw_input('Suma:')
    if (isInt(valor) == False):
        if valor == "EXIT":
            sys.exit();
        else:
            p = subprocess.Popen(["display", "darkvader.jpg"])
            digues("Has d'escriure un número. Torna-ho a provar")
            p.kill()
    else:
        valorEscrit = int(valor)
        if (valorEscrit == valorEsperat):
            p = subprocess.Popen(["display", "bb8.png"])
            digues("Molt bé! galinfardeu")
            p.kill()
        else:
            p = subprocess.Popen(["display", "darkvader.jpg"])
            digues("La suma no és correcta. Torna-ho a provar")
            p.kill()
print("Fi del joc. Torna-ho a provar amb uns altres número")

