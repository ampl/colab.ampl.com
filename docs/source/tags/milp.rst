.. _tag-milp:

milp
====

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
    


Infeasible? Ask the solver for an IIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Infeasible? Ask the solver for an IIS <../notebooks/infeasible-ask-the-solver-for-an-iis.html>`_
| |github-infeasible-ask-the-solver-for-an-iis| |colab-infeasible-ask-the-solver-for-an-iis| |deepnote-infeasible-ask-the-solver-for-an-iis| |kaggle-infeasible-ask-the-solver-for-an-iis| |gradient-infeasible-ask-the-solver-for-an-iis| |sagemaker-infeasible-ask-the-solver-for-an-iis|
| Description: Find out why a unit commitment model is infeasible: ask an MP solver for an irreducible infeasible subsystem (IIS) and read it through AMPL suffixes in amplpy
| Tags: :ref:`tag-mp`, :ref:`tag-iis`, :ref:`tag-infeasibility`, :ref:`tag-suffixes`, :ref:`tag-unit-commitment`, :ref:`tag-energy`, :ref:`tag-milp`, :ref:`tag-amplpy`, :ref:`tag-highs`, :ref:`tag-gurobi`, :ref:`tag-xpress`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-infeasible-ask-the-solver-for-an-iis|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
    :alt: iis_unit_commitment.ipynb
    
.. |colab-infeasible-ask-the-solver-for-an-iis| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
    :alt: Open In Colab
    
.. |deepnote-infeasible-ask-the-solver-for-an-iis| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-infeasible-ask-the-solver-for-an-iis| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
    :alt: Open In Kaggle
    
.. |gradient-infeasible-ask-the-solver-for-an-iis| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-infeasible-ask-the-solver-for-an-iis| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/solver-features/iis_unit_commitment.ipynb
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
    


Pricing and target-market
^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Pricing and target-market <../notebooks/pricing-and-target-market.html>`_
| |github-pricing-and-target-market| |colab-pricing-and-target-market| |deepnote-pricing-and-target-market| |kaggle-pricing-and-target-market| |gradient-pricing-and-target-market| |sagemaker-pricing-and-target-market|
| Description: Formulate a pricing optimization and target-market problem as a MILP.
| Tags: :ref:`tag-industry`, :ref:`tag-pricing`, :ref:`tag-milp`, :ref:`tag-mip`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-pricing-and-target-market|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: pricing_and_target_market.ipynb
    
.. |colab-pricing-and-target-market| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In Colab
    
.. |deepnote-pricing-and-target-market| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-pricing-and-target-market| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In Kaggle
    
.. |gradient-pricing-and-target-market| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-pricing-and-target-market| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In SageMaker Studio Lab
    


