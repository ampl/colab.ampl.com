
Modules
=======

`AMPL and all Solvers are now available as Python Packages. <https://dev.ampl.com/ampl/python/modules.html>`_
This page organizes the notebooks according to the modules used.

.. note::
    On Google Colab there is a default `AMPL Community
    Edition license <https://ampl.com/ce/>`_ that gives you **unlimited access to AMPL
    with open-source solvers** (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with commercial solvers from the `NEOS Server <http://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.
    
    In the list ``modules`` you need to include 
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver; 
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver; 
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers, your license needs to include the commercial solver (e.g., an AMPL CE commercial solver trial).
    
    .. code-block:: bash

        # Install dependencies
        !pip install -q amplpy

    .. code-block:: python

        # Google Colab & Kaggle integration
        from amplpy import AMPL, tools
        ampl = tools.ampl_notebook(
            modules=["coin", "highs", "gokestrel"], # modules to install
            license_uuid="default", # license to use
            g=globals()) # instantiate AMPL object and register magics


.. toctree::
    :maxdepth: 2

    cbc
    coin
    cplex
    gurobi
    highs
    knitro
    open

