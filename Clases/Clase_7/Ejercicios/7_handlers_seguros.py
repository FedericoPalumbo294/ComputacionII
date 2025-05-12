import signal
import os

# ⚠️ Esto NO es seguro (usar print en el handler)
def handler_no_seguro(sig, frame):
    print("¡Señal recibida!")  # <-- print no es async-signal-safe
    exit(0)

# ✅ Esto ES seguro porque no usa print
# Usar os.write en el handler(os.write(1, b"mensaje\n"))
def handler_seguro(sig, frame):
    os.write(1, b"Senal recibida\n")  # write a STDOUT directamente
    os._exit(0)

signal.signal(signal.SIGINT, handler_seguro)

print("Esperando CTRL+C...")
signal.pause()
# 🧪 Probalo asi:
# 1. Ejecuta el script
# 2. Presiona CTRL+C
# 3. Observa el comportamiento
# 4. Cambia el handler a handler_no_seguro y repite