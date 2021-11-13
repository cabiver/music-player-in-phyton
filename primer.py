from pygame import mixer
import keyboard
import os 
import json
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json') as f:
  data = json.load(f)

mixer.init()
salir = True
volume = 1
reset = True
for names in data:
    print(names["name"])

cancion=str(input("Selecciona la caccion: "))


mixer.music.load(cancion)
mixer.music.set_volume(volume)
mixer.music.play()

while salir:
    if reset:
        print("")
        print("press p by pause")
        print("press r by unpause")
        print("press s by stop")
        print("press e by select another music")
        print("press down by volume down")
        print("press up by volume up")
        print("press c by exit")
        print("")
        reset=False
    if keyboard.is_pressed('p'):
        mixer.music.pause()
    if keyboard.is_pressed('r'):
        mixer.music.unpause()
    if keyboard.is_pressed('s'):
        mixer.music.stop()
    if keyboard.is_pressed('e'):
        mixer.music.stop()
        cancion=str(input('Select your music: '))
        mixer.music.load(cancion)
        mixer.music.set_volume(volume)
        mixer.music.play()
    if keyboard.is_pressed('down'):
        volume-=0.00034
        if(volume<0):
            volume=0
        mixer.music.set_volume(volume)
    if keyboard.is_pressed('up'):
        volume+=0.00034
        if(volume>1):
            volume=1
        
        mixer.music.set_volume(volume)
    if keyboard.is_pressed('c'):
        salir = False
    
        
print("adios")