import matplotlib.pyplot as plt
import numpy as np

def draw_sector(ax, start_angle, radius, color):
    # Define the angles for the sector
    theta = np.linspace(start_angle, start_angle + 120, 100)

    # Define the x and y coordinates of the sector
    x = [0] + [radius * np.cos(np.radians(angle)) for angle in theta] + [0]
    y = [0] + [radius * np.sin(np.radians(angle)) for angle in theta] + [0]

    # Plot the sector
    ax.fill(x, y, color=color)

    # Set plot limits and aspect ratio
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_aspect('equal')

def draw_circles(r1, r2, lineWidth, colorValues):
    fig, ax = plt.subplots()
    circle_color = 'black'
    shape_colors = [
        ['red', 'green'], ['green', 'blue'], ['blue', 'red'],
        ['red', 'blue'], ['green', 'red'], ['blue', 'green'],
    ]  # Customize the colors as desired
    middleColors = ["Snow", "Cyan", "PaleGreen", "Magenta"]
    shape_start = int((colorValues%16)/6)
    colorIndex = (colorValues%16) % 6
    middleIndex = int(colorValues/16)

    startAngle = 90

    draw_sector(ax, startAngle+shape_start*120,     r1, shape_colors[colorIndex][0])
    draw_sector(ax, startAngle+(shape_start+1)*120, r1, shape_colors[colorIndex][1])
    # yellow for default
    draw_sector(ax, startAngle+(shape_start+2)*120, r1, "yellow")

    # Draw lines between circles   
    angles = [startAngle, startAngle+120, startAngle+240]
    for i, angle in enumerate(angles):
        x = [r1 * np.cos(np.radians(angle)), r2 * np.cos(np.radians(angle))]
        y = [r1 * np.sin(np.radians(angle)), r2 * np.sin(np.radians(angle))]
        ax.plot(x, y, linewidth=lineWidth, color=circle_color)

    # Draw big circle
    big_circle = plt.Circle((0, 0), r1, fill=False, linewidth=lineWidth, edgecolor=circle_color)
    ax.add_artist(big_circle)

    # Draw small circle
    small_circle = plt.Circle((0, 0), r2, fill=True, facecolor=middleColors[middleIndex], linewidth=lineWidth, edgecolor=circle_color)
    ax.add_artist(small_circle)

    # Turn off axis and grid
    ax.axis('off')
    ax.grid(False)

    max_radius = max(r1, r2)
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_aspect('equal')

    # Save plot as PNG image
    plt.savefig(f'image/image_{colorValues}.png', dpi=200, transparent=True)

# Example usage
r1 = 9
r2 = 3
lineWidth = 2
for i in range(16):
    draw_circles(r1, r2, lineWidth, i)

for i in range(16, 32):
    draw_circles(r1, r2, lineWidth, i)

for i in range(32, 48):
    draw_circles(r1, r2, lineWidth, i)

for i in range(48, 64):
    draw_circles(r1, r2, lineWidth, i)
