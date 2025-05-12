import os
import signal
import time

pid_destino = int(input("PID del proceso receptor: "))
os.kill(pid_destino, signal.SIGUSR1)
print(f"Enviada SIGUSR1 a {pid_destino}")
