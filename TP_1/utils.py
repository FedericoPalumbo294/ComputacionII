import hashlib

def calcular_hash(bloque):
    bloque_str = str(bloque["prev_hash"]) + str(bloque["datos"]) + str(bloque["timestamp"])
    return hashlib.sha256(bloque_str.encode()).hexdigest()
