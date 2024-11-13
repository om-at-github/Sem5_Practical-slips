## cd slip6

## python package_area_and_volume.py

## Write python script using package to calculate area and volume of cube and sphere


import math

def calculate_cube_properties(side_length):
    """Calculate the surface area and volume of a cube."""
    area = 6 * (side_length ** 2)
    volume = side_length ** 3
    return area, volume

def calculate_sphere_properties(radius):
    """Calculate the surface area and volume of a sphere."""
    area = 4 * math.pi * (radius ** 2)
    volume = (4/3) * math.pi * (radius ** 3)
    return area, volume

if __name__ == "__main__":
    # Input for cube
    side_length = float(input("Enter the side length of the cube: "))
    cube_area, cube_volume = calculate_cube_properties(side_length)
    print(f"Cube Surface Area: {cube_area:.2f}")
    print(f"Cube Volume: {cube_volume:.2f}")

    # Input for sphere
    radius = float(input("Enter the radius of the sphere: "))
    sphere_area, sphere_volume = calculate_sphere_properties(radius)
    print(f"Sphere Surface Area: {sphere_area:.2f}")
    print(f"Sphere Volume: {sphere_volume:.2f}")
