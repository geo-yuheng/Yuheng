Documentation
=============

This directory contains the documentation for the Yuheng project.

Building the Documentation
-------------------------

To build the documentation, you need to have Sphinx and other dependencies installed.
You can install them by running:

.. code-block:: bash

    python init.py

Or manually install the required packages:

.. code-block:: bash

    pip install sphinx furo sphinx-autodoc-typehints sphinx-copybutton

Then, you can build the documentation by running:

.. code-block:: bash

    make html

The built documentation will be available in the ``_build/html`` directory.
You can open the ``index.html`` file in your browser to view it.

Documentation Structure
----------------------

- ``conf.py``: Sphinx configuration file
- ``index.rst``: Main documentation page
- ``Guidebook/``: User guides and tutorials
- ``Manual/``: API reference and manual
- ``Dev/``: Development documentation