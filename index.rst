
.. setuptools-odoo slides file, created by
   hieroglyph-quickstart on Sun Sep 18 10:39:57 2016.


===============
setuptools-odoo
===============

A modern Odoo development workflow with pip and virtualenv.

|

|

Stéphane Bidoul <stephane.bidoul@acsone.eu>

.. figure:: /_static/logo.png
   :scale: 50%
   :target: http://acsone.eu/

The Python ecosystem packaging tools
====================================

.. rst-class:: build-item-1

Installation tools

.. rst-class:: build-item-1

- ``pip`` to install Python packages
- ``virtualenv`` to create isolated Python environments

.. rst-class:: build-item-2

Packaging tools

.. rst-class:: build-item-2

- ``setuptools`` to define projects and create distributions
- ``wheel`` the modern Python built distribution format

.. rst-class:: build-item-3

Start reading from `Python Packaging Authority <http://pypa.io/>`_.

virtualenv
==========

.. rst-class:: build-item-1

Create and activate a new virtualenv named ``myproject``:

.. rst-class:: build-item-1

.. code-block:: console

   $ virtualenv myproject
   $ source myproject/bin/active

.. rst-class:: build-item-2

To juggle many projects, use `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_.

.. rst-class:: build-item-2

Create and activate a virtualenv for a new project:

.. rst-class:: build-item-2

.. code-block:: console

   $ mkdir ~/project1
   $ mkvirtualenv project1 -a ~/project1

.. rst-class:: build-item-2

Easily switch project:

.. rst-class:: build-item-2

.. code-block:: console

   $ workon project1
   $ workon project2

Installing python packages
==========================

Install a library **and its dependencies**:

.. code-block:: console

   $ pip install hieroglyph
   Collecting hieroglyph
   Downloading hieroglyph-0.7.1-py2.py3-none-any.whl (1.6MB)
      100% |████████████████████████████████| 1.7MB 3.6MB/s 
   Collecting Sphinx>=1.2 (from hieroglyph)
   Downloading Sphinx-1.4.6-py2.py3-none-any.whl (1.6MB)
      100% |████████████████████████████████| 1.6MB 3.7MB/s 
   [...]
   Successfully installed Jinja2-2.8 MarkupSafe-0.23 Pygments-2.1.3 
   Sphinx-1.4.6 alabaster-0.7.9 babel-2.3.4 docutils-0.12 [...]

Find what is installed:

.. code-block:: console
   
   $ pip list

.. nextslide::
   :increment:

Start working on a python project
=================================

Git clone it.

Install in ``editable`` (aka ``develop``) mode:

.. code-block:: console

   $ pip install -e .  # or python setup.py develop

This installs the latest version of dependencies.

Projects usually provide a known-good set of dependency versions in ``requirements.txt``:

.. code-block:: console

   $ pip install -r requirements.txt
   $ pip install -e .

Working with unrelased libraries
================================

Just pip install them from git.

.. code-block:: console

   $ pip install -e git+https://github.com/nyergler/hieroglyph.git#egg=hieroglyph

If you what to hack your own version, fork it and install it in editable mode:

.. code-block:: console

   $ pip install -e git+ssh://git@github.com/sbidoul/hieroglyph.git#egg=hieroglyph

If you have it cloned locally already

.. code-block:: console

   $ pip install -e ~/projects/hieroglyph#egg=hieroglyph

Freeze
======

Because you `git tag` everything you send to production, don't you?

Create a **repeatable** know-good set of dependencies.

.. code-block:: console
   :emphasize-lines: 6,6

   $ pip freeze > requirements.txt
   $ cat requirements.txt
   alabaster==0.7.9
   Babel==2.3.4
   docutils==0.12
   -e git+https://github.com/nyergler/hieroglyph.git@800323dea#egg=hieroglyph
   Pygments==2.1.3
   Sphinx==1.4.6
   [...]

What about the Odoo ecosystem?
==============================

.. rst-class:: build-item-1

Current state

.. rst-class:: build-item-1

- install Odoo using standard python tools, so far so good
- locate and download addons (on apps.odoo.com, github, etc)
- read their manifest and/or doc to find dependencies 
  (other addons, python dependencies)
- manually install dependencies
- fiddle with ``--addons-path``
- start Odoo and hope for the best
- repeat

.. rst-class:: build-item-2

**It does not need to be so.**

.. rst-class:: build-item-2

After all Odoo addons are just python code.

Now you can do this
===================

Install Odoo 9 latest nightly:

.. code-block:: console

   $ pip install https://nightly.odoo.com/9.0/nightly/src/odoo_9.0c.latest.zip

Install ``mis_builder`` and it's dependencies:

.. code-block:: console
   :emphasize-lines: 1,1

   $ pip install odoo9-addon-mis_builder -f https://wheelhouse.acsone.eu/oca
   Installing collected packages: 
     odoo9-addon-mis-builder,
     odoo9-addon-date-range, odoo9-addon-report-xlsx, 
     xlsxwriter 

Notice two addons (date_range, report_xlsx) from different OCA github repositories,
and one python library (xslxwriter) are automatically installed.

.. nextslide::
   :increment:

Freeze:

.. code-block:: console

   $ pip freeze | grep odoo
   odoo==9.0rc20160918
   odoo9-addon-date-range==9.0.1.0.0.99.dev11
   odoo9-addon-mis-builder==9.0.2.0.1.99.dev2
   odoo9-addon-report-xlsx==9.0.1.0.0.99.dev1

You can work with development branches too:

.. code-block:: console

   $ pip install -e git+https://github.com/acsone/account-financial-reporting\
   > @9.0-imp_mis_builder_style_9e_tbi#\
   > egg=odoo9-addon-mis_builder\&subdirectory=setup/mis_builder

Packaging your own addons
=========================

Create the following directory structure:

.. code::

   setup.py
   odoo_addons/__init__.py
   odoo_addons/youraddon/__manifest__.py
   odoo_addons/youraddon/__init__.py
   odoo_addons/youraddon/models/...

Where ``odoo_addons/__init__.py`` contain:

.. code-block:: python

   __import__('pkg_resources').declare_namespace(__name__)

.. nextslide::
   :increment:

And ``setup.py`` is:

.. code-block:: python
   :emphasize-lines: 4,5

   from setuptools import setup

   setup(
     setup_requires=['setuptools-odoo']
     odoo_addon=True,
   )

The ``odoo_addon`` keyword does the magic by examining the 
addon's ``__manifest__.py``.

.. nextslide::
   :increment:

In this example it is the equivalent of:

.. code-block:: python

   from setuptools import setup

   setup(
      name='odoo9-addon-mis_builder',
      version='...',           # version from manifest
      description='...',       # summary from manifest
      long_description='...',  # description from manifest or README.rst
      url='...',               # url from manifest
      install_requires=['odoo>=9.0a,<9.1a',
                        'odoo9-addon-report_xslx', 'odoo9-addon-date_range'],
      packages=['odoo_addons',
                'odoo_addons.mis_builder', 'odoo_addons.mis_builder.models', ...],
      namespace_packages=['odoo_addons'],
      include_package_data=True,
      license='AGPL-3')

Automatic discovery of installed addons
=======================================

TODO, pending https://github.com/odoo/odoo/pull/13237

Bringing Odoo into the python ecosystem
=======================================

- automatic discovery of dependencies
- automatic discovery of installed addons, no need to maintain --addons-path
- robust install/uninstall
- freeze !
- pythonistas don't need to learn new tools
