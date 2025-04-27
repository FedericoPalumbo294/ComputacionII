import os, time, random


pid = os.fork()

acciones = [
    "llora desconsoladamente.",
    "grita al cielo: ¿por qué?",
    "se queda mirando al vacío.",
    "promete vengar a su hijo.",
    "se ríe nerviosamente."
]

if pid == 0:
    print("[HIJO] Finalizando... *música triste*")
    os._exit(0)
else:
    print("[PADRE] Mi hijo se fue... observen el zombie con 'ps -el'.")
    print(f"[PADRE] Mientras espero, {random.choice(acciones)}")
    time.sleep(15)
    os.wait()
    print("[PADRE] Al fin, mi hijo pudo descansar en paz. 🕊️")