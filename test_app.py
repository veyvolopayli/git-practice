import unittest
from person1 import file1
from person1 import file2
from person1 import file3
from person1 import new_dev_file


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

    def test_new_dev_file_message(self):
        """Проверяет сообщение из новой функции"""
        self.assertEqual(new_dev_file.get_feature_message(), "This is an important new feature")


if __name__ == '__main__':
    unittest.main()
