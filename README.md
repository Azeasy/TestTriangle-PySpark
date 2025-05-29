# Geometric Shapes & PySpark

A simple Python module for calculating areas of geometric shapes:

`path=./geometric_shapes`

A simple PySpark module for DataFrame data manipulation

`path=./PySpark`

## Geometric Shapes

```python
from geometric_shapes.shapes import Circle, Triangle, create_shape

# Create a circle and calculate its area
circle = Circle(radius=5)
print(f"Circle area: {circle.area()}")

# Create a triangle and calculate its area
triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area()}")
print(f"Is right triangle: {triangle.is_right()}")

# Create a shape without knowing its type at compile-time
shape = create_shape("circle", radius=5)
print(f"Shape area: {shape.area()}")
```

## Extending with New Shapes

You can easily extend the library by creating new classes that inherit from the `Shape` base class:

```python
from geometric_shapes.shapes import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

# Create a rectangle and calculate its area
rectangle = Rectangle(width=4, height=5)
print(f"Rectangle area: {rectangle.area()}")
```

## Running Tests

```bash
python3 geometric_shapes/test_shapes.py
```

####

## PySpark

## Running Tests

```bash
pip install pyspark
```

```bash
python3 PySpark/test_pyspark.py
```
Input Data in tests:
```
Products:
+---+------------------------+
|id |name                    |
+---+------------------------+
|1  |Laptop                  |
|2  |Smartphone              |
|3  |Headphones              |
|4  |Mouse                   |
|5  |Product without category|
+---+------------------------+

Categories:
+---+-------------------------+
|id |name                     |
+---+-------------------------+
|1  |Electronics              |
|2  |Computers                |
|3  |Accessories              |
|4  |Mobile                   |
|5  |Category without products|
+---+-------------------------+

Product-Category Mappings:
+----------+-----------+
|product_id|category_id|
+----------+-----------+
|1         |1          |
|1         |2          |
|2         |1          |
|2         |4          |
|3         |1          |
|3         |3          |
|4         |2          |
|4         |3          |
+----------+-----------+
```
Output in the console should be:
```
Product-Category pairs and products without categories:
+------------------------+-------------+
|product_name            |category_name|
+------------------------+-------------+
|Laptop                  |Computers    |
|Laptop                  |Electronics  |
|Smartphone              |Mobile       |
|Smartphone              |Electronics  |
|Product without category|NULL         |
|Headphones              |Accessories  |
|Headphones              |Electronics  |
|Mouse                   |Accessories  |
|Mouse                   |Computers    |
+------------------------+-------------+

```