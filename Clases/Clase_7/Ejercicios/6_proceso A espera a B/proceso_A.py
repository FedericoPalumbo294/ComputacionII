import signal
import os

def continuar(sig, frame):
    print("Recibí señal de continuar. ¡Sigo trabajando!")
    exit(0)

signal.signal(signal.SIGUSR1, continuar)

print(f"[Proceso A] PID: {os.getpid()}. Esperando señal para continuar...")
signal.pause()
