import os
import signal
import time

pid_a = int(input("PID del Proceso A: "))
time.sleep(3)
print("[Proceso B] Enviando señal para continuar...")
os.kill(pid_a, signal.SIGUSR1)
