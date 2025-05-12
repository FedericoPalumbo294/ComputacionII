# Este código hace que la señal SIGALRM  utilize una alarma temporizada.
# En este caso, el programa espera 5 segundos y luego activa una alarma que ejecuta un handler específico.
# Sin necesidad de enviar la señal manualmente, ya que el programa la activa automáticamente después de 5 segundos.
# Es parecida a la funcion time.sleep() pero con las diferencias son:

# time.time() es más flexible si necesitas hacer múltiples verificaciones o manejar 
# otros eventos a la vez, pero requiere más manejo manual.

# signal.alarm() es más simple y eficiente si solo te interesa ejecutar un evento
# después de un tiempo sin necesidad de hacer más verificaciones.

import signal
import time
import os

# Handler para SIGALRM
def handler_alarma(sig, frame):
    print("⏰ Pasaron 5 segundos. Se activó la alarma automáticamente.")
    exit(0)

# Asociamos la señal SIGALRM al handler
signal.signal(signal.SIGALRM, handler_alarma)

# Activamos una alarma que se dispara en 5 segundos
signal.alarm(5)

# Mostrar el PID por si querés hacer pruebas extra
print(f"PID del proceso: {os.getpid()}")
print("Esperando 5 segundos...")

# Mientras tanto, el programa sigue vivo
while True:
    time.sleep(1)
    print("Sigo esperando...")
