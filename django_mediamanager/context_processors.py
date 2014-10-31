from django.utils.safestring import mark_safe

import django_mediamanager


def render_scripts():
    return mark_safe("\n".join(django_mediamanager.site.render_js()))


def render_styles():
    return mark_safe("\n".join(django_mediamanager.site.render_css()))


def media_manager_processors(req):
    """
    Media manager context processors
    """
    return {
        "ALL_SCRIPTS": render_scripts,
        "ALL_STYLES": render_styles
    }
