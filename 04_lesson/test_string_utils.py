import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    # Тесты для метода capitalize
    def test_capitalize_positive(self):
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitalize("test"), "Test")
        self.assertEqual(self.utils.capitalize("123abc"), "123abc")
        self.assertEqual(self.utils.capitalize(""), "")
        self.assertEqual(self.utils.capitalize("hello world"), "Hello world")
        self.assertEqual(self.utils.capitalize("HELLO"), "HELLO")

    def test_capitalize_negative(self):
        with self.assertRaises(TypeError):
            self.utils.capitalize(123)
        with self.assertRaises(TypeError):
            self.utils.capitalize(None)
        with self.assertRaises(TypeError):
            self.utils.capitalize(["list"])
        with self.assertRaises(TypeError):
            self.utils.capitalize(True)

    # Тесты для метода trim
    def test_trim_positive(self):
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("\t\t\ttest"), "test")
        self.assertEqual(self.utils.trim("\n\n\n123abc"), "123abc")
        self.assertEqual(self.utils.trim(" "), "")
        self.assertEqual(self.utils.trim(""), "")
        self.assertEqual(self.utils.trim("   test   "), "test   ")

    def test_trim_negative(self):
        with self.assertRaises(TypeError):
            self.utils.trim(123)
        with self.assertRaises(TypeError):
            self.utils.trim(None)
        with self.assertRaises(TypeError):
            self.utils.trim(["list"])
        with self.assertRaises(TypeError):
            self.utils.trim(True)

    # Тесты для метода contains
    def test_contains_positive(self):
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertTrue(self.utils.contains("SkyPro", "k"))
        self.assertTrue(self.utils.contains("SkyPro", "Pro"))
        self.assertTrue(self.utils.contains("123abc", "3"))
        self.assertTrue(self.utils.contains("123abc", "abc"))
        self.assertTrue(self.utils.contains("hello world", "world"))
        self.assertTrue(self.utils.contains("hello world", " "))

    def test_contains_negative(self):
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertFalse(self.utils.contains("SkyPro", "xyz"))
        self.assertFalse(self.utils.contains("123abc", "4"))
        self.assertFalse(self.utils.contains("123abc", "def"))
        self.assertFalse(self.utils.contains("hello world", "x"))
        with self.assertRaises(TypeError):
            self.utils.contains(123, "a")
        with self.assertRaises(TypeError):
            self.utils.contains("string", 123)
        with self.assertRaises(TypeError):
            self.utils.contains(None, "a")
        with self.assertRaises(TypeError):
            self.utils.contains("string", None)
        with self.assertRaises(TypeError):
            self.utils.contains("string", ["list"])

    # Тесты для метода delete_symbol
    def test_delete_symbol_positive(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")
        self.assertEqual(self.utils.delete_symbol("123abc", "3"), "12abc")
        self.assertEqual(self.utils.delete_symbol("123abc", "abc"), "123")
        self.assertEqual(self.utils.delete_symbol("test", ""), "")