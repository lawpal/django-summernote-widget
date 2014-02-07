from django.forms.util import flatatt
from django.forms.widgets import Textarea
from django.utils.encoding import force_text
from django.utils.html import format_html


class SummernoteWidget(Textarea):
    class Meta:
        css = {
            'all': (
                '//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.0.3/css/font-awesome.min.css',
                '//cdnjs.cloudflare.com/ajax/libs/summernote/0.5.0/summernote.css'
            ),
        }
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/summernote/0.5.0/summernote.min.js',
            'summernote/js/jquery.summernote.js'
        )

    def __init__(self, attrs=None):
        default_attrs = {
            'cols': '80',
        }
        if attrs:
            default_attrs.update(attrs)
        super(SummernoteWidget, self).__init__(default_attrs)

    def render(self, name, value, attrs={}):
        attrs['data-toggle'] = 'summernote'
        return super(SummernoteWidget, self).render(name, value, attrs)
