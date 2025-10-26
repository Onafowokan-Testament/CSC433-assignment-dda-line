import matplotlib.pyplot as plt

def get_user_input():
    """I will get starting and ending coordinates from user"""
    print("=" * 50)
    print("DDA LINE DRAWING ALGORITHM - CSC433")
    print("=" * 50)
    
    x0 = int(input("Enter starting X coordinate (x0): "))
    y0 = int(input("Enter starting Y coordinate (y0): "))
    x1 = int(input("Enter ending X coordinate (x1): "))
    y1 = int(input("Enter ending Y coordinate (y1): "))
    
    return x0, y0, x1, y1

def calculate_dda_params(x0, y0, x1, y1):
    """Calculate DDA algorithm parameters"""
    dx = x1 - x0
    dy = y1 - y0
    
    # Calculate slope
    if dx != 0:
        m = dy / dx
    else:
        m = float('inf')  # Vertical line
    
    # Calculate steps
    steps = max(abs(dx), abs(dy))
    
    # Determine case
    if abs(m) < 1:
        case = "Case-01 (M < 1)"
    elif abs(m) == 1:
        case = "Case-02 (M = 1)"
    else:
        case = "Case-03 (M > 1)"
    
    return dx, dy, m, steps, case

def generate_dda_points(x0, y0, x1, y1, m, steps, case):
    """Generate all points using DDA algorithm"""
    points = []
    xp = float(x0)
    yp = float(y0)
    
    # Add starting point
    points.append((round(xp), round(yp)))
    
    # Generate intermediate points
    for i in range(steps):
        if abs(m) < 1:
            # Case-01: M < 1
            xp = xp + 1
            yp = yp + m
        elif abs(m) == 1:
            # Case-02: M = 1
            xp = xp + 1
            yp = yp + 1
        else:
            # Case-03: M > 1
            xp = xp + (1/m)
            yp = yp + 1
        
        points.append((round(xp), round(yp)))
    
    return points

def print_calculations(x0, y0, x1, y1, dx, dy, m, steps, case):
    """Print DDA calculations"""
    print("\n" + "=" * 50)
    print("CALCULATIONS")
    print("=" * 50)
    print(f"Starting Point: ({x0}, {y0})")
    print(f"Ending Point: ({x1}, {y1})")
    print(f"ΔX = {x1} - {x0} = {dx}")
    print(f"ΔY = {y1} - {y0} = {dy}")
    print(f"M (Slope) = ΔY / ΔX = {dy} / {dx} = {m:.4f}")
    print(f"Steps = max(|ΔX|, |ΔY|) = max({abs(dx)}, {abs(dy)}) = {steps}")
    print(f"Case: {case}")

def print_points_table(points):
    """Print table of generated points"""
    print("\n" + "=" * 50)
    print("GENERATED POINTS")
    print("=" * 50)
    print(f"{'Step':<8} {'X':<8} {'Y':<8} {'Point'}")
    print("-" * 50)
    
    # Show first 10 points
    for i in range(min(10, len(points))):
        x, y = points[i]
        print(f"{i:<8} {x:<8} {y:<8} ({x}, {y})")
    
    # Show middle points if there are many
    if len(points) > 20:
        print("...")
        mid = len(points) // 2
        for i in range(mid-2, mid+3):
            x, y = points[i]
            print(f"{i:<8} {x:<8} {y:<8} ({x}, {y})")
        print("...")
    
    # Show last 5 points
    if len(points) > 10:
        for i in range(max(10, len(points)-5), len(points)):
            x, y = points[i]
            print(f"{i:<8} {x:<8} {y:<8} ({x}, {y})")
    
    print(f"\nTotal Points Generated: {len(points)}")

def draw_line(points, x0, y0, x1, y1):
    """Draw the line using matplotlib"""
    # Extract x and y coordinates
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    # Create figure and axis
    plt.figure(figsize=(10, 8))
    
    # Plot the line
    plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='DDA Line')
    plt.plot(x_coords, y_coords, 'ro', markersize=3, label='Generated Points')
    
    # Mark start and end points
    plt.plot(x0, y0, 'go', markersize=10, label=f'Start ({x0}, {y0})')
    plt.plot(x1, y1, 'rs', markersize=10, label=f'End ({x1}, {y1})')
    
    # Add grid
    plt.grid(True, alpha=0.3)
    
    # Labels and title
    plt.xlabel('X Coordinate', fontsize=12)
    plt.ylabel('Y Coordinate', fontsize=12)
    plt.title('DDA Line Drawing Algorithm', fontsize=14, fontweight='bold')
    plt.legend(loc='best')
    
    # Set axis limits with some padding
    x_margin = abs(x1 - x0) * 0.1 or 10
    y_margin = abs(y1 - y0) * 0.1 or 10
    plt.xlim(min(x0, x1) - x_margin, max(x0, x1) + x_margin)
    plt.ylim(min(y0, y1) - y_margin, max(y0, y1) + y_margin)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run DDA algorithm"""
    # Step 1: Get user input
    x0, y0, x1, y1 = get_user_input()
    
    # Step 2: Calculate DDA parameters
    dx, dy, m, steps, case = calculate_dda_params(x0, y0, x1, y1)
    
    # Step 3: Print calculations
    print_calculations(x0, y0, x1, y1, dx, dy, m, steps, case)
    
    # Step 4: Generate points
    points = generate_dda_points(x0, y0, x1, y1, m, steps, case)
    
    # Step 5: Print points table
    print_points_table(points)
    
    # Step 6: Draw the line
    print("\n" + "=" * 50)
    print("Drawing line... (close the plot window to exit)")
    print("=" * 50)
    draw_line(points, x0, y0, x1, y1)

if __name__ == "__main__":
    main()