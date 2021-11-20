sphinx-xref-example
===================

This example provides an extension called ``mydoc.py`` which registers a custom directive and role.

* ``mydoc``: A role that works like the Sphinx doc_ role. This creates a hyperlink to another RST document.
* ``mytoctree``: A directive that works similar to the Sphinx toctree_ directive. This creates a bullet list of hyperlinks to RST documents

Examples
--------

Custom doc role
~~~~~~~~~~~~~~~

Here's how the official doc_ role works: :doc:`lorem_ipsum`

Here's how my custom ``mydoc`` role works: :mydoc:`lorem_ipsum`

Custom toctree directive
~~~~~~~~~~~~~~~~~~~~~~~~

Here's how the official toctree_ directive works:

.. This will generate warnings about duplicate entries. I'm doing this for the symmetry of the example and laziness

.. toctree::

    lorem_ipsum
    mydoc_reference
    mydoc_source
    this_doc_does_not_exist

Here's how my custom ``mytoctree`` directive works:

.. mytoctree::

    lorem_ipsum
    mydoc_reference
    mydoc_source
    this_doc_does_not_exist

.. this_doc_does_not_exist will generate a warning. This is intentional to show off refwarn

Layout
------

::

    source/               <-- source directory made by sphinx-quickstart
        _ext/             <-- where I put extensions (similar to tutorials)
            mydoc.py      <-- registers mydoc and mytoctree
        index.rst         <-- This page! Uses mydoc and mytoctree
        lorem_ipsum.rst   <-- A page that exists solely to be linked to

.. _doc: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc
.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html?highlight=toctree#directive-toctree