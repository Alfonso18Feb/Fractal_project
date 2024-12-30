import matplotlib.pyplot as plt
import numpy as np

def curva_levy_iterativo(x, y, length, depth):
    points = [(x, y)]
    stack = [(x, y, length, depth, 0)]
    while stack:
        x, y, length, depth, angle = stack.pop()
        if depth == 0:
            x_end = x + length * np.cos(np.radians(angle))
            y_end = y + length * np.sin(np.radians(angle))
            points.append((x_end, y_end))
        else:
            mid_length = length / (2 ** 0.5)
            stack.append((x, y, mid_length, depth - 1, angle + 45))
            x_mid = x + mid_length * np.cos(np.radians(angle + 45))
            y_mid = y + mid_length * np.sin(np.radians(angle + 45))
            stack.append((x_mid, y_mid, mid_length, depth - 1, angle - 45))
    return points

def curva_koch_iterativo(length, depth):
    points = [(0, 0), (length, 0)]
    for _ in range(depth):
        new_points = []
        for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
            dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
            x3, y3 = x1 + dx, y1 + dy
            x4, y4 = x3 + dx * np.cos(np.radians(60)) - dy * np.sin(np.radians(60)), y3 + dx * np.sin(np.radians(60)) + dy * np.cos(np.radians(60))
            x5, y5 = x1 + 2 * dx, y1 + 2 * dy
            new_points.extend([(x1, y1), (x3, y3), (x4, y4), (x5, y5)])
        new_points.append(points[-1])
        points = new_points
    return points

def sierpinski_iterativo(ax, ay, bx, by, cx, cy, depth):
    triangles = [(ax, ay, bx, by, cx, cy)]
    for _ in range(depth):
        new_triangles = []
        for ax, ay, bx, by, cx, cy in triangles:
            mx_ab, my_ab = (ax + bx) / 2, (ay + by) / 2
            mx_bc, my_bc = (bx + cx) / 2, (by + cy) / 2
            mx_ca, my_ca = (cx + ax) / 2, (cy + ay) / 2
            new_triangles.extend([
                (ax, ay, mx_ab, my_ab, mx_ca, my_ca),
                (mx_ab, my_ab, bx, by, mx_bc, my_bc),
                (mx_ca, my_ca, mx_bc, my_bc, cx, cy)
            ])
        triangles = new_triangles
    return triangles


def main():
    while True:
        print("\nSeleccione un fractal para dibujar:")
        print("1. Curva de Lévycon 15 max")
        print("2. Curva de Koch con 9 max")
        print("3. Triángulo de Sierpiński con 6 max")
        print("4. Salir")

        opcion = input("Ingrese el número de su elección: ")

        if opcion == "1":
            profundidad = int(input("Profundidad de la Curva de Lévy: "))
            puntos = curva_levy_iterativo(0, 0, 400, profundidad)
            x_coords, y_coords = zip(*puntos)
            plt.figure(figsize=(10, 10))
            plt.plot(x_coords, y_coords, color="blue", linewidth=0.5)
            plt.axis("equal")
            plt.axis("off")
            plt.show()

        elif opcion == "2":
            profundidad = int(input("Profundidad de la Curva de Koch: "))
            puntos = curva_koch_iterativo(300, profundidad)
            x_coords, y_coords = zip(*puntos)
            plt.figure(figsize=(10, 10))
            plt.plot(x_coords, y_coords, color="blue", linewidth=0.5)
            plt.axis("equal")
            plt.axis("off")
            plt.show()

        elif opcion == "3":
            profundidad = int(input("Profundidad del Triángulo de Sierpiński: "))
            triangulos = sierpinski_iterativo(0, 0, 1, 0, 0.5, 0.866, profundidad)
            plt.figure(figsize=(10, 10))
            for ax, ay, bx, by, cx, cy in triangulos:
                plt.fill([ax, bx, cx], [ay, by, cy], "blue", alpha=0.6)
            plt.axis("equal")
            plt.axis("off")
            plt.show()

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
