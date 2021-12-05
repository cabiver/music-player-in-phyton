import sys
from pygame import mixer
import keyboard
import os 
import json
import threading

opcion=sys.stdin.read()


dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json') as f:
  data = json.load(f)
mixer.init()

index=0
volume = 0.7
reset = True
comants = False
can_chance_z = True
founded = True

def press(event):
    global index
    global founded
    if event.name == 'flecha arriba':
        index-=1
        founded = True
    if event.name == 'flecha abajo':
        index+=1
        founded = True
keyboard.on_press(press)
def getSong():    
    global founded
    os.system("cls")
    found_song=False
    global index
    index=0
    while not found_song:
        print("") 
        for names in data:
            print(names["volumen"]) 
        print("")
        for names in data:
            founded = True
            if(names["volumen"]==opcion):
                while True:
                    if(founded):      
                        os.system("cls")
                        for i, songs in enumerate(names["songs"]):
                            if(i==index):
                                print(f"> {songs['name']}")
                            else:
                                print(f"- {songs['name']}")
                        founded=False
                    if keyboard.is_pressed("enter"):
                        return names["songs"][index]["url"]

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
        print("--press alt by activate the opcion--")
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
    if (keyboard.is_pressed('alt') and can_chance_z):
        comants = not comants
        can_chance_z=False
        print(f"opction actived is change {comants}")
        identidy=set_time_out(chance_z, 1)
identidy.cancel()
print("BYE")