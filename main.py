import my_def
from gtts import gTTS
import os
import random
import math as mate


def reproducir_texto(texto, idioma='en'):
    tts = gTTS(text=texto, lang=idioma)
    tts.save("temp.mp3")  # Guarda el audio como un archivo temporal (temp.mp3)
    os.system("start temp.mp3")  # Reproduce el archivo MP3
    return("            Listen carefully to days of the week")

def Menu():
    menu = """
                    Learn English With Python

    1. Days of the week

    """
    return menu


def option_1():
    mensaje = """
                    Let's study the days of the week
            
    1. Learn
    2. listen
    3. write
    4. menu
    """
    print(mensaje)
    opcion = int(input("type an option: "))
    if opcion == 1:
        print("             Days of the week\n")
        for i in my_def.Dias_en_Ingles:
            print(f"=> {i}")
    elif opcion == 2:
        separador = ","
        texto = separador.join(my_def.Dias_en_Ingles)
        print(reproducir_texto(texto))
    elif opcion == 3:
        num = 0
        while num < 7:
            dia = random.choice(my_def.Dias_en_español)
            respuesta = input(f"As {dia} is written in english: => ")
            
            if respuesta in my_def.Dias_en_Ingles:
                
                print("Very Good")
                my_def.Dias_en_español.remove(dia)
                my_def.Dias_en_Ingles.remove(respuesta)
                print(my_def.Dias_en_Ingles)
                print(len(my_def.Dias_en_Ingles))
                num += 1
            else:
                print("Intenta de nuevo")
    elif opcion == 4:
        return options()
    return (option_1())
    
 
    
def options():
    print(Menu())
    opcion = int(input("type an option: "))
    if opcion == 1:
        return option_1()
    

  
print(options())
