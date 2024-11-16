## Datos
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 14, 39, 69, 95, 114, 129, 139]
h = 1  # Intervalo fijo

# Cálculo del área usando la regla del trapecio
area_trapecio = 0
for i in range(1, len(x)):
    area_trapecio += (y[i] + y[i - 1]) * h / 2

# Cálculo del área usando la regla de Simpson
n = len(x) - 1  # número de intervalos
area_simpson = y[0] + y[-1]  # sumamos los extremos
for i in range(1, n, 2):  # sumamos los términos impares
    area_simpson += 4 * y[i]
for i in range(2, n - 1, 2):  # sumamos los términos pares
    area_simpson += 2 * y[i]
area_simpson *= h / 3  # multiplicamos por h/3

# Resultados
print(f"Área bajo la curva usando la regla del trapecio: {area_trapecio}")
print(f"Área bajo la curva usando la regla de Simpson: {area_simpson}")