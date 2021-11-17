from pygame import mixer
import keyboard
import os 
import json
import threading

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json') as f:
  data = json.load(f)
mixer.init()

volume = 0.7
reset = True
comants = False
can_chance_z = True

def getSong():
    
    os.system("cls")
    found_song=False
    try:
            
        while not found_song:
            print("") 
            for names in data:
                print(names["volumen"]) 
            print("")
            category=str(input("Selecciona la categoria:  "))
            
            
            for names in data:
                if(names["volumen"]==category):
                    founded = False
                    while not founded:
                        for songs in names["songs"]:
                            print(songs["name"])
                        name=str(input("Selecciona la caccion: "))
                        for songs in names["songs"]:
                            if(songs["name"] == name):
                                founded=True
                                cancion = songs["url"]
                                return cancion
                        if not founded:
                            print("------your songs isn't founded------")
            if not found_song: 
                print("------your songs isn't founded------")
    except  EOFError as e:
        print(e)

def set_time_out(func, sec):
    # def func_wrapper():
        # set_interval(func, sec)
        # func()
    # t = threading.Timer(sec, func_wrapper)
    t = threading.Timer(sec, func)
    t.start()
    return t

def chance_z(): 
    global can_chance_z
    can_chance_z = True

cancion=getSong()
print(cancion)
if (cancion != None):
    mixer.music.load( str(dir_path+cancion))
    mixer.music.set_volume(volume)
    mixer.music.play()
    found_song = True
    salir = True
else:
    salir = False

while salir:
    if reset:
        
        os.system("cls")
        print("")
        print("press p by pause")
        print("press r by unpause")
        print("press s by stop")
        print("press e by select another music")
        print("press down by volume down")
        print("press up by volume up")
        print("press c by exit")
        print(" ")
        print("--press z by activate the opcion--")
        print("")
        reset=False
    if comants:
        if keyboard.is_pressed('p'):
            mixer.music.pause()
        if keyboard.is_pressed('r'):
            mixer.music.unpause()
        if keyboard.is_pressed('s'):
            mixer.music.stop()
        if keyboard.is_pressed('e'):
            reset=True
            mixer.music.stop()
            cancion=getSong()
            comants=False
            mixer.music.load(str(dir_path+cancion))
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
        print(f"opction actived is change {comants}")
        identidy=set_time_out(chance_z, 1)
identidy.cancel()
print("BYE")