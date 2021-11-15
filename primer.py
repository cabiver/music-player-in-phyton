from pygame import mixer
import keyboard
import os 
import json
import threading

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json') as f:
  data = json.load(f)

mixer.init()
salir = True
volume = 0.3
reset = True
comants = True
can_chance_z = True

def getSong ():       
    print("") 
    for names in data:
        print(names["volumen"])
    category=str(input("Selecciona la categoria:  "))
    for names in data:
        if(names["volumen"]==category):
            for songs in names["songs"]:
                print(songs["name"])
            name=str(input("Selecciona la caccion: "))
            founded = False
            for songs in names["songs"]:
                if(songs["name"] == name):
                    founded=True
                    cancion = songs["url"]
                    return cancion
            return founded


def set_time_out(func, sec):
    def func_wrapper():
        # set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def chance_z(): 
    print("entre")
    global can_chance_z
    can_chance_z = True

cancion=getSong()
mixer.music.load(cancion)
mixer.music.set_volume(volume)
mixer.music.play()
while salir:
    if comants:
        if reset:
            print("")
            print("press p by pause")
            print("press r by unpause")
            print("press s by stop")
            print("press e by select another music")
            print("press down by volume down")
            print("press up by volume up")
            print("press c by exit")
            print("press z by cant exit without stop")
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
            cancion=getSong()
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
    if (keyboard.is_pressed('z') and can_chance_z):
        comants = not comants
        can_chance_z=False
        identidy=set_time_out(chance_z, 3)
        print(comants)
identidy.cancel()
print("adios")