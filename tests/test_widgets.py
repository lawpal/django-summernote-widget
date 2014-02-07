import unittest

from summernote.widgets import SummernoteWidget


class SummernoteWidgetTests(unittest.TestCase):
    def test(self):
        w = SummernoteWidget()
        self.assertEqual(w.render('foo', ''), '<textarea cols="80" data-toggle="summernote" name="foo" rows="10">\r\n</textarea>')
        self.assertEqual(w.render('foo', 'bar'), '<textarea cols="80" data-toggle="summernote" name="foo" rows="10">\r\nbar</textarea>')

        # You can also pass 'attrs' to the constructor:
        w = SummernoteWidget(attrs={'cols': '20'})
        self.assertEqual(w.render('foo', ''), '<textarea cols="20" data-toggle="summernote" name="foo" rows="10">\r\n</textarea>')
        self.assertEqual(w.render('foo', 'bar'), '<textarea cols="20" data-toggle="summernote" name="foo" rows="10">\r\nbar</textarea>')
