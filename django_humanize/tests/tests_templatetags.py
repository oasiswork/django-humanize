from datetime import datetime, timedelta
import imp

from django.test import TestCase
from django.test.utils import override_settings
from django.template import Template, Context

now = datetime.now()
one_hour = timedelta(hours=1)
one_day = timedelta(days=1)
some_day = datetime(1982, 6, 27)
import django_humanize.templatetags.humanizelib

@override_settings(LANGUAGE_CODE='en-us')
class TestHumanize(TestCase):

    def mk_tpl(self, filtr):
        return Template(
            """{{% load humanizelib %}}
            {{{{ var|{} }}}}
            """.format(filtr)
        )

    def test_filters(self):
        django_humanize.templatetags.humanizelib.init()

        cases = [
            ('ordinal', 1, '1st'),
            ('intword', 1000000, '1.0 million'),
            ('intcomma', 1000, '1,000'),
            ('apnumber', 1, 'one'),
            ('fractional', (4.0/3.0), '1 1/3'),
            ('naturaldelta', timedelta(seconds=1000), '16 minutes'),
            ('naturalday',  now, 'today'),
            ('naturaltime', now, 'now'),
            ('naturaldate', some_day, 'Jun 27 1982'),
            ('naturalsize', 300, '300 Bytes'),
        ]

        for filtr, _in, out in cases:
            tpl = self.mk_tpl(filtr)
            context = Context({'var': _in})

            self.assertEqual(
                tpl.render(context).strip(),
                out
            )

    @override_settings(LANGUAGE_CODE='fr-fr')
    def test_localized_filter(self):
        django_humanize.templatetags.humanizelib.init()
        tpl = self.mk_tpl('apnumber')
        context = Context({'var': 1})
        self.assertEqual(tpl.render(context).strip(), 'un')
