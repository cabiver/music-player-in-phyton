from pygame import mixer
import keyboard
import os 
import json
import threading

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/data.json') as f:
  data = json.load(f)
mixer.init()

index=0
volume = 0.7
reset = True
comants = False
can_chance_z = True
can_enter = True
founded = True

def chance_z(): 
    global can_chance_z
    can_chance_z = True
def chance_enter():
    global can_enter
    can_enter = True

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


def set_time_out(func, sec):
    # def func_wrapper():
        # set_interval(func, sec)
        # func()
    # t = threading.Timer(sec, func_wrapper)
    t = threading.Timer(sec, func)
    t.start()
    return t

def getSong():
        
    global founded
    global can_enter
    founded=True
    os.system("cls")
    found_song=False
    global index
    index=0
    select_volumen = True
    while not found_song:
        # print(data[2])
        while select_volumen:
            if(founded):
                os.system("cls")      
                for i, names in enumerate(data):
                    # print(names)
                    if(i==index):
                        print(f"> {names['volumen']}")
                    else:
                        print(f"- {names['volumen']}")
                    founded=False
            if keyboard.is_pressed("enter") and can_enter:
                # print(data[index])
                can_enter = False
                set_time_out(chance_enter, 1)
                opcion = data[index]
                select_volumen = False
        print("")
        founded = True
        index=0
        while True:
            if(founded):      
                os.system("cls")
                # print(opcion)
                for i, songs in enumerate(opcion["songs"]):
                    if(i==index):
                        print(f"> {songs['name']}")
                    else:
                        print(f"- {songs['name']}")
                founded=False
            # print(can_enter)
            if keyboard.is_pressed("enter")  and can_enter:
                return f"./songs/{opcion['songs'][index]['url']}"
                 



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