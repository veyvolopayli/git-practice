import unittest
# Импортируем функции из наших файлов
from person1 import file1
from person1 import file2
from person1 import file3


class TestApp(unittest.TestCase):

    def test_file1_greeting(self):
        """Проверяет приветствие из file1.py"""
        self.assertEqual(file1.get_greeting(), "Hello from file1")

    def test_file2_greeting(self):
        """Проверяет приветствие из file2.py"""
        self.assertEqual(file2.get_greeting(), "Hello from file2")

    def test_file3_greeting(self):
        """Проверяет приветствие из file3.py"""
        self.assertEqual(file3.get_greeting(), "Hello from file3")


if __name__ == '__main__':
    unittest.main()
