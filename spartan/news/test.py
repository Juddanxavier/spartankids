from django.test import TestCase

from .models import News


class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(title="this is title")
        News.objects.create(title="this is title")

    def test_check_slugs(self):
        object_1 = News.objects.get(pk=1)
        object_2 = News.objects.get(pk=2)

        self.assertEqual(object_1.slug, 'this-is-title')
        self.assertEqual(object_2.slug, 'this-is-title-2')
