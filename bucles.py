import pandas as pd

df = pd.DataFrame([
    {"nombre": "Luis", "ventas": 1200},
    {"nombre": "Ana", "ventas": 800},
    {"nombre": "Joaquín", "ventas": 500}
])

for i, fila in df.iterrows():
    if fila["ventas"] >= 1000:
        estado = "Top vendedor"
    elif fila["ventas"] >= 600:
        estado = "Vendedor medio"
    else:
        estado = "Bajo rendimiento"
    print(f"{fila['nombre']}: {estado}")
