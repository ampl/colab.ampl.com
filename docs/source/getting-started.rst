
Getting Started
===============

In order to be use AMPL on the notebook platforms you just need to following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   !pip install -q amplpy


.. code-block:: python

    # Google Colab & Kaggle integration
    from amplpy import AMPL, tools
    ampl = tools.ampl_notebook(
        modules=["coin", "highs", "gokestrel"], # modules to install
        license_uuid="your-license-uuid", # license to use
        g=globals()) # instantiate AMPL object and register magics

In the list ``modules`` you can specify the AMPL solvers you want to use in your notebook.
For more information on the AMPL Modules for Python see `Python Modules Documentation <https://dev.ampl.com/ampl/python/modules.html>`_.
For more information on how to use ``amplpy`` see `Python API Documentation <https://amplpy.readthedocs.io/>`_.

.. grid:: 1 1 2 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::
        :margin: 0
        :padding: 0

        Quick Start using Pandas dataframes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Data can be loaded in various forms, one of which is ``pandas.DataFrame`` objects.

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Open In SageMaker Studio Lab

    .. grid-item-card::
        :margin: 0
        :padding: 0

        Quick Start using lists and dictionaries
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Data can be loaded in various forms, including Python lists and dictionaries.

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Open In SageMaker Studio Lab

.. note::

    In these notebooks there are ``%%ampl_eval`` cells that allow you to run AMPL code directly from the notebook. 
    They are equivalent to ``ampl.eval("""cell content""")``.

Free licenses available
-----------------------

- On **Google Colab** there is a default `AMPL Community Edition license <https://ampl.com/ce/>`_
  that gives you unlimited access to AMPL
  with open-source solvers (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
  or with commercial solvers from the `NEOS Server <http://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.

- `AMPL for Courses <https://ampl.com/licenses-and-pricing/ampl-for-teaching/>`_ is another free license of full-featured AMPL with no limitations on problem size, and a selection of popular commercial and open-source solvers.
  **This license can be used on Google Colab and similar platforms for teaching.**

- To access commercial solvers you can use solver trials associated to your `AMPL Community Edition license <https://ampl.com/ce/>`_.


