django-mediamanager
============

A central repository for registering scripts and styles for your applications.  This is similar to how the Django form media works,
except that instead of including the media in each form, they are expected to be included in some base template so they are available on every page.

This is useful when dealing with single page web apps that use client side MVC frameworks like Backbone.js and you have multiple Django apps that are providing their own media.

## Installing

Install from pip
```
sudo pip install django_mediamanager
```

Add the content processor

```python
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django_mediamanager.context_processors.media_manager_processors',
)
```

Autodiscover any media within your applications.  Add this to your main urls.py
```python
import django_mediamanager
django_mediamanager.autodiscover()
```

## Adding media
Your Django applications can provide a media.py file that registers all their media.  The media files are expected to be in a "static" directory within your application

Example media.py
```python
import django_mediamanager

django_mediamanager.site.add_js((
    "js/bootstrap.min.js",
    "js/mycooljavascript.js",
))

django_mediamanager.site.add_css({
    "all": (
        "css/bootstrap.css",
        "css/prettystyles.css",
    )
})
```

## Including media in your templates
You can use the media manager's context processors to include all the registered media in your templates.  For example:

```html
<html>
    <head>
        {{ALL_STYLES}}
    </head>

    <body>
        {{ALL_SCRIPTS}}
    </body>
</html>
```