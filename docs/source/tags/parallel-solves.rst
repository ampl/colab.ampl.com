.. _tag-parallel-solves:

parallel-solves
===============

AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition <../notebooks/ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition.html>`_
| |github-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |colab-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |kaggle-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |gradient-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |sagemaker-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition|
| Description: In the fifth installment of our six-part series, we delve deeper by showing how to evolve our Benders decomposition Python script from a serial execution to one that solves subproblems in parallel.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`, :ref:`tag-parallel-solves`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: 5_benders_parallel_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


