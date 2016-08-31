from django.test import TestCase

class Smoketest(TestCase):

    def test_bad_maths(self):
        self.assertEquals(1 + 1, 3)
