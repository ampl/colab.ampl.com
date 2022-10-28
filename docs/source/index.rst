
AMPL Model Colaboratory
=======================

Introduction
------------

AMPL Model Colaboratory is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as Google Colab, Kaggle, Gradient, and AWS SageMaker.

In order to be use AMPL on these platforms you just need to following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   !pip install -q amplpy


.. code-block:: python

   # Google Colab & Kaggle integration
   MODULES=['ampl', 'coin', 'highs', 'gokestrel']
   from amplpy import tools
   ampl = tools.ampl_notebook(modules=MODULES, globals_=globals()) # instantiate AMPL object and register magics


In the list ``MODULES`` you can specify the AMPL solvers you want to use in your notebook.
As a quick-start you can use our template notebook: :ref:`tag-template`.
You can contribute to this repository by making pull requests to https://github.com/ampl/amplcolab and following the instructions in the  `README <https://github.com/ampl/amplcolab/blob/master/README.md>`_ file.

.. note::

    In these notebooks there are ``%%ampl_eval`` cells that allow you to run AMPL code directly from the notebook. 
    They are equivalent to ``ampl.eval("""cell content""")``.

.. warning::
    Some notebooks require a license to run due to the problem size. You can use a free `AMPL Community
    Edition <https://ampl.com/ce/>`_ license with an open-source solver (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with a commercial solver from the `NEOS Server <http://www.neos-server.org/>`_ as described in <https://dev.ampl.com/solvers/kestrel.html>.
    In the list ``MODULES`` you need to include 
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver; 
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver; 
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers without NEOS, you need to use a cloud license that includes the commercial solver.
 

Main categories
---------------

.. toctree::
    :maxdepth: 1

    tags/ampl-lecture
    tags/finance
    tags/industry
    tags/military
    tags/google-sheets

Authors
-------

The notebooks in this repository are contributed by the following authors:

.. toctree::
    :maxdepth: 2

    authors/index

**Your name can be here too!** Just make a pull request to https://github.com/ampl/amplcolab.

Notebooks
---------


AMPL Model Colaboratory Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Basic notebook template for the AMPL Colab repository

Tags: :ref:`tag-ampl-only`, :ref:`tag-template`, :ref:`tag-industry`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/template/colab.ipynb
    :alt: colab.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/template/colab.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/template/colab.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/template/colab.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/template/colab.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: Economic equilibria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: economic model using complementarity conditions from Chapter 19 AMPL book

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-finance`, :ref:`tag-complementarity_problem`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: economic_eq_lecture.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: Transshipment problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: book example with general transshipment model (net1.mod)

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/net1.ipynb
    :alt: net1.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/net1.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/net1.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/net1.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/net1.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: diet
^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using diet.mod, diet.dat, and diet.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/diet.ipynb
    :alt: diet.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/diet.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/diet.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/diet.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/diet.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: prod
^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using prod.mod, prod.dat, and prod.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`

Author: N/A

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/prod.ipynb
    :alt: prod.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/prod.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/prod.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/prod.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/prod.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: steel
^^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using steel.mod, steel.dat, and steel.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`

Author: N/A

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/steel.ipynb
    :alt: steel.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/steel.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/steel.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/steel.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/steel.ipynb
    :alt: Open In SageMaker Studio Lab
    

Book Example: transp
^^^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using transp.mod, transp.dat, and transp.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`

Author: N/A

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/transp.ipynb
    :alt: transp.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/transp.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/transp.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/transp.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/transp.ipynb
    :alt: Open In SageMaker Studio Lab
    

CP-style scheduling model with the *numberof* operator, solved by a MIP solver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Scheduling model with the Constraint Programming *numberof* operator, solved with a MIP solver. New MIP solver drivers based on the [MP library](https://amplmp.readthedocs.io/) enable CP-style modeling.

Tags: :ref:`tag-ampl-only`, :ref:`tag-constraint-programming`

Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/sched_numberof.ipynb
    :alt: sched_numberof.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/sched_numberof.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/sched_numberof.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/sched_numberof.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/sched_numberof.ipynb
    :alt: Open In SageMaker Studio Lab
    

Capacity expansion of power generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Models the extensive form of a deterministic multi-stage capacity expansion problem. In this model we can have multiple resources of the same type which have identical properties. The model can be further developed into a stochastic one.

Tags: :ref:`tag-ampl-only`, :ref:`tag-planning`, :ref:`tag-mip`, :ref:`tag-power-generation`

Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/capacity_expansion.ipynb
    :alt: capacity_expansion.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/capacity_expansion.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/capacity_expansion.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/capacity_expansion.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/capacity_expansion.ipynb
    :alt: Open In SageMaker Studio Lab
    

Diet lecture
^^^^^^^^^^^^
Description: Diet case study

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: diet_case_study.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In SageMaker Studio Lab
    

Diet model with Google Sheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Diet model using Google Sheets

Tags: :ref:`tag-amplpy`, :ref:`tag-google-sheets`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/gspread.ipynb
    :alt: gspread.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/gspread.ipynb
    :alt: Open In Colab
    

Efficient Frontier with Google Sheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Efficient Frontier example using Google Sheets

Tags: :ref:`tag-amplpy`, :ref:`tag-google-sheets`, :ref:`tag-example`

Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/finance/efficient_frontier.ipynb
    :alt: efficient_frontier.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/finance/efficient_frontier.ipynb
    :alt: Open In Colab
    

Financial Portfolio Optimization with amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Financial Portfolio Optimization with amplpy and amplpyfinance

Tags: :ref:`tag-amplpy`, :ref:`tag-amplpyfinance`, :ref:`tag-finance`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/finance/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: amplpyfinance_vs_amplpy.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/finance/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/finance/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/finance/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/finance/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In SageMaker Studio Lab
    

Google Hashcode 2022
^^^^^^^^^^^^^^^^^^^^
Description: Google Hashcode 2022 Practice Problem

Tags: :ref:`tag-amplpy`, :ref:`tag-heuristics`, :ref:`tag-engineering`, :ref:`tag-scheduling`, :ref:`tag-complexity`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/hashcode/practice_problem.ipynb
    :alt: practice_problem.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/hashcode/practice_problem.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/hashcode/practice_problem.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/hashcode/practice_problem.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/hashcode/practice_problem.ipynb
    :alt: Open In SageMaker Studio Lab
    

Hospitals-Residents MIP
^^^^^^^^^^^^^^^^^^^^^^^
Description: hospitals-residents problem with ties problem solved with ampl and highs

Tags: :ref:`tag-ampl-api`, :ref:`tag-assignment`, :ref:`tag-mip`, :ref:`tag-data-structures`, :ref:`tag-graphs`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/hospitals_residents.ipynb
    :alt: hospitals_residents.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/hospitals_residents.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/hospitals_residents.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/hospitals_residents.ipynb
    :alt: Open In SageMaker Studio Lab
    

Jupyter Notebook Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Jupyter Notebook Integration with amplpy

Tags: :ref:`tag-amplpy`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/magics.ipynb
    :alt: magics.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/magics.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/magics.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/magics.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/magics.ipynb
    :alt: Open In SageMaker Studio Lab
    

Multicommodity transportation problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Multicommodity transportation model with binary variables

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-mixed-integer-linear`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/multmip1.ipynb
    :alt: multmip1.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/multmip1.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/multmip1.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In SageMaker Studio Lab
    

Network design with redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Design of an electricity transportation network provides enough redundancy, so that a break of one component does not prevent any user from receiving electricity. The approach also works for similar distribution networks and can potentially be used in the design of military logistic networks.

Tags: :ref:`tag-electric-grid`, :ref:`tag-military`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/military/electric_grid_with_redundancy.ipynb
    :alt: electric_grid_with_redundancy.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/military/electric_grid_with_redundancy.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/military/electric_grid_with_redundancy.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/military/electric_grid_with_redundancy.ipynb
    :alt: Open In SageMaker Studio Lab
    

Nonlinear transportation model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using nltransd.mod, nltrans.dat, and nltrans.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-nonlinear`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: nltrans_lecture.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    

Nonlinear transportation problem example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: book example autogenerated using nltransd.mod, nltrans.dat, and nltrans.run

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-nonlinear`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/nltrans.ipynb
    :alt: nltrans.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/nltrans.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/nltrans.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In SageMaker Studio Lab
    

Optimization Methods in Finance: Chapter 3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Optimization Methods in Finance: Bond Dedication Problem.

Tags: :ref:`tag-amplpy`, :ref:`tag-example`, :ref:`tag-finance`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/finance/finance_opt_example_3_1.ipynb
    :alt: finance_opt_example_3_1.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/finance/finance_opt_example_3_1.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/finance/finance_opt_example_3_1.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/finance/finance_opt_example_3_1.ipynb
    :alt: Open In SageMaker Studio Lab
    

Pattern Enumeration
^^^^^^^^^^^^^^^^^^^
Description: Pattern enumeration example with amplpy

Tags: :ref:`tag-amplpy`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_enumeration.ipynb
    :alt: pattern_enumeration.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_enumeration.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_enumeration.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_enumeration.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/pattern_enumeration.ipynb
    :alt: Open In SageMaker Studio Lab
    

Pattern Generation
^^^^^^^^^^^^^^^^^^
Description: Pattern generation example with amplpy

Tags: :ref:`tag-amplpy`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_generation.ipynb
    :alt: pattern_generation.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_generation.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_generation.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_generation.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/pattern_generation.ipynb
    :alt: Open In SageMaker Studio Lab
    

Production model
^^^^^^^^^^^^^^^^
Description: generic model for production problem

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-industry`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-book/production_model.ipynb
    :alt: production_model.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-book/production_model.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-book/production_model.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-book/production_model.ipynb
    :alt: Open In SageMaker Studio Lab
    

Roll Cutting - Revision 1 & 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Pattern tradeoff example with amplpy

Tags: :ref:`tag-amplpy`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_tradeoff.ipynb
    :alt: pattern_tradeoff.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_tradeoff.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/pattern_tradeoff.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/pattern_tradeoff.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/pattern_tradeoff.ipynb
    :alt: Open In SageMaker Studio Lab
    

Steel industry problem
^^^^^^^^^^^^^^^^^^^^^^
Description: model for steel production problem

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`, :ref:`tag-industry`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: steel_lecture.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    

Transportation problem
^^^^^^^^^^^^^^^^^^^^^^
Description: an AMPL model for the transportation problem

Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`

Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: transp_lecture.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    

Travelling Salesman Problem with subtour elimination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: this example shows how to solve a TSP  by eliminating subtours using amplpy and ampls

Tags: :ref:`tag-callbacks`, :ref:`tag-tsp`

Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/tsp_simple_cuts_generic.ipynb
    :alt: tsp_simple_cuts_generic.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/tsp_simple_cuts_generic.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/tsp_simple_cuts_generic.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/tsp_simple_cuts_generic.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/tsp_simple_cuts_generic.ipynb
    :alt: Open In SageMaker Studio Lab
    

VPSolver: Cutting & Packing Problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Solving cutting & packing problems using arc-flow formulations

Tags: :ref:`tag-industry`, :ref:`tag-cutting-stock`, :ref:`tag-bin-packing`, :ref:`tag-vector-packing`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/vpsolver.ipynb
    :alt: vpsolver.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/vpsolver.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/vpsolver.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/vpsolver.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/vpsolver.ipynb
    :alt: Open In SageMaker Studio Lab
    

amplpy setup & Quick Start
^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: amplpy setup and quick start

Tags: :ref:`tag-amplpy`, :ref:`tag-example`

Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/amplcolab/blob/master/miscellaneous/quickstart.ipynb
    :alt: quickstart.ipynb
    
.. image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/miscellaneous/quickstart.ipynb
    :alt: Open In Colab
    
.. image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/miscellaneous/quickstart.ipynb
    :alt: Kaggle
    
.. image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/miscellaneous/quickstart.ipynb
    :alt: Gradient
    
.. image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/miscellaneous/quickstart.ipynb
    :alt: Open In SageMaker Studio Lab
    


Tag list
--------

.. toctree::
    :maxdepth: 2

    tags/index

