from multiprocessing import Pipe, Queue

# Pipe: comunicación punto a punto (dos extremos conectados).
conn1, conn2 = Pipe()
conn1.send("Hola desde Pipe")
print(conn2.recv())

# Queue: cola segura para múltiples productores/consumidores.
q = Queue()
q.put("Hola desde Queue")
print(q.get())
