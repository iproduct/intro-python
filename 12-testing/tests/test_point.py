import unittest

from simple.point import Point


class TestPointMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.point = Point(1, 3)

    def tearDown(self) -> None:
        print("tearing down fixture")
        self.point = None

    def test_distance(self):
        self.assertEqual(5, self.point.distance(Point(4, 7)))


if __name__ == "__main__":
    unittest.main()
