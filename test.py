from pynput.keyboard import Listener, Key 

def on_press(key):
    if key.char == 'q':
        print('q key pressed')


with Listener(on_press=on_press) as listener:
    listener.join()

