History
=======

Pending release
---------------

.. Insert new release notes below this line

* Update Python support to 3.5-3.7, as 3.4 has reached its end of life.
* Converted setuptools metadata to configuration file. This meant removing the
  ``__version__`` attribute from the package. If you want to inspect the
  installed version, use
  ``pkg_resources.get_distribution("apig-wsgi").version``
  (`docs <https://setuptools.readthedocs.io/en/latest/pkg_resources.html#getting-or-creating-distributions>`__).

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
