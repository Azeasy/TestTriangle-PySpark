import unittest
import math
from shapes import Circle, Triangle, create_shape


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected_area)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_triangle_area(self):
        # Right triangle
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

        # Not a right triangle
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())

    def test_invalid_triangle(self):
        # Negative side
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)

        # Triangle inequality
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_factory_function(self):
        # Create a circle
        circle = create_shape('circle', radius=5)
        self.assertIsInstance(circle, Circle)
        self.assertEqual(circle.radius, 5)

        # Create a triangle
        triangle = create_shape('triangle', a=3, b=4, c=5)
        self.assertIsInstance(triangle, Triangle)
        self.assertTrue(triangle.is_right())


if __name__ == '__main__':
    unittest.main()
