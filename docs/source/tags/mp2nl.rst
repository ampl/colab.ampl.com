.. _tag-mp2nl:

mp2nl
=====

Unit Commitment MINLP with Knitro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Unit Commitment MINLP with Knitro <../notebooks/unit-commitment-minlp-with-knitro.html>`_
| |github-unit-commitment-minlp-with-knitro| |colab-unit-commitment-minlp-with-knitro| |deepnote-unit-commitment-minlp-with-knitro| |kaggle-unit-commitment-minlp-with-knitro| |gradient-unit-commitment-minlp-with-knitro| |sagemaker-unit-commitment-minlp-with-knitro|
| Description: Solving a nonlinear Unit Commitment problem with Knitro using MP features for logic and multi-objective optimization. The goal of this notebook is to show a straightforward and clear way of using nonlinear solvers for complex models with logical expressions and also hierarchical multi-objective optimization.
| Tags: :ref:`tag-mp`, :ref:`tag-knitro`, :ref:`tag-mp2nl`, :ref:`tag-nonlinear`, :ref:`tag-quadratic`, :ref:`tag-minlp`, :ref:`tag-unit-commitment`, :ref:`tag-electric-power-industry`, :ref:`tag-energy`, :ref:`tag-multi-objective`, :ref:`tag-gurobi`, :ref:`tag-xpress`, :ref:`tag-mp2nl`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-unit-commitment-minlp-with-knitro|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: unit_commitment_minlp_mp2nl.ipynb
    
.. |colab-unit-commitment-minlp-with-knitro| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Colab
    
.. |deepnote-unit-commitment-minlp-with-knitro| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-unit-commitment-minlp-with-knitro| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Kaggle
    
.. |gradient-unit-commitment-minlp-with-knitro| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-unit-commitment-minlp-with-knitro| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In SageMaker Studio Lab
    


Unit Commitment MINLP with Knitro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Unit Commitment MINLP with Knitro <../notebooks/unit-commitment-minlp-with-knitro.html>`_
| |github-unit-commitment-minlp-with-knitro| |colab-unit-commitment-minlp-with-knitro| |deepnote-unit-commitment-minlp-with-knitro| |kaggle-unit-commitment-minlp-with-knitro| |gradient-unit-commitment-minlp-with-knitro| |sagemaker-unit-commitment-minlp-with-knitro|
| Description: Solving a nonlinear Unit Commitment problem with Knitro using MP features for logic and multi-objective optimization. The goal of this notebook is to show a straightforward and clear way of using nonlinear solvers for complex models with logical expressions and also hierarchical multi-objective optimization.
| Tags: :ref:`tag-mp`, :ref:`tag-knitro`, :ref:`tag-mp2nl`, :ref:`tag-nonlinear`, :ref:`tag-quadratic`, :ref:`tag-minlp`, :ref:`tag-unit-commitment`, :ref:`tag-electric-power-industry`, :ref:`tag-energy`, :ref:`tag-multi-objective`, :ref:`tag-gurobi`, :ref:`tag-xpress`, :ref:`tag-mp2nl`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-unit-commitment-minlp-with-knitro|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: unit_commitment_minlp_mp2nl.ipynb
    
.. |colab-unit-commitment-minlp-with-knitro| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Colab
    
.. |deepnote-unit-commitment-minlp-with-knitro| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-unit-commitment-minlp-with-knitro| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Kaggle
    
.. |gradient-unit-commitment-minlp-with-knitro| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-unit-commitment-minlp-with-knitro| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/unit_commitment_minlp_mp2nl.ipynb
    :alt: Open In SageMaker Studio Lab
    


Using multiple objectives in your model 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <../notebooks/index.html>`_ > `Using multiple objectives in your model  <../notebooks/using-multiple-objectives-in-your-model.html>`_
| |github-using-multiple-objectives-in-your-model| |colab-using-multiple-objectives-in-your-model| |deepnote-using-multiple-objectives-in-your-model| |kaggle-using-multiple-objectives-in-your-model| |gradient-using-multiple-objectives-in-your-model| |sagemaker-using-multiple-objectives-in-your-model|
| Description: We show how to use multiple objectives with Amplpy using a nonlinear Unit Commitment problem. We won't be using native or emulated features from the solver interface, but emulating manually a lexicographic multiobjective problem.
| Tags: :ref:`tag-warm-start`, :ref:`tag-mp`, :ref:`tag-multi-objective`, :ref:`tag-gurobi`, :ref:`tag-xpress`, :ref:`tag-knitro`, :ref:`tag-mp2nl`, :ref:`tag-electric-power-industry`, :ref:`tag-unit-commitment`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-using-multiple-objectives-in-your-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: emulate_multiobjective.ipynb
    
.. |colab-using-multiple-objectives-in-your-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: Open In Colab
    
.. |deepnote-using-multiple-objectives-in-your-model| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-using-multiple-objectives-in-your-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: Open In Kaggle
    
.. |gradient-using-multiple-objectives-in-your-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-using-multiple-objectives-in-your-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/emulate_multiobjective.ipynb
    :alt: Open In SageMaker Studio Lab
    


