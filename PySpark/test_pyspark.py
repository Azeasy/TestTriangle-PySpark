import unittest
from pyspark.sql import SparkSession


class TestPySpark(unittest.TestCase):
    def test_get_product_categories(self):
        """
        PySpark test for the get_product_categories function.
        """
        spark = SparkSession.builder \
            .appName("ProductCategories") \
            .getOrCreate()

        products_data = [
            (1, "Laptop"),
            (2, "Smartphone"),
            (3, "Headphones"),
            (4, "Mouse"),
            (5, "Product without category")
        ]
        products_df = spark.createDataFrame(products_data, ["id", "name"])

        categories_data = [
            (1, "Electronics"),
            (2, "Computers"),
            (3, "Accessories"),
            (4, "Mobile"),
            (5, "Category without products")
        ]
        categories_df = spark.createDataFrame(categories_data, ["id", "name"])

        product_category_data = [
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 4),
            (3, 1),
            (3, 3),
            (4, 2),
            (4, 3)
        ]
        product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

        result = get_product_categories(products_df, categories_df, product_category_df)

        print("Product-Category pairs and products without categories:")
        result.show(truncate=False)

        spark.stop()


if __name__ == "__main__":
    unittest.main()
