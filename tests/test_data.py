

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
                Page(
                    'Page 1',
                    children=[
                        Page('Subpage 1')
                    ]
                ),
                Page('Page 2')
            ]
        )
        result = parent.flatten()
        print(result.to_hierarchy())
        self.assertEqual(result.pages[0].name, 'Page 1')
        self.assertEqual(result.pages[0].pages[0].name, 'Introduction')
        self.assertEqual(result.pages[0].pages[1].name, 'Subpage 1')
        self.assertEqual(result.pages[1].name, 'Page 2')

