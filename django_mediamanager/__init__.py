from django.forms.widgets import Media
site = Media()


def autodiscover():
    """
    Auto-discover INSTALLED_APPS media.py modules.
    """
    # This code is based off django.contrib.admin.__init__
    from django.conf import settings
    from importlib import import_module
    from django.utils.module_loading import module_has_submodule

    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        try:
            import_module('%s.media' % app)
        except:
            if module_has_submodule(mod, 'media'):
                raise
