import keyboard

def press(event):
    print(event.name)
    if event.name == 'flecha arriba':
        print("arriba")
    if event.name == 'flecha abajo':
        print("abajo")
    if event.name == 'enter':
        print("presionado")


keyboard.on_press(press)

while True:
    le=0