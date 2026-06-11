from django.test import TestCase

class SimpleTest(TestCase):
    def test_suma(self):
        self.assertEqual(2 + 2, 4)