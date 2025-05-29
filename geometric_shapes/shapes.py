import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape with radius.
    """
    def __init__(self, radius):
        """
        Initialize a circle with given radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            ValueError: If radius is not positive.
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """
    Triangle shape with three sides.
    """
    def __init__(self, a: float, b: float, c: float):
        """
        Initialize a triangle with three sides.

        Args:
            a (float): Length of the first side.
            b (float): Length of the second side.
            c (float): Length of the third side.

        Raises:
            ValueError: If any side is not positive or
            triangle inequality does not hold.
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive")

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides cannot form a triangle")

        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """
        Check if the triangle is a right triangle
        using the Pythagorean theorem.

        Returns:
            bool: True if the triangle is a right triangle, False otherwise.
        """
        # Sort the sides to make comparison easier
        sides = sorted([self.a, self.b, self.c])
        return sides[0]**2 + sides[1]**2 == sides[2]**2


def create_shape(shape_type: str, **kwargs) -> Shape:
    shape_type = shape_type.lower()

    if shape_type == 'circle':
        return Circle(radius=kwargs['radius'])
    elif shape_type == 'triangle':
        return Triangle(a=kwargs['a'], b=kwargs['b'], c=kwargs['c'])
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")
