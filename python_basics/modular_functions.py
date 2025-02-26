import math

def calculate_area(shape, dimension1, dimension2=0):
    """Calculates the area of a given shape."""
    if shape == "circle":
        return math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Testing the function with different shapes
shapes = [
    ("circle", 5),
    ("rectangle", 10, 20),
    ("triangle", 8, 12),
    ("circle", 7),
    ("rectangle", 15, 30),
    ("triangle", 6, 10)
]

for shape_data in shapes:
    shape = shape_data[0]
    dimension1 = shape_data[1]
    dimension2 = shape_data[2] if len(shape_data) > 2 else 0
    area = calculate_area(shape, dimension1, dimension2)
    print(f"The area of the {shape} is: {area}")
