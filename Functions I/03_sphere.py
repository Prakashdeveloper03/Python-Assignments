from math import pi
from typing import Tuple


def sphere(radius: float) -> Tuple[float]:
    return 4 * pi * radius**2, (4 / 3) * (pi * radius**3)


radius = float(input("Radius of sphere: "))
area, volume = sphere(radius)
print(
    f"Surface area of the sphere is {area :.5f}\nVolume of the sphere is {volume :.5f}"
)
