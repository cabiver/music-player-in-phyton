# import keyboard

# def press(event):
#     print(event.name)
#     if event.name == 'flecha arriba':
#         print("arriba")
#     if event.name == 'flecha abajo':
#         print("abajo")
#     if event.name == 'enter':
#         print("presionado")


# keyboard.on_press(press)

# while True:
#     le=0
import os


dirs = os.listdir("./songs")
# print(dirs)

json = open("data.json", "w")

json.write("")
json.close()

f = open("data.json", "a")
f.write("[\n")
for index, data in enumerate(dirs):
    
    # print(len(dirs)-1)
    # print(data)
    f.write("    {\n")
    f.write(f'        "volumen": "{data}", \n')
    dirsSongs = os.listdir(f"./songs/{data}")
    f.write(f'        "songs": [\n')
    # print(dirsSongs)
    for i, songData in enumerate(dirsSongs):
        f.write('            {\n')
        f.write(f'               "name": "{songData}", \n')
        f.write(f'               "url": "{data}/{songData}" \n')
        if(i == (len(dirsSongs)-1) ):
            f.write("            }\n")
        else:
            f.write("            },\n")    
    # print(index)
    f.write(f'        ]\n')
    if(index == (len(dirs)-1) ):
        f.write("    }\n")
    else:
        f.write("    },\n")
    

f.write("]")
f.close()
