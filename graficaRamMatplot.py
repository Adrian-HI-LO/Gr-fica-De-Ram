import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

fig, ax = plt.subplots()
x_datos, y_datos = [], []
linea, = ax.plot([], [], lw=2)
ax.set_xlabel('Segundos')
ax.set_ylabel('Ram GB')
ax.set_title('Uso de memoria RAM')

def actualizar(frame):
    info_memoria = psutil.virtual_memory()
    ram_gb = info_memoria.used / 1e9
    
    ahora = datetime.now()
    tiempo_actual = ahora.strftime("%H:%M:%S")
    
    x_datos.append(tiempo_actual)
    y_datos.append(ram_gb)
    
    if len(x_datos) > 30:
        x_datos.pop(0)
        y_datos.pop(0)
    
    linea.set_data(range(len(x_datos)), y_datos)
    ax.set_xlim(0, max(30, len(x_datos)))
    ax.relim()
    ax.autoscale_view()
    return linea,

ani = FuncAnimation(fig, actualizar, interval=1000)

plt.tight_layout()
plt.show()
