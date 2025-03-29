
Modules
=======

Modules available
-----------------

`AMPL and all Solvers are now available as Python Packages. <https://dev.ampl.com/ampl/python/modules.html>`_
List of modules available:

- Open-source: ``highs``, ``cbc``, ``coin`` (includes: CBC, Couenne, Ipopt, Bonmin), ``open`` (includes all open-source solvers)
- `NEOS Server <https://www.neos-server.org/>`_: ``gokestrel`` (`kestrel client <https://dev.ampl.com/solvers/kestrel.html>`_)
- Commercial solvers: ``baron``, ``conopt``, ``copt``, ``cplex``, ``gurobi``, ``knitro``, ``lgo``, ``lindoglobal``, ``loqo``, ``minos``, ``mosek``, ``octeract``, ``snopt``, ``xpress``
- AMPL Plugins: ``amplgsl`` (`amplgsl docs <https://amplgsl.readthedocs.io/>`_), ``plugins`` (`amplplugins docs <https://amplplugins.readthedocs.io/>`_)

.. note::
    On Google Colab there is a default `AMPL Community
    Edition license <https://ampl.com/ce/>`_ that gives you **unlimited access to AMPL
    with open-source solvers** (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with commercial solvers from the `NEOS Server <https://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.
    
    In the list ``modules`` you need to include 
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver; 
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver; 
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers, your license needs to include the commercial solver (e.g., an AMPL CE commercial solver trial).
    
    .. code-block:: bash

        # Install dependencies
        %pip install -q amplpy==0.15.0b2

    .. code-block:: python

        # Google Colab & Kaggle integration
        from amplpy import AMPL, ampl_notebook

        ampl = ampl_notebook(
            modules=["gurobi", "coin", "highs", "gokestrel"],  # modules to install
            license_uuid="default",  # license to use
        )  # instantiate AMPL object and register magics

Learn more: [`AMPL and Solvers modules <https://dev.ampl.com/ampl/python/modules.html>`_] [`Solver docs <https://dev.ampl.com/solvers/index.html>`_]

Notebooks grouped by modules
----------------------------

.. toctree::
    :maxdepth: 2

    cbc
    coin
    copt
    cplex
    gcg
    gurobi
    highs
    knitro
    mosek
    open
    plugins
    scip
    xpress

