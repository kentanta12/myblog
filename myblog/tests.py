from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class IndexTests(TestCase):
    """インデックスビューのテストクラス."""

    def test_get(self):
        """getで通常のアクセスを行う"""
        response = self.client.get(reverse('myblog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['index'], [])
