

from unittest import TestCase

from data.agnostic import Category, Page


class FlatteningTests(TestCase):

    def test_flat(self):
        parent = Category(
            '',
            'parent',
            pages=[
                Page('Page 1'),
                Page('Page 2'),
                Page('Page 3')
            ]
        )
        result = parent.flatten()
        self.assertEqual(result.pages, parent.pages)

    def test_one_depth(self):
        parent = Category(
            '',
            'parent',
            pages=[
                Page('Page 1'),
                Page('Page 2'),
                Page('Page 3')
            ]
        )
