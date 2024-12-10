import random

def generate_svg(filename="output.svg"):
    width, height = 500, 500
    shapes = []
    
    for _ in range(10):
        x, y = random.randint(0, width), random.randint(0, height)
        size = random.randint(10, 100)
        color = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
        shape_type = random.choice(["circle", "rect"])
        if shape_type == "circle":
            shapes.append(f'<circle cx="{x}" cy="{y}" r="{size // 2}" fill="{color}" />')
        elif shape_type == "rect":
            shapes.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}" />')

    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content += "\n".join(shapes)
    svg_content += "\n</svg>"

    with open(filename, "w") as f:
        f.write(svg_content)

if __name__ == "__main__":
    generate_svg()
    print("File SVG generato: output.svg")
