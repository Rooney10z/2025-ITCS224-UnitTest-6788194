import unittest
from age import categorize_by_age

class TestAgeCategories(unittest.TestCase):

    def test_child_age(self):
        for age in range(10): 
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print(f"{age} is considered as a child.")

    def test_adolescent_age(self):
        for age in range(10, 18):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adolescent")
                print(f"{age} is considered as an adolescent.")

    def test_adult_age(self):

        for age in range(19, 60): 
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                print(f"{age} is considered as an adult.")

if __name__ == "__main__":
    unittest.main(verbosity=2)