from django.test import TestCase

class ExampleTest(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        """ Example assertion test """
        self.assertEqual(1, 1)
