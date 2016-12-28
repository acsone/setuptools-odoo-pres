
.. setuptools-odoo slides file, created by
   hieroglyph-quickstart on Sun Sep 18 10:39:57 2016.

.. |acsone_logo| image:: _static/logo.png
   :height: 100px
   :target: http://acsone.eu/

.. |oca_logo| image:: _static/oca.png
   :height: 100px
   :target: http://odoo-community.org/

.. |nbsp| unicode:: 0xa0

=================================================
Odoo development workflow with pip and virtualenv
=================================================

|acsone_logo| |nbsp| |nbsp| |nbsp| |nbsp| |nbsp| |oca_logo|

|

Version 1.2.1

Stéphane Bidoul <stephane.bidoul@acsone.eu>


Python ecosystem packaging tools
================================

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

Create and activate a new virtualenv named ``myproject``:

.. code-block:: console

   $ virtualenv myproject
   $ source myproject/bin/activate

Upgrade to a recent pip version in your activated virtualenv:

.. code-block:: console

   $ pip install -U "pip>=9.0.1"

.. nextslide::
   :increment:

To juggle many projects, use `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_.

Create and activate a virtualenv for a new project:

.. code-block:: console

   $ mkdir ~/project1
   $ mkvirtualenv project1 -a ~/project1
   $ pip install -U "pip>=9.0.1"

Easily switch project:

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

If you want to hack your own version, fork it and install it in editable mode:

.. code-block:: console

   $ pip install -e git+ssh://git@github.com/sbidoul/hieroglyph.git#egg=hieroglyph

If you have it cloned locally already

.. code-block:: console

   $ pip install -e ~/projects/hieroglyph

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

**It does not need to be so difficult.**

.. rst-class:: build-item-2

After all Odoo addons are just python code.

With setuptools-odoo, you can now do this [9.0]
===============================================

Install Odoo 9 latest nightly:

.. code-block:: console

   $ pip install https://nightly.odoo.com/9.0/nightly/src/odoo_9.0.latest.zip

Install ``mis_builder`` and it's dependencies:

.. code-block:: console
   :emphasize-lines: 1,1

   $ pip install odoo9-addon-mis_builder -f https://wheelhouse.odoo-community.org/oca
   Installing collected packages: 
     odoo9-addon-mis-builder,
     odoo9-addon-date-range, odoo9-addon-report-xlsx, 
     xlsxwriter 

Notice the installation of two dependent addons (date_range, report_xlsx) 
from different OCA github repositories, and one python library (xslxwriter).

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

With setuptools-odoo, you can now do this [10.0]
================================================

Install Odoo 10 latest nightly:

.. code-block:: console

   $ pip install https://nightly.odoo.com/10.0/nightly/src/odoo_10.0.latest.zip

Install ``account_fiscal_year`` and it's dependencies:

.. code-block:: console
   :emphasize-lines: 1,1

   $ pip install odoo10-addon-account_fiscal_year -f https://wheelhouse.odoo-community.org/oca
   Installing collected packages: 
     odoo10-addon-date-range

Notice the installation of one dependent addons (date_range) 
from different OCA github repositories.

.. nextslide::
   :increment:

Freeze:

.. code-block:: console

   $ pip freeze | grep odoo
   odoo==10.0.post20161011
   odoo10-addon-account-fiscal-year==10.0.1.0.0
   odoo10-addon-date-range==10.0.1.0.0

You can work with development branches too:

.. code-block:: console

   $ pip install -e git+https://github.com/acsone/account-invoicing\
   > @10-mig-account_invoice_supplier_ref_unique-ape#\
   > egg=odoo10-addon-account_invoice_supplier_ref_unique\
   > \&subdirectory=setup/account_invoice_supplier_ref_unique

Packaging your own addons [9.0]
===============================

Create the following directory structure:

.. code::

   setup.py
   odoo_addons/__init__.py
   odoo_addons/youraddon/__openerp__.py
   odoo_addons/youraddon/__init__.py
   odoo_addons/youraddon/models/...

Where ``odoo_addons/__init__.py`` contains:

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
addon's ``__openerp__.py``.

.. nextslide::
   :increment:

In this example it is the equivalent of:

.. code-block:: python

   from setuptools import setup

   setup(
      name='odoo9-addon-youraddon',
      version='...',           # version from manifest
      description='...',       # summary from manifest
      long_description='...',  # description from manifest or README.rst
      url='...',               # url from manifest
      install_requires=['odoo>=9.0a,<9.1a',
                        'odoo9-addon-dependency1', 'odoo9-addon-dependency2',
                        'some_python_dependency'],
      packages=['odoo_addons',
                'odoo_addons.youraddon', 'odoo_addons.youraddon.models', ...],
      namespace_packages=['odoo_addons'],
      include_package_data=True,
      license='AGPL-3')

Packaging your own addons [10.0]
================================

Create the following directory structure:

.. code::

   setup.py
   odoo/__init__.py
   odoo/addons/__init__.py
   odoo/addons/youraddon/__manifest__.py
   odoo/addons/youraddon/__init__.py
   odoo/addons/youraddon/models/...

Where ``odoo/__init__.py`` and ``odoo/addons/__init__.py`` contains:

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
      name='odoo10-addon-youraddon',
      version='...',           # version from manifest
      description='...',       # summary from manifest
      long_description='...',  # description from manifest or README.rst
      url='...',               # url from manifest
      install_requires=['odoo>=10.0,<10.1dev',
                        'odoo10-addon-dependency1', 'odoo10-addon-dependency2',
                        'some_python_dependency'],
      packages=['odoo', 'odoo.addons',
                'odoo.addons.youraddon', 'odoo_addons.youraddon.models', ...],
      namespace_packages=['odoo', 'odoo.addons'],
      include_package_data=True,
      license='AGPL-3')

Automatic discovery of installed addons
=======================================

In Odoo 8 and 9, addons installed this way can be
discovered automatically using 
`odoo-autodiscover <https://pypi.python.org/pypi/odoo-autodiscover>`_.

In Odoo 10, autodiscovery of installed addons is a
built-in feature, so starting ``odoo`` is enough for it
to extend the addons-path automatically..

The main difference between 8/9 and 10 is that in the
namespace package for addons is ``odoo.addons`` (directory ``odoo/addons``)
instead of ``odoo_addons`` (in 8 and 9).

Bringing Odoo into the python ecosystem
=======================================

- automatic discovery of dependencies
- automatic discovery of installed addons, no need to maintain --addons-path
- robust install/uninstall
- freeze !
- pythonistas don't need to learn new tools

.. rst-class:: content-auto-fadein

Q&A
===

|

|

|

|

.. rst-class:: centered large-text

Thank You

|

|

.. rst-class:: centered

| @sbidoul
| stephane.bidoul@acsone.eu
| https://acsone.eu/
| https://wheelhouse.odoo-community.org/
