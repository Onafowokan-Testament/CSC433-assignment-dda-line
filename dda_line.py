import matplotlib.pyplot as plt

x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

dx = x1 - x0
dy = y1 - y0

steps = max(abs(dx), abs(dy))
x_inc = dx / steps
y_inc = dy / steps

x = x0
y = y0
points = []

for i in range(steps + 1):
    points.append((round(x), round(y)))
    x += x_inc
    y += y_inc

print("Generated Points:")
for p in points:
    print(p)

# Plot
plt.plot([p[0] for p in points], [p[1] for p in points], "bo-")
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
