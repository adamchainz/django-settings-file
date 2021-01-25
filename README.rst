====================
django-settings-file
====================

.. image:: https://img.shields.io/github/workflow/status/adamchainz/django-settings-file/CI/master?style=for-the-badge
   :target: https://github.com/adamchainz/django-settings-file/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/django-settings-file.svg?style=for-the-badge
   :target: https://pypi.org/project/django-settings-file/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Let Django use settings from an arbitrary Python file instead of an importable module.

As per `James Pic's idea posted on the django-developers mailing list
<https://groups.google.com/forum/#!msg/django-developers/mzkwaGQtpOk/LZkxLUMwBQAJ>`_.

Requirements
------------

Python 3.6 to 3.9 supported.

Django 2.2 to 3.2 supported.

----

**Deploying a Django project?**
**Testing a Django project?**
**Are your tests slow?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Usage
-----

1. Install with ``python -m pip install django-settings-file``.

2. Edit your ``manage.py`` and ``wsgi.py`` to swap out Django's default logic for setting ``DJANGO_SETTINGS_MODULE`` to
   instead do:

   .. code-block:: python

       import django_settings_file
       django_settings_file.setup()

3. Add ``os.environ.setdefault('DJANGO_SETTINGS_FILE', '/path/to/default.py')`` before the ``setup()`` call, unless you
   can be sure ``DJANGO_SETTINGS_FILE`` will always be defined in your environment. You might need to figure out the
   path relative to your ``manage.py`` with some ``os.path`` manipulation.

4. Run it! If ``DJANGO_SETTINGS_MODULE`` is defined, it will raise a ``DjangoSettingsFileError`` with a message about
   how only ``DJANGO_SETTINGS_FILE`` is allowed now. If ``DJANGO_SETTINGS_FILE`` is not defined, it will also fail with
   a ``DjangoSettingsFileError`` with a message about defining it. Otherwise Django should start with the settings!

How it works
------------

``django-settings-file`` imports the contents of the specified file using the import machinery available on your Python
version (different logic for 2 and 3) and copies it contents into its own module, which Django sees as the settings
file defined via the traditional ``DJANGO_SETTINGS_MODULE``. Nothing about Django is really touched, it's just a
hacky module.

Caveats
-------

* If the Python file defined by ``DJANGO_SETTINGS_FILE`` tries to do any imports, the directory the file is in will not
  be on ``PYTHONPATH``, so the author of the settings file might get some surprises.
* Additionally, you might experience other problems from loading a file whilst it's not on ``PYTHONPATH``.
* If you want your settings file to extend another one, it will probably find it easiest to ``import`` the base one
  from a location on ``PYTHONPATH``, otherwise it too will have to do use the same import 'hacks' to load the default
  settings.
* File paths are not portable between operating systems, so you may need logic to support both Unix and Windows at
  once.
* File paths are not portable between ``.py`` and ``.pyc`` files. In most cases this means a ``.pyc`` file will not be
  used for settings since it can't be guaranteed to be there, slightly slowing down import time.
* ``DJANGO_SETTINGS_MODULE`` and ``DJANGO_SETTINGS_FILE`` can't both be used by the same project, since the module is
  required for the file-based logic. You might be able to allow them both with extra logic, pull requests accepted.
* ``¯\_(ツ)_/¯`` - this is kind of unknown territory, this library has not been tested in any real project, just with
  the example project in the test folder.
