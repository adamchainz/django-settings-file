=======
History
=======

2.10.1 (2022-12-07)
-------------------

* Mark as unmaintained.

2.10.0 (2022-06-05)
-------------------

* Support Python 3.11.

* Support Django 4.1.

2.9.0 (2022-05-10)
------------------

* Drop support for Django 2.2, 3.0, and 3.1.

2.8.0 (2022-01-10)
------------------

* Drop Python 3.6 support.

2.7.0 (2021-10-05)
------------------

* Support Python 3.10.

2.6.0 (2021-09-28)
------------------

* Support Django 4.0.

2.5.0 (2021-08-14)
------------------

* Add type hints.

2.4.1 (2021-07-05)
------------------

* Stop distributing tests to reduce package size. Tests are not intended to be
  run outside of the tox setup in the repository. Repackagers can use GitHub's
  tarballs per tag.

2.4.0 (2021-01-25)
------------------

* Support Django 3.2.

2.3.0 (2020-12-13)
------------------

* Drop Python 3.5 support.
* Support Python 3.9.
* Drop Django 2.0 and 2.1 support.

2.2.0 (2020-06-15)
------------------

* Add Django 3.1 support.
* Drop Django 1.11 support. Only Django 2.0+ is supported now.

2.1.0 (2019-12-19)
------------------

* Update Python support to 3.5-3.8, as 3.4 has reached its end of life.
* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``importlib.metadata.version("django-settings-file")``
  (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ /
  `backport <https://pypi.org/project/importlib-metadata/>`__).
* Tested with Django 3.0. No changes were required for compatibility.

2.0.1 (2019-04-28)
------------------

* Tested with Django 2.2. No changes were required for compatibility.

2.0.0 (2019-02-02)
------------------

* Drop Python 2 support, only Python 3.4+ is supported now.
* Drop Django 1.8, 1.9, and 1.10 support. Only Django 1.11+ is supported now.

1.0.0 (2017-04-14)
------------------

* First version, supporting ``DJANGO_SETTINGS_FILE`` instead of
  ``DJANGO_SETTINGS_MODULE``
