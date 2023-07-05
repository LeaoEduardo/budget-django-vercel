colors = {
    'primary': 'rgba(15, 157, 88, 1)',       # Green
    'secondary': 'rgba(235, 87, 87, 1)',     # Red
    'accent': 'rgba(0, 123, 255, 1)',        # Blue
    'background': 'rgba(247, 247, 247, 1)',  # Light Gray
    'text': 'rgba(51, 51, 51, 1)'            # Dark Gray
}

def change_alpha(color, alpha=0.2):
    # Extract RGB values from the color string
    rgb_values = color[5:-1].split(',')[:-1]

    # Convert RGB values to integers
    r, g, b = map(int, rgb_values)

    # Return the modified color with the new alpha value
    return f'rgba({r}, {g}, {b}, {alpha})'
