django-humanize − use humanize 3rd-party lib as template filters
================================================================

Django already offers
[django.contrib.humanize](https://docs.djangoproject.com/en/1.8/ref/contrib/humanize/)
but that implementation is lacking some features, like humanization of
durations.

That lib comes to the rescue allowing you to use *template filters*
backed on [the standalone humanize lib](https://pypi.python.org/pypi/humanize).

Install
------

Add `django_humanize` to your *INSTALLED_APPS* setting.

Examples
--------

### Template

    {% load humanizelib %}

    It lasted {{ duration|naturaldelta }}.

### View

    import datetime
    from django.shortcuts import render_

    def summary(request):
        context = {'duration': datetime.timedelta(seconds=1000)}
        return render('template.html', context)

Will render as *"lasted 16 minutes."*.

Template filters
----------------

The following template filters are available :

- naturalday
- naturaltime
- ordinal
- intword
- naturaldelta
- intcomma
- apnumber
- fractional
- naturalsize
- naturaldate

Internationalization
---------------------

Internationalization is supported and matches Django *LANGUAGE_CODE* setting. If
it does not work, maybe, your language code is not supported by the standalone
humanize lib. Think about
[contributing it](https://github.com/jmoiron/humanize/#localization).
