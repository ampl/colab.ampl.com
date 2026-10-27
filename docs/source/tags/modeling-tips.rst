.. _tag-modeling-tips:

modeling-tips
=============

Big-M constants come from declared bounds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Big-M constants come from declared bounds <../notebooks/big-m-constants-come-from-declared-bounds.html>`_
| |github-big-m-constants-come-from-declared-bounds| |colab-big-m-constants-come-from-declared-bounds| |deepnote-big-m-constants-come-from-declared-bounds| |kaggle-big-m-constants-come-from-declared-bounds| |gradient-big-m-constants-come-from-declared-bounds| |sagemaker-big-m-constants-come-from-declared-bounds|
| Description: How MP sizes the big-M constants of logical constraints from declared variable bounds, why naming an expression and declaring its bound tightens the LP relaxation, and how to check this with the root bound and the exported solver model
| Tags: :ref:`tag-modeling-tips`, :ref:`tag-mp`, :ref:`tag-big-m`, :ref:`tag-reinforced-formulations`, :ref:`tag-formulation-comparison`, :ref:`tag-facility-location`, :ref:`tag-milp`, :ref:`tag-amplpy`, :ref:`tag-highs`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-big-m-constants-come-from-declared-bounds|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: declared_bounds_bigm.ipynb
    
.. |colab-big-m-constants-come-from-declared-bounds| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: Open In Colab
    
.. |deepnote-big-m-constants-come-from-declared-bounds| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-big-m-constants-come-from-declared-bounds| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: Open In Kaggle
    
.. |gradient-big-m-constants-come-from-declared-bounds| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-big-m-constants-come-from-declared-bounds| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/declared_bounds_bigm.ipynb
    :alt: Open In SageMaker Studio Lab
    


MP2NL: logical and complementarity constraints with any NL solver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `MP2NL: logical and complementarity constraints with any NL solver <../notebooks/mp2nl-logical-and-complementarity-constraints-with-any-nl-solver.html>`_
| |github-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| |colab-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| |deepnote-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| |kaggle-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| |gradient-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| |sagemaker-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver|
| Description: Using the MP2NL meta-driver from amplpy: which options go where, what the subsolver receives, why the subsolver must handle the problem class MP produces, how to choose a complementarity reformulation, and how to check the returned solution
| Tags: :ref:`tag-mp2nl`, :ref:`tag-mp`, :ref:`tag-minlp`, :ref:`tag-complementarity`, :ref:`tag-solution-check`, :ref:`tag-nonlinear`, :ref:`tag-amplpy`, :ref:`tag-modeling-tips`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: mp2nl_logic_and_complementarity.ipynb
    
.. |colab-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: Open In Colab
    
.. |deepnote-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: Open In Kaggle
    
.. |gradient-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-mp2nl-logical-and-complementarity-constraints-with-any-nl-solver| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/mp2nl_logic_and_complementarity.ipynb
    :alt: Open In SageMaker Studio Lab
    


Perspective reformulation of a convex cost on a semicontinuous variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Perspective reformulation of a convex cost on a semicontinuous variable <../notebooks/perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable.html>`_
| |github-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| |colab-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| |deepnote-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| |kaggle-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| |gradient-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| |sagemaker-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable|
| Description: Unit commitment with a convex piecewise-linear fuel cost: the perspective reformulation, its linear form for piecewise-linear costs, its form for MP's semicontinuous declarations, and checking its value with the root bound before benchmarking
| Tags: :ref:`tag-modeling-tips`, :ref:`tag-mp`, :ref:`tag-perspective`, :ref:`tag-semi-continuous`, :ref:`tag-unit-commitment`, :ref:`tag-piecewise-linear`, :ref:`tag-reinforced-formulations`, :ref:`tag-formulation-comparison`, :ref:`tag-milp`, :ref:`tag-amplpy`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: perspective_unit_commitment.ipynb
    
.. |colab-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: Open In Colab
    
.. |deepnote-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: Open In Kaggle
    
.. |gradient-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-perspective-reformulation-of-a-convex-cost-on-a-semicontinuous-variable| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/perspective_unit_commitment.ipynb
    :alt: Open In SageMaker Studio Lab
    


Robust Linear Programming with Ellipsoidal Uncertainty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Robust Linear Programming with Ellipsoidal Uncertainty <../notebooks/robust-linear-programming-with-ellipsoidal-uncertainty.html>`_
| |github-robust-linear-programming-with-ellipsoidal-uncertainty| |colab-robust-linear-programming-with-ellipsoidal-uncertainty| |deepnote-robust-linear-programming-with-ellipsoidal-uncertainty| |kaggle-robust-linear-programming-with-ellipsoidal-uncertainty| |gradient-robust-linear-programming-with-ellipsoidal-uncertainty| |sagemaker-robust-linear-programming-with-ellipsoidal-uncertainty|
| Description: AMPL Modeling Tips #6: Robust Linear Programming
| Tags: :ref:`tag-highlights`, :ref:`tag-modeling-tips`, :ref:`tag-conic`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-robust-linear-programming-with-ellipsoidal-uncertainty|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: tip6_robust_linear_programming.ipynb
    
.. |colab-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In Colab
    
.. |deepnote-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In Kaggle
    
.. |gradient-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In SageMaker Studio Lab
    


The model as an evaluator: fix the decisions, solve the rest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `The model as an evaluator: fix the decisions, solve the rest <../notebooks/the-model-as-an-evaluator-fix-the-decisions-solve-the-rest.html>`_
| |github-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| |colab-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| |deepnote-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| |kaggle-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| |gradient-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| |sagemaker-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest|
| Description: A local-search heuristic around an AMPL model: fixing the discrete decisions and solving the continuous rest with an NLP solver, checking every solve, ranking infeasible candidates with an elastic model, and comparing against the status-quo baseline
| Tags: :ref:`tag-heuristics`, :ref:`tag-fix-and-solve`, :ref:`tag-modeling-tips`, :ref:`tag-amplpy`, :ref:`tag-nonlinear`, :ref:`tag-local-optimization`, :ref:`tag-facility-location`, :ref:`tag-minlp`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: model_as_evaluator.ipynb
    
.. |colab-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: Open In Colab
    
.. |deepnote-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: Open In Kaggle
    
.. |gradient-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-the-model-as-an-evaluator-fix-the-decisions-solve-the-rest| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-practice/model_as_evaluator.ipynb
    :alt: Open In SageMaker Studio Lab
    


