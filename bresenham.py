import time

import matplotlib.pyplot as plt


# DDA Algorithm
def dda_algorithm(x0, y0, x1, y1):
    start = time.perf_counter()

    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    points = []
    for _ in range(int(steps) + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    end = time.perf_counter()
    return points, (end - start) * 1000


# Bresenham's Algorithm
def bresenham_algorithm(x0, y0, x1, y1):
    start = time.perf_counter()

    dx = x1 - x0
    dy = y1 - y0
    p = 2 * dy - dx

    x, y = x0, y0
    points = [(x, y)]

    for _ in range(dx):
        if p < 0:
            x += 1
            p = p + 2 * dy
        else:
            x += 1
            y += 1
            p = p + 2 * dy - 2 * dx
        points.append((x, y))

    end = time.perf_counter()
    return points, (end - start) * 1000



def plot_lines(dda_points, bres_points):
    plt.figure(figsize=(8, 6))
    dda_x, dda_y = zip(*dda_points)
    bres_x, bres_y = zip(*bres_points)

    plt.plot(dda_x, dda_y, "bo-", label="DDA Line")
    plt.plot(bres_x, bres_y, "ro-", label="Bresenham Line")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("DDA vs Bresenham Line Drawing")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main program
def main():
    print("DDA vs Bresenham Line Drawing Algorithm\n")

    x0 = int(input("Enter x0: "))
    y0 = int(input("Enter y0: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))

    dda_points, dda_time = dda_algorithm(x0, y0, x1, y1)
    bres_points, bres_time = bresenham_algorithm(x0, y0, x1, y1)

    print("\n--- Results ---")
    print(f"DDA generated {len(dda_points)} points in {dda_time:.4f} ms")
    print(f"Bresenham generated {len(bres_points)} points in {bres_time:.4f} ms")

    if dda_time < bres_time:
        print("DDA was faster.")
    else:
        print("Bresenham was faster.")

    plot_lines(dda_points, bres_points)


if __name__ == "__main__":
    main()
