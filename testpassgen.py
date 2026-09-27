import unittest
from passgen import make_password, check_strength

class TestPasswordTool(unittest.TestCase):

    def test_length(self):
        # test if generator makes the requested length
        pwd = make_password(14)
        self.assertEqual(len(pwd), 14)

    def test_weak_password(self):
        # short and simple password should be weak
        self.assertEqual(check_strength("abc"), "Weak")

    def test_strong_password(self):
        # password with upper, digits, symbols and length >= 10
        self.assertEqual(check_strength("MyPass123!@#"), "Strong")

if __name__ == "__main__":
    unittest.main()