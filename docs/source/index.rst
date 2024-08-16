
AMPL Model Colaboratory
=======================

AMPL Model Colaboratory is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as **Google Colab**, **Kaggle**, **Gradient**, and **AWS SageMaker**.
[:ref:`See our Highlights <tag-highlights>`]

.. raw:: html

    <a href="https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb" target="_blank">
        <video width="100%" autoplay loop muted poster="https://ampl.com/upload/videos/nqueens_poster.jpg">
            <source src="https://ampl.com/upload/videos/nqueens.mp4" type="video/mp4" />
        </video>
    </a>

.. grid:: 1 1 2 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::
        :margin: 0
        :padding: 0

        You can use the **Christmas notebook** written by `ChatGPT <https://chat.openai.com/>`_ to get started:

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In SageMaker Studio Lab

        | BTW: you can even ask `ChatGPT <https://chat.openai.com/>`_ to write models for you! If it makes mistakes you can ask for help in our new `Discourse Forum <https://discuss.ampl.com>`_!

    .. grid-item-card::
        :margin: 0
        :padding: 0

        .. figure:: /_static/3lines.png
            :alt: the only 3 lines you need to use AMPL on Colab
            :align: center
            :width: 100%
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/template/minimal.ipynb

Contents
--------

.. toctree::
    :maxdepth: 2

    getting-started
    modules/index
    Highlights <tags/highlights>
    Lectures <tags/ampl-lecture>
    authors/index

.. toctree::
    :hidden:

    tags/index
    notebooks/index

Notebooks
---------


AMPL - solve multiple models in parallel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL - solve multiple models in parallel <notebooks/ampl-solve-multiple-models-in-parallel.html>`_
| |github-ampl-solve-multiple-models-in-parallel| |colab-ampl-solve-multiple-models-in-parallel| |kaggle-ampl-solve-multiple-models-in-parallel| |gradient-ampl-solve-multiple-models-in-parallel| |sagemaker-ampl-solve-multiple-models-in-parallel|
| Description: Solve multiple AMPL models in parallel in Python with amplpy and the multiprocessing modules.
| Tags: :ref:`tag-ampl`, :ref:`tag-python`, :ref:`tag-amplpy`, :ref:`tag-multiprocess`, :ref:`tag-parallel-computing`, :ref:`tag-stochastic-programming`
| Author: :ref:`email-nfbvs_at_ampl.com` <nfbvs@ampl.com>

.. |github-ampl-solve-multiple-models-in-parallel|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: multiproc.ipynb
    
.. |colab-ampl-solve-multiple-models-in-parallel| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-solve-multiple-models-in-parallel| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-solve-multiple-models-in-parallel| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-solve-multiple-models-in-parallel| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL - spreadsheet handling with amplxl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL - spreadsheet handling with amplxl <notebooks/ampl-spreadsheet-handling-with-amplxl.html>`_
| |github-ampl-spreadsheet-handling-with-amplxl| |colab-ampl-spreadsheet-handling-with-amplxl| |kaggle-ampl-spreadsheet-handling-with-amplxl| |gradient-ampl-spreadsheet-handling-with-amplxl| |sagemaker-ampl-spreadsheet-handling-with-amplxl|
| Description: Basic example of reading/writing data into/from a .xlsx spreadsheet with amplxl
| Tags: :ref:`tag-ampl`, :ref:`tag-amplxl`, :ref:`tag-spreadsheet`, :ref:`tag-excel`, :ref:`tag-xlsx`
| Author: :ref:`email-nfbvs_at_ampl.com` <nfbvs@ampl.com>

.. |github-ampl-spreadsheet-handling-with-amplxl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: amplxl.ipynb
    
.. |colab-ampl-spreadsheet-handling-with-amplxl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-spreadsheet-handling-with-amplxl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-spreadsheet-handling-with-amplxl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-spreadsheet-handling-with-amplxl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Bin Packing Problem with GCG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Bin Packing Problem with GCG <notebooks/ampl-bin-packing-problem-with-gcg.html>`_
| |github-ampl-bin-packing-problem-with-gcg| |colab-ampl-bin-packing-problem-with-gcg| |kaggle-ampl-bin-packing-problem-with-gcg| |gradient-ampl-bin-packing-problem-with-gcg| |sagemaker-ampl-bin-packing-problem-with-gcg|
| Description: Dantzig-Wolfe decomposition for Bin Packing Problem with GCG
| Tags: :ref:`tag-gcg`, :ref:`tag-bpp`, :ref:`tag-amplpy`, :ref:`tag-dantzig-wolfe-decomposition`, :ref:`tag-branch-price-and-cut`, :ref:`tag-highlights`
| Author: :ref:`email-jurgenlentz26_at_gmail.com` <jurgenlentz26@gmail.com>

.. |github-ampl-bin-packing-problem-with-gcg|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: bpp.ipynb
    
.. |colab-ampl-bin-packing-problem-with-gcg| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-bin-packing-problem-with-gcg| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-bin-packing-problem-with-gcg| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-bin-packing-problem-with-gcg| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Capacitated p-Median Problem with GCG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Capacitated p-Median Problem with GCG <notebooks/ampl-capacitated-p-median-problem-with-gcg.html>`_
| |github-ampl-capacitated-p-median-problem-with-gcg| |colab-ampl-capacitated-p-median-problem-with-gcg| |kaggle-ampl-capacitated-p-median-problem-with-gcg| |gradient-ampl-capacitated-p-median-problem-with-gcg| |sagemaker-ampl-capacitated-p-median-problem-with-gcg|
| Description: Dantzig-Wolfe decomposition for Capacitated p-Median Problem with GCG
| Tags: :ref:`tag-gcg`, :ref:`tag-cpmp`, :ref:`tag-amplpy`, :ref:`tag-dantzig-wolfe-decomposition`, :ref:`tag-branch-price-and-cut`, :ref:`tag-highlights`
| Author: :ref:`email-jurgenlentz26_at_gmail.com` <jurgenlentz26@gmail.com>

.. |github-ampl-capacitated-p-median-problem-with-gcg|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: cpmp.ipynb
    
.. |colab-ampl-capacitated-p-median-problem-with-gcg| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-capacitated-p-median-problem-with-gcg| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-capacitated-p-median-problem-with-gcg| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-capacitated-p-median-problem-with-gcg| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Christmas Model created by ChatGPT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Christmas Model created by ChatGPT <notebooks/ampl-christmas-model-created-by-chatgpt.html>`_
| |github-ampl-christmas-model-created-by-chatgpt| |colab-ampl-christmas-model-created-by-chatgpt| |kaggle-ampl-christmas-model-created-by-chatgpt| |gradient-ampl-christmas-model-created-by-chatgpt| |sagemaker-ampl-christmas-model-created-by-chatgpt|
| Description: Christmas model generated by ChatGPT
| Tags: :ref:`tag-christmas`, :ref:`tag-chatgpt`, :ref:`tag-amplpy`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-ampl-christmas-model-created-by-chatgpt|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: christmas.ipynb
    
.. |colab-ampl-christmas-model-created-by-chatgpt| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-christmas-model-created-by-chatgpt| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-christmas-model-created-by-chatgpt| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-christmas-model-created-by-chatgpt| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 1/6 -- Capacitated Facility Location Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 1/6 -- Capacitated Facility Location Problem <notebooks/ampl-development-tutorial-16-capacitated-facility-location-problem.html>`_
| |github-ampl-development-tutorial-16-capacitated-facility-location-problem| |colab-ampl-development-tutorial-16-capacitated-facility-location-problem| |kaggle-ampl-development-tutorial-16-capacitated-facility-location-problem| |gradient-ampl-development-tutorial-16-capacitated-facility-location-problem| |sagemaker-ampl-development-tutorial-16-capacitated-facility-location-problem|
| Description: This notebook marks the beginning of a six-part series.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-facility-location`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-16-capacitated-facility-location-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: 1_floc.ipynb
    
.. |colab-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 2/6 -- Stochastic Capacitated Facility Location Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 2/6 -- Stochastic Capacitated Facility Location Problem <notebooks/ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem.html>`_
| |github-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |colab-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |kaggle-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |gradient-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |sagemaker-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem|
| Description: This notebook continues our six-part series as the second installment.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: 2_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 3/6 -- Benders Decomposition via AMPL scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 3/6 -- Benders Decomposition via AMPL scripting <notebooks/ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting.html>`_
| |github-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |colab-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |kaggle-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |gradient-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |sagemaker-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting|
| Description: In this third installment of our six-part series, we continue our exploration by addressing the complexities introduced by the stochastic programming formulation presented in part two.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: 3_benders_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 4/6 -- Benders Decomposition via PYTHON scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 4/6 -- Benders Decomposition via PYTHON scripting <notebooks/ampl-development-tutorial-46-benders-decomposition-via-python-scripting.html>`_
| |github-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |colab-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |kaggle-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |gradient-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |sagemaker-ampl-development-tutorial-46-benders-decomposition-via-python-scripting|
| Description: In this fourth installment of our six-part series, we advance our exploration by demonstrating how to adapt our AMPL script for use with AMPL's Python API.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-46-benders-decomposition-via-python-scripting|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: 4_benders_in_python_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition <notebooks/ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition.html>`_
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
    


AMPL Development Tutorial 6/6 -- Implementing Benders Decomposition with *ampls*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 6/6 -- Implementing Benders Decomposition with *ampls* <notebooks/ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls.html>`_
| |github-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |colab-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |kaggle-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |gradient-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |sagemaker-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls|
| Description: This concluding notebook in our six-part series delves into enhancing the efficiency of our decomposition algorithm by utilizing **AMPL Solver Libraries** (*ampls*).
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-ampls`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>, :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: 6_benders_ampls_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Model Colaboratory Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Model Colaboratory Template <notebooks/ampl-model-colaboratory-template.html>`_
| |github-ampl-model-colaboratory-template| |colab-ampl-model-colaboratory-template| |kaggle-ampl-model-colaboratory-template| |gradient-ampl-model-colaboratory-template| |sagemaker-ampl-model-colaboratory-template|
| Description: Basic notebook template for the AMPL Colab repository
| Tags: :ref:`tag-amplpy`, :ref:`tag-template`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-ampl-model-colaboratory-template|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: colab.ipynb
    
.. |colab-ampl-model-colaboratory-template| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In Colab
    
.. |kaggle-ampl-model-colaboratory-template| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Kaggle
    
.. |gradient-ampl-model-colaboratory-template| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Gradient
    
.. |sagemaker-ampl-model-colaboratory-template| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In SageMaker Studio Lab
    


Aircrew trainee scheduling with seniority constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Aircrew trainee scheduling with seniority constraints <notebooks/aircrew-trainee-scheduling-with-seniority-constraints.html>`_
| |github-aircrew-trainee-scheduling-with-seniority-constraints| |colab-aircrew-trainee-scheduling-with-seniority-constraints| |kaggle-aircrew-trainee-scheduling-with-seniority-constraints| |gradient-aircrew-trainee-scheduling-with-seniority-constraints| |sagemaker-aircrew-trainee-scheduling-with-seniority-constraints|
| Description: Aircrew trainee scheduling with simpler seniority modeling
| Tags: :ref:`tag-trainee-scheduling`, :ref:`tag-aircrew-scheduling`, :ref:`tag-employee-scheduling`, :ref:`tag-seniority-constraints`, :ref:`tag-seniority-ranking`, :ref:`tag-preferential-bidding-system`, :ref:`tag-multiple-objectives`, :ref:`tag-lexicographic-optimization`, :ref:`tag-amplpy`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-aircrew-trainee-scheduling-with-seniority-constraints|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: tip8_aircrew_trainees_seniority.ipynb
    
.. |colab-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In Colab
    
.. |kaggle-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Kaggle
    
.. |gradient-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Gradient
    
.. |sagemaker-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: Economic equilibria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: Economic equilibria <notebooks/book-example-economic-equilibria.html>`_
| |github-book-example-economic-equilibria| |colab-book-example-economic-equilibria| |kaggle-book-example-economic-equilibria| |gradient-book-example-economic-equilibria| |sagemaker-book-example-economic-equilibria|
| Description: economic model using complementarity conditions from Chapter 19 AMPL book
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-finance`, :ref:`tag-complementarity-problem`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-economic-equilibria|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: economic_eq_lecture.ipynb
    
.. |colab-book-example-economic-equilibria| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-economic-equilibria| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-economic-equilibria| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-economic-equilibria| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: Transshipment problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: Transshipment problem <notebooks/book-example-transshipment-problem.html>`_
| |github-book-example-transshipment-problem| |colab-book-example-transshipment-problem| |kaggle-book-example-transshipment-problem| |gradient-book-example-transshipment-problem| |sagemaker-book-example-transshipment-problem|
| Description: book example with general transshipment model (net1.mod)
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-transshipment-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: net1.ipynb
    
.. |colab-book-example-transshipment-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-transshipment-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-transshipment-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-transshipment-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: diet
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: diet <notebooks/book-example-diet.html>`_
| |github-book-example-diet| |colab-book-example-diet| |kaggle-book-example-diet| |gradient-book-example-diet| |sagemaker-book-example-diet|
| Description: book example autogenerated using diet.mod, diet.dat, and diet.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-diet|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: diet.ipynb
    
.. |colab-book-example-diet| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-diet| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-diet| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-diet| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: prod
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: prod <notebooks/book-example-prod.html>`_
| |github-book-example-prod| |colab-book-example-prod| |kaggle-book-example-prod| |gradient-book-example-prod| |sagemaker-book-example-prod|
| Description: book example autogenerated using prod.mod, prod.dat, and prod.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-prod|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: prod.ipynb
    
.. |colab-book-example-prod| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-prod| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-prod| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-prod| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: steel
^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: steel <notebooks/book-example-steel.html>`_
| |github-book-example-steel| |colab-book-example-steel| |kaggle-book-example-steel| |gradient-book-example-steel| |sagemaker-book-example-steel|
| Description: book example autogenerated using steel.mod, steel.dat, and steel.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-steel|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: steel.ipynb
    
.. |colab-book-example-steel| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-steel| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-steel| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-steel| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: transp
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: transp <notebooks/book-example-transp.html>`_
| |github-book-example-transp| |colab-book-example-transp| |kaggle-book-example-transp| |gradient-book-example-transp| |sagemaker-book-example-transp|
| Description: book example autogenerated using transp.mod, transp.dat, and transp.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-transp|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: transp.ipynb
    
.. |colab-book-example-transp| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In Colab
    
.. |kaggle-book-example-transp| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Kaggle
    
.. |gradient-book-example-transp| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Gradient
    
.. |sagemaker-book-example-transp| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In SageMaker Studio Lab
    


CP-style scheduling model with the *numberof* operator, solved by a MIP solver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `CP-style scheduling model with the *numberof* operator, solved by a MIP solver <notebooks/cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver.html>`_
| |github-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |colab-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |kaggle-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |gradient-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |sagemaker-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver|
| Description: Scheduling model with the Constraint Programming *numberof* operator, solved with a MIP solver. New MIP solver drivers based on the [MP library](https://amplmp.readthedocs.io/) enable CP-style modeling.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-constraint-programming`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: sched_numberof.ipynb
    
.. |colab-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In Colab
    
.. |kaggle-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Kaggle
    
.. |gradient-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Gradient
    
.. |sagemaker-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In SageMaker Studio Lab
    


Capacity expansion of power generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Capacity expansion of power generation <notebooks/capacity-expansion-of-power-generation.html>`_
| |github-capacity-expansion-of-power-generation| |colab-capacity-expansion-of-power-generation| |kaggle-capacity-expansion-of-power-generation| |gradient-capacity-expansion-of-power-generation| |sagemaker-capacity-expansion-of-power-generation|
| Description: Models the extensive form of a deterministic multi-stage capacity expansion problem. In this model we can have multiple resources of the same type which have identical properties. The model can be further developed into a stochastic one.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-energy`, :ref:`tag-planning`, :ref:`tag-mip`, :ref:`tag-power-generation`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-capacity-expansion-of-power-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: capacity_expansion.ipynb
    
.. |colab-capacity-expansion-of-power-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In Colab
    
.. |kaggle-capacity-expansion-of-power-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Kaggle
    
.. |gradient-capacity-expansion-of-power-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Gradient
    
.. |sagemaker-capacity-expansion-of-power-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In SageMaker Studio Lab
    


Containers scheduling
^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Containers scheduling <notebooks/containers-scheduling.html>`_
| |github-containers-scheduling| |colab-containers-scheduling| |kaggle-containers-scheduling| |gradient-containers-scheduling| |sagemaker-containers-scheduling|
| Description: Scheduling model for harbor operations. It is a problem with dependences between containers, which should be dispatch the fastest possible. We are using the MP solver interfaces to model a complex system using techniques from Constraint Programming, such as indicator constraints, and logical or and forall operators. After the model is written, a couple instances are presented and Highs/Gurobi MIP solvers are used to tackle the problem.
| Tags: :ref:`tag-amplpy`, :ref:`tag-scheduling`, :ref:`tag-industry`, :ref:`tag-mip`, :ref:`tag-constraint-programming`, :ref:`tag-mp`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-containers-scheduling|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: containers_scheduling.ipynb
    
.. |colab-containers-scheduling| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In Colab
    
.. |kaggle-containers-scheduling| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Kaggle
    
.. |gradient-containers-scheduling| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Gradient
    
.. |sagemaker-containers-scheduling| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In SageMaker Studio Lab
    


Debugging Model Infeasibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Debugging Model Infeasibility <notebooks/debugging-model-infeasibility.html>`_
| |github-debugging-model-infeasibility| |colab-debugging-model-infeasibility| |kaggle-debugging-model-infeasibility| |gradient-debugging-model-infeasibility| |sagemaker-debugging-model-infeasibility|
| Description: This notebook offers a concise guide on troubleshooting model infeasibility using AMPL's presolve feature and other language capabilities.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-debug`, :ref:`tag-infeasibility`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-debugging-model-infeasibility|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: debug_infeas.ipynb
    
.. |colab-debugging-model-infeasibility| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In Colab
    
.. |kaggle-debugging-model-infeasibility| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Kaggle
    
.. |gradient-debugging-model-infeasibility| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Gradient
    
.. |sagemaker-debugging-model-infeasibility| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In SageMaker Studio Lab
    


Diet lecture
^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Diet lecture <notebooks/diet-lecture.html>`_
| |github-diet-lecture| |colab-diet-lecture| |kaggle-diet-lecture| |gradient-diet-lecture| |sagemaker-diet-lecture|
| Description: Diet case study
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-diet-lecture|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: diet_case_study.ipynb
    
.. |colab-diet-lecture| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Colab
    
.. |kaggle-diet-lecture| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Kaggle
    
.. |gradient-diet-lecture| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Gradient
    
.. |sagemaker-diet-lecture| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In SageMaker Studio Lab
    


Diet model with Google Sheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Diet model with Google Sheets <notebooks/diet-model-with-google-sheets.html>`_
| |github-diet-model-with-google-sheets| |colab-diet-model-with-google-sheets|
| Description: Diet model using Google Sheets
| Tags: :ref:`tag-amplpy`, :ref:`tag-google-sheets`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-diet-model-with-google-sheets|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/gspread/gspread.ipynb
    :alt: gspread.ipynb
    
.. |colab-diet-model-with-google-sheets| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/gspread/gspread.ipynb
    :alt: Open In Colab
    


Dual-Donor Organ Exchange problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Dual-Donor Organ Exchange problem <notebooks/dual-donor-organ-exchange-problem.html>`_
| |github-dual-donor-organ-exchange-problem| |colab-dual-donor-organ-exchange-problem| |kaggle-dual-donor-organ-exchange-problem| |gradient-dual-donor-organ-exchange-problem| |sagemaker-dual-donor-organ-exchange-problem|
| Description: Most transplants from living donors require only one donor for each procedure. There are, however, exceptions, including dual-graft liver transplantation, bilateral living-donor lobar lung transplantation, and simultaneous liver-kidney transplantation. For each of these procedures, grafts from two compatible living donors are transplanted. As such, these procedures are more involved from an organizational perspective than those with only one donor. Unfortunately, one or both of the donors can often be biologically incompatible with the intended recipient, precluding the transplantation.
| Tags: :ref:`tag-medicine`, :ref:`tag-organ-exchange`, :ref:`tag-mip`, :ref:`tag-ampl-only`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-dual-donor-organ-exchange-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Dual-Donor_Organ_Exchange.ipynb
    
.. |colab-dual-donor-organ-exchange-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In Colab
    
.. |kaggle-dual-donor-organ-exchange-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Kaggle
    
.. |gradient-dual-donor-organ-exchange-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Gradient
    
.. |sagemaker-dual-donor-organ-exchange-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In SageMaker Studio Lab
    


Dynamic routing example
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Dynamic routing example <notebooks/dynamic-routing-example.html>`_
| |github-dynamic-routing-example| |colab-dynamic-routing-example| |kaggle-dynamic-routing-example| |gradient-dynamic-routing-example| |sagemaker-dynamic-routing-example|
| Description: Example of interactive optimization with GUI using AMPL and Google Maps
| Tags: :ref:`tag-amplpy`, :ref:`tag-gui`
| Author: :ref:`email-christian.valente_at_gmail.com` <christian.valente@gmail.com>

.. |github-dynamic-routing-example|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Dynamic_routing_example.ipynb
    
.. |colab-dynamic-routing-example| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In Colab
    
.. |kaggle-dynamic-routing-example| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Kaggle
    
.. |gradient-dynamic-routing-example| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Gradient
    
.. |sagemaker-dynamic-routing-example| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In SageMaker Studio Lab
    


Efficient Frontier with Google Sheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Efficient Frontier with Google Sheets <notebooks/efficient-frontier-with-google-sheets.html>`_
| |github-efficient-frontier-with-google-sheets| |colab-efficient-frontier-with-google-sheets|
| Description: Efficient Frontier example using Google Sheets
| Tags: :ref:`tag-amplpy`, :ref:`tag-google-sheets`, :ref:`tag-finance`
| Author: :ref:`email-christian.valente_at_gmail.com` <christian.valente@gmail.com>

.. |github-efficient-frontier-with-google-sheets|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/finance/efficient_frontier.ipynb
    :alt: efficient_frontier.ipynb
    
.. |colab-efficient-frontier-with-google-sheets| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/finance/efficient_frontier.ipynb
    :alt: Open In Colab
    


Employee Scheduling Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Employee Scheduling Optimization <notebooks/employee-scheduling-optimization.html>`_
| |github-employee-scheduling-optimization| |colab-employee-scheduling-optimization| |kaggle-employee-scheduling-optimization| |gradient-employee-scheduling-optimization| |sagemaker-employee-scheduling-optimization|
| Description: Employee scheduling model from the Analytical Decision Modeling course at the Arizona State University.
| Tags: :ref:`tag-educational`, :ref:`tag-mip`, :ref:`tag-scheduling`, :ref:`tag-amplpy`, :ref:`tag-gurobi`, :ref:`tag-highs`
| Author: :ref:`email-yimin_wang_at_asu.edu` <yimin_wang@asu.edu>, :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-employee-scheduling-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Employee_Scheduling.ipynb
    
.. |colab-employee-scheduling-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In Colab
    
.. |kaggle-employee-scheduling-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Kaggle
    
.. |gradient-employee-scheduling-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Gradient
    
.. |sagemaker-employee-scheduling-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In SageMaker Studio Lab
    


Financial Portfolio Optimization with amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Financial Portfolio Optimization with amplpy <notebooks/financial-portfolio-optimization-with-amplpy.html>`_
| |github-financial-portfolio-optimization-with-amplpy| |colab-financial-portfolio-optimization-with-amplpy| |kaggle-financial-portfolio-optimization-with-amplpy| |gradient-financial-portfolio-optimization-with-amplpy| |sagemaker-financial-portfolio-optimization-with-amplpy|
| Description: Financial Portfolio Optimization with amplpy and amplpyfinance
| Tags: :ref:`tag-amplpy`, :ref:`tag-amplpyfinance`, :ref:`tag-finance`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-financial-portfolio-optimization-with-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: amplpyfinance_vs_amplpy.ipynb
    
.. |colab-financial-portfolio-optimization-with-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Colab
    
.. |kaggle-financial-portfolio-optimization-with-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Kaggle
    
.. |gradient-financial-portfolio-optimization-with-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Gradient
    
.. |sagemaker-financial-portfolio-optimization-with-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In SageMaker Studio Lab
    


Google Hashcode 2022
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Google Hashcode 2022 <notebooks/google-hashcode-2022.html>`_
| |github-google-hashcode-2022| |colab-google-hashcode-2022| |kaggle-google-hashcode-2022| |gradient-google-hashcode-2022| |sagemaker-google-hashcode-2022|
| Description: Google Hashcode 2022 Practice Problem
| Tags: :ref:`tag-amplpy`, :ref:`tag-heuristics`, :ref:`tag-engineering`, :ref:`tag-scheduling`, :ref:`tag-complexity`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-google-hashcode-2022|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: practice_problem.ipynb
    
.. |colab-google-hashcode-2022| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In Colab
    
.. |kaggle-google-hashcode-2022| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Kaggle
    
.. |gradient-google-hashcode-2022| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Gradient
    
.. |sagemaker-google-hashcode-2022| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In SageMaker Studio Lab
    


Hospitals-Residents MIP
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Hospitals-Residents MIP <notebooks/hospitals-residents-mip.html>`_
| |github-hospitals-residents-mip| |colab-hospitals-residents-mip| |kaggle-hospitals-residents-mip| |gradient-hospitals-residents-mip| |sagemaker-hospitals-residents-mip|
| Description: hospitals-residents problem with ties problem solved with ampl and highs
| Tags: :ref:`tag-amplpy`, :ref:`tag-assignment`, :ref:`tag-mip`, :ref:`tag-data-structures`, :ref:`tag-graphs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-hospitals-residents-mip|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: hospitals_residents.ipynb
    
.. |colab-hospitals-residents-mip| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Colab
    
.. |kaggle-hospitals-residents-mip| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Kaggle
    
.. |gradient-hospitals-residents-mip| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Gradient
    
.. |sagemaker-hospitals-residents-mip| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In SageMaker Studio Lab
    


Hydrothermal Scheduling Problem with Conic Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Hydrothermal Scheduling Problem with Conic Programming <notebooks/hydrothermal-scheduling-problem-with-conic-programming.html>`_
| |github-hydrothermal-scheduling-problem-with-conic-programming| |colab-hydrothermal-scheduling-problem-with-conic-programming| |kaggle-hydrothermal-scheduling-problem-with-conic-programming| |gradient-hydrothermal-scheduling-problem-with-conic-programming| |sagemaker-hydrothermal-scheduling-problem-with-conic-programming|
| Description: Hydrothermal Scheduling Problem using Second-Order Cones
| Tags: :ref:`tag-amplpy`, :ref:`tag-conic`, :ref:`tag-second-order-cone`, :ref:`tag-quadratic-cone`, :ref:`tag-nonlinear-programming`, :ref:`tag-scheduling`, :ref:`tag-engineering`, :ref:`tag-power-generation`, :ref:`tag-geothermal-energy`, :ref:`tag-hydropower`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-hydrothermal-scheduling-problem-with-conic-programming|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: hydrothermal.ipynb
    
.. |colab-hydrothermal-scheduling-problem-with-conic-programming| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In Colab
    
.. |kaggle-hydrothermal-scheduling-problem-with-conic-programming| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Kaggle
    
.. |gradient-hydrothermal-scheduling-problem-with-conic-programming| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Gradient
    
.. |sagemaker-hydrothermal-scheduling-problem-with-conic-programming| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In SageMaker Studio Lab
    


Introduction to Linear and Integer Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Introduction to Linear and Integer Programming <notebooks/introduction-to-linear-and-integer-programming.html>`_
| |github-introduction-to-linear-and-integer-programming| |colab-introduction-to-linear-and-integer-programming| |kaggle-introduction-to-linear-and-integer-programming| |gradient-introduction-to-linear-and-integer-programming| |sagemaker-introduction-to-linear-and-integer-programming|
| Description: Basic introduction to linear programming and AMPL via a lemonade stand example
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-lemonade-stand`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-introduction-to-linear-and-integer-programming|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_prorgramming.ipynb
    :alt: intro_to_linear_prorgramming.ipynb
    
.. |colab-introduction-to-linear-and-integer-programming| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_prorgramming.ipynb
    :alt: Open In Colab
    
.. |kaggle-introduction-to-linear-and-integer-programming| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_prorgramming.ipynb
    :alt: Kaggle
    
.. |gradient-introduction-to-linear-and-integer-programming| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_prorgramming.ipynb
    :alt: Gradient
    
.. |sagemaker-introduction-to-linear-and-integer-programming| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_prorgramming.ipynb
    :alt: Open In SageMaker Studio Lab
    


Introduction to Mathematical Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Introduction to Mathematical Optimization <notebooks/introduction-to-mathematical-optimization.html>`_
| |github-introduction-to-mathematical-optimization| |colab-introduction-to-mathematical-optimization| |kaggle-introduction-to-mathematical-optimization| |gradient-introduction-to-mathematical-optimization| |sagemaker-introduction-to-mathematical-optimization|
| Description: Basic introduction to optimization and AMPL via unconstrained optimization
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-optimization`, :ref:`tag-convexity`, :ref:`tag-unconstrained`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-introduction-to-mathematical-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: intro_to_optimization.ipynb
    
.. |colab-introduction-to-mathematical-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In Colab
    
.. |kaggle-introduction-to-mathematical-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Kaggle
    
.. |gradient-introduction-to-mathematical-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Gradient
    
.. |sagemaker-introduction-to-mathematical-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In SageMaker Studio Lab
    


Jupyter Notebook Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Jupyter Notebook Integration <notebooks/jupyter-notebook-integration.html>`_
| |github-jupyter-notebook-integration| |colab-jupyter-notebook-integration| |kaggle-jupyter-notebook-integration| |gradient-jupyter-notebook-integration| |sagemaker-jupyter-notebook-integration|
| Description: Jupyter Notebook Integration with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-jupyter-notebook-integration|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: magics.ipynb
    
.. |colab-jupyter-notebook-integration| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In Colab
    
.. |kaggle-jupyter-notebook-integration| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Kaggle
    
.. |gradient-jupyter-notebook-integration| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Gradient
    
.. |sagemaker-jupyter-notebook-integration| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In SageMaker Studio Lab
    


Largest small polygon
^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Largest small polygon <notebooks/largest-small-polygon.html>`_
| |github-largest-small-polygon| |colab-largest-small-polygon| |kaggle-largest-small-polygon| |gradient-largest-small-polygon| |sagemaker-largest-small-polygon|
| Description: lecture about models for the Largest Small Polygon Problem
| Tags: :ref:`tag-geometry`, :ref:`tag-non-linear`, :ref:`tag-amplpy`, :ref:`tag-ipopt`, :ref:`tag-educational`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-largest-small-polygon|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: largest_small_polygon.ipynb
    
.. |colab-largest-small-polygon| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In Colab
    
.. |kaggle-largest-small-polygon| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Kaggle
    
.. |gradient-largest-small-polygon| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Gradient
    
.. |sagemaker-largest-small-polygon| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In SageMaker Studio Lab
    


Logistic Regression with amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Logistic Regression with amplpy <notebooks/logistic-regression-with-amplpy.html>`_
| |github-logistic-regression-with-amplpy| |colab-logistic-regression-with-amplpy| |kaggle-logistic-regression-with-amplpy| |gradient-logistic-regression-with-amplpy| |sagemaker-logistic-regression-with-amplpy|
| Description: Logistic regression with amplpy using exponential cones
| Tags: :ref:`tag-highlights`, :ref:`tag-amplpy`, :ref:`tag-regression`, :ref:`tag-sigmoid`, :ref:`tag-softplus`, :ref:`tag-log-sum-exp`, :ref:`tag-classifier`, :ref:`tag-regularization`, :ref:`tag-machine-learning`, :ref:`tag-conic`, :ref:`tag-exponential-cone`, :ref:`tag-second-order-cone`, :ref:`tag-quadratic-cone`, :ref:`tag-formulation-comparison`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>, :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-logistic-regression-with-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: logistic_regression.ipynb
    
.. |colab-logistic-regression-with-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In Colab
    
.. |kaggle-logistic-regression-with-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Kaggle
    
.. |gradient-logistic-regression-with-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Gradient
    
.. |sagemaker-logistic-regression-with-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In SageMaker Studio Lab
    


Magic sequences
^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Magic sequences <notebooks/magic-sequences.html>`_
| |github-magic-sequences| |colab-magic-sequences| |kaggle-magic-sequences| |gradient-magic-sequences| |sagemaker-magic-sequences|
| Description: Solving magic sequences through reinforced formulations and constrained programming. Some comparison between models and solvers is done, and we look into the "Another solution" problem for these sequences.
| Tags: :ref:`tag-constraint-programming`, :ref:`tag-educational`, :ref:`tag-mp`, :ref:`tag-sequences`, :ref:`tag-arithmetic`, :ref:`tag-reinforced-formulations`, :ref:`tag-highs`, :ref:`tag-gecode`, :ref:`tag-cbc`, :ref:`tag-mip`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-magic-sequences|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: magic_sequences.ipynb
    
.. |colab-magic-sequences| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In Colab
    
.. |kaggle-magic-sequences| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Kaggle
    
.. |gradient-magic-sequences| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Gradient
    
.. |sagemaker-magic-sequences| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In SageMaker Studio Lab
    


Multicommodity transportation problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Multicommodity transportation problem <notebooks/multicommodity-transportation-problem.html>`_
| |github-multicommodity-transportation-problem| |colab-multicommodity-transportation-problem| |kaggle-multicommodity-transportation-problem| |gradient-multicommodity-transportation-problem| |sagemaker-multicommodity-transportation-problem|
| Description: Multicommodity transportation model with binary variables
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-mixed-integer-linear`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-multicommodity-transportation-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: multmip1.ipynb
    
.. |colab-multicommodity-transportation-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Colab
    
.. |kaggle-multicommodity-transportation-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Kaggle
    
.. |gradient-multicommodity-transportation-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Gradient
    
.. |sagemaker-multicommodity-transportation-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In SageMaker Studio Lab
    


N-Queens
^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `N-Queens <notebooks/n-queens.html>`_
| |github-n-queens| |colab-n-queens| |kaggle-n-queens| |gradient-n-queens| |sagemaker-n-queens|
| Description: How can N queens be placed on an NxN chessboard so that no two of them attack each other?
| Tags: :ref:`tag-amplpy`, :ref:`tag-constraint-programming`, :ref:`tag-highlights`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-n-queens|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: nqueens.ipynb
    
.. |colab-n-queens| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In Colab
    
.. |kaggle-n-queens| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Kaggle
    
.. |gradient-n-queens| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Gradient
    
.. |sagemaker-n-queens| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In SageMaker Studio Lab
    


NFL Team Rating
^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `NFL Team Rating <notebooks/nfl-team-rating.html>`_
| |github-nfl-team-rating| |colab-nfl-team-rating| |kaggle-nfl-team-rating| |gradient-nfl-team-rating| |sagemaker-nfl-team-rating|
| Description: NFL Team Rating problem from the Analytical Decision Modeling course at the Arizona State University.
| Tags: :ref:`tag-educational`, :ref:`tag-quadratic`, :ref:`tag-amplpy`, :ref:`tag-gurobi`
| Author: :ref:`email-yimin_wang_at_asu.edu` <yimin_wang@asu.edu>, :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nfl-team-rating|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: NFL_Team_Rating.ipynb
    
.. |colab-nfl-team-rating| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In Colab
    
.. |kaggle-nfl-team-rating| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Kaggle
    
.. |gradient-nfl-team-rating| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Gradient
    
.. |sagemaker-nfl-team-rating| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In SageMaker Studio Lab
    


Network Linear Programs
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Network Linear Programs <notebooks/network-linear-programs.html>`_
| |github-network-linear-programs| |colab-network-linear-programs| |kaggle-network-linear-programs| |gradient-network-linear-programs| |sagemaker-network-linear-programs|
| Description: Basic introduction to network linear programms and AMPL via max flow and shortest path problems
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-max-flow`, :ref:`tag-shortest-path`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-network-linear-programs|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: network.ipynb
    
.. |colab-network-linear-programs| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In Colab
    
.. |kaggle-network-linear-programs| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Kaggle
    
.. |gradient-network-linear-programs| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Gradient
    
.. |sagemaker-network-linear-programs| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In SageMaker Studio Lab
    


Network design with redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Network design with redundancy <notebooks/network-design-with-redundancy.html>`_
| |github-network-design-with-redundancy| |colab-network-design-with-redundancy| |kaggle-network-design-with-redundancy| |gradient-network-design-with-redundancy| |sagemaker-network-design-with-redundancy|
| Description: Design of an electricity transportation network provides enough redundancy, so that a break of one component does not prevent any user from receiving electricity. The approach also works for similar distribution networks and can potentially be used in the design of military logistic networks.
| Tags: :ref:`tag-electric-grid`, :ref:`tag-military`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-network-design-with-redundancy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: electric_grid_with_redundancy.ipynb
    
.. |colab-network-design-with-redundancy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Colab
    
.. |kaggle-network-design-with-redundancy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Kaggle
    
.. |gradient-network-design-with-redundancy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Gradient
    
.. |sagemaker-network-design-with-redundancy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In SageMaker Studio Lab
    


Nonlinear transportation model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Nonlinear transportation model <notebooks/nonlinear-transportation-model.html>`_
| |github-nonlinear-transportation-model| |colab-nonlinear-transportation-model| |kaggle-nonlinear-transportation-model| |gradient-nonlinear-transportation-model| |sagemaker-nonlinear-transportation-model|
| Description: book example autogenerated using nltransd.mod, nltrans.dat, and nltrans.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-nonlinear`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nonlinear-transportation-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: nltrans_lecture.ipynb
    
.. |colab-nonlinear-transportation-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Colab
    
.. |kaggle-nonlinear-transportation-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Kaggle
    
.. |gradient-nonlinear-transportation-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Gradient
    
.. |sagemaker-nonlinear-transportation-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Nonlinear transportation problem example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Nonlinear transportation problem example <notebooks/nonlinear-transportation-problem-example.html>`_
| |github-nonlinear-transportation-problem-example| |colab-nonlinear-transportation-problem-example| |kaggle-nonlinear-transportation-problem-example| |gradient-nonlinear-transportation-problem-example| |sagemaker-nonlinear-transportation-problem-example|
| Description: book example autogenerated using nltransd.mod, nltrans.dat, and nltrans.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-nonlinear`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nonlinear-transportation-problem-example|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: nltrans.ipynb
    
.. |colab-nonlinear-transportation-problem-example| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Colab
    
.. |kaggle-nonlinear-transportation-problem-example| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Kaggle
    
.. |gradient-nonlinear-transportation-problem-example| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Gradient
    
.. |sagemaker-nonlinear-transportation-problem-example| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In SageMaker Studio Lab
    


Oil refinery production optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Oil refinery production optimization <notebooks/oil-refinery-production-optimization.html>`_
| |github-oil-refinery-production-optimization| |colab-oil-refinery-production-optimization| |kaggle-oil-refinery-production-optimization| |gradient-oil-refinery-production-optimization| |sagemaker-oil-refinery-production-optimization|
| Tags: :ref:`tag-oil-production`, :ref:`tag-production-optimization`, :ref:`tag-profitability`, :ref:`tag-refinery`, :ref:`tag-deterministic-model`, :ref:`tag-piecewise-linear`, :ref:`tag-mip`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-oil-refinery-production-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: oil_refining.ipynb
    
.. |colab-oil-refinery-production-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In Colab
    
.. |kaggle-oil-refinery-production-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Kaggle
    
.. |gradient-oil-refinery-production-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Gradient
    
.. |sagemaker-oil-refinery-production-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization Methods in Finance: Chapter 3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization Methods in Finance: Chapter 3 <notebooks/optimization-methods-in-finance-chapter-3.html>`_
| |github-optimization-methods-in-finance-chapter-3| |colab-optimization-methods-in-finance-chapter-3| |kaggle-optimization-methods-in-finance-chapter-3| |gradient-optimization-methods-in-finance-chapter-3| |sagemaker-optimization-methods-in-finance-chapter-3|
| Description: Optimization Methods in Finance: Bond Dedication Problem.
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`, :ref:`tag-finance`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-optimization-methods-in-finance-chapter-3|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: finance_opt_example_3_1.ipynb
    
.. |colab-optimization-methods-in-finance-chapter-3| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Colab
    
.. |kaggle-optimization-methods-in-finance-chapter-3| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Kaggle
    
.. |gradient-optimization-methods-in-finance-chapter-3| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Gradient
    
.. |sagemaker-optimization-methods-in-finance-chapter-3| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization of an TV advertising campaign based on TRP, GRP indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization of an TV advertising campaign based on TRP, GRP indicators <notebooks/optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators.html>`_
| |github-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |colab-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |kaggle-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |gradient-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |sagemaker-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators|
| Description: The modern world is unthinkable without advertising. Advertising is the engine of progress.
| Tags: :ref:`tag-marketing`, :ref:`tag-advertisement`, :ref:`tag-deterministic-model`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: TV_Advertisement_campaign_GRP_TRP.ipynb
    
.. |colab-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In Colab
    
.. |kaggle-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Kaggle
    
.. |gradient-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Gradient
    
.. |sagemaker-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization of an advertising campaign for launching a new product on the market
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization of an advertising campaign for launching a new product on the market <notebooks/optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market.html>`_
| |github-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |colab-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |kaggle-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |gradient-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |sagemaker-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market|
| Description: The modern world is unthinkable without advertising. Advertising is the engine of progress.
| Tags: :ref:`tag-marketing`, :ref:`tag-advertisement`, :ref:`tag-deterministic-model`, :ref:`tag-piecewise-linear`, :ref:`tag-mip`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Advertising_campaign_colab.ipynb
    
.. |colab-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In Colab
    
.. |kaggle-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Kaggle
    
.. |gradient-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Gradient
    
.. |sagemaker-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimize your Christmas Tree to Global Optimality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimize your Christmas Tree to Global Optimality <notebooks/optimize-your-christmas-tree-to-global-optimality.html>`_
| |github-optimize-your-christmas-tree-to-global-optimality| |colab-optimize-your-christmas-tree-to-global-optimality| |kaggle-optimize-your-christmas-tree-to-global-optimality| |gradient-optimize-your-christmas-tree-to-global-optimality| |sagemaker-optimize-your-christmas-tree-to-global-optimality|
| Description: Optimize the placement of ornaments on a christmas tree.
| Tags: :ref:`tag-christmas`, :ref:`tag-amplpy`, :ref:`tag-global-optimization`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-optimize-your-christmas-tree-to-global-optimality|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: christmas_tree.ipynb
    
.. |colab-optimize-your-christmas-tree-to-global-optimality| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In Colab
    
.. |kaggle-optimize-your-christmas-tree-to-global-optimality| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Kaggle
    
.. |gradient-optimize-your-christmas-tree-to-global-optimality| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Gradient
    
.. |sagemaker-optimize-your-christmas-tree-to-global-optimality| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In SageMaker Studio Lab
    


P-Median problem
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `P-Median problem <notebooks/p-median-problem.html>`_
| |github-p-median-problem| |colab-p-median-problem| |kaggle-p-median-problem| |gradient-p-median-problem| |sagemaker-p-median-problem|
| Description: this notebook states the p-median problem with a simple example, and a MIP formulation in amplpy. The problem is parametrized with a class, so it is easier to sample and replicate experiments. A graphical solution is plotted.
| Tags: :ref:`tag-amplpy`, :ref:`tag-mip`, :ref:`tag-facility-location`, :ref:`tag-bin-packing`, :ref:`tag-graphs`, :ref:`tag-highs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-p-median-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: p_median.ipynb
    
.. |colab-p-median-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In Colab
    
.. |kaggle-p-median-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Kaggle
    
.. |gradient-p-median-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Gradient
    
.. |sagemaker-p-median-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pattern Enumeration
^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pattern Enumeration <notebooks/pattern-enumeration.html>`_
| |github-pattern-enumeration| |colab-pattern-enumeration| |kaggle-pattern-enumeration| |gradient-pattern-enumeration| |sagemaker-pattern-enumeration|
| Description: Pattern enumeration example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-pattern-enumeration|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: pattern_enumeration.ipynb
    
.. |colab-pattern-enumeration| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In Colab
    
.. |kaggle-pattern-enumeration| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Kaggle
    
.. |gradient-pattern-enumeration| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Gradient
    
.. |sagemaker-pattern-enumeration| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pattern Generation
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pattern Generation <notebooks/pattern-generation.html>`_
| |github-pattern-generation| |colab-pattern-generation| |kaggle-pattern-generation| |gradient-pattern-generation| |sagemaker-pattern-generation|
| Description: Pattern generation example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-pattern-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: pattern_generation.ipynb
    
.. |colab-pattern-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In Colab
    
.. |kaggle-pattern-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Kaggle
    
.. |gradient-pattern-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Gradient
    
.. |sagemaker-pattern-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In SageMaker Studio Lab
    


Plot feasible region
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Plot feasible region <notebooks/plot-feasible-region.html>`_
| |github-plot-feasible-region| |colab-plot-feasible-region| |kaggle-plot-feasible-region| |gradient-plot-feasible-region| |sagemaker-plot-feasible-region|
| Description: Plot the feasible region and optimal solution for a simple two variable model using AMPL's Python API.
| Tags: :ref:`tag-lecture`, :ref:`tag-lp`, :ref:`tag-simple`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>, :ref:`email-sarah_at_ampl.com` <sarah@ampl.com>

.. |github-plot-feasible-region|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: plot_feasible_region.ipynb
    
.. |colab-plot-feasible-region| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In Colab
    
.. |kaggle-plot-feasible-region| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Kaggle
    
.. |gradient-plot-feasible-region| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Gradient
    
.. |sagemaker-plot-feasible-region| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pricing and target-market
^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pricing and target-market <notebooks/pricing-and-target-market.html>`_
| |github-pricing-and-target-market| |colab-pricing-and-target-market| |kaggle-pricing-and-target-market| |gradient-pricing-and-target-market| |sagemaker-pricing-and-target-market|
| Description: Formulate a pricing optimization and target-market problem as a MILP.
| Tags: :ref:`tag-industry`, :ref:`tag-pricing`, :ref:`tag-milp`, :ref:`tag-mip`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-pricing-and-target-market|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: pricing_and_target_market.ipynb
    
.. |colab-pricing-and-target-market| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In Colab
    
.. |kaggle-pricing-and-target-market| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Kaggle
    
.. |gradient-pricing-and-target-market| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Gradient
    
.. |sagemaker-pricing-and-target-market| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/miscellaneous/pricing_and_target_market.ipynb
    :alt: Open In SageMaker Studio Lab
    


Production Model
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Production Model <notebooks/production-model.html>`_
| |github-production-model| |colab-production-model| |kaggle-production-model| |gradient-production-model| |sagemaker-production-model|
| Description: Basic introduction to AMPL's indexed entities and the Pygwalker Python package via a lemonade stand example
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-sets`, :ref:`tag-indexing`, :ref:`tag-lemonade-stand`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-production-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: production_model.ipynb
    
.. |colab-production-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In Colab
    
.. |kaggle-production-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Kaggle
    
.. |gradient-production-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Gradient
    
.. |sagemaker-production-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In SageMaker Studio Lab
    


Production model
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Production model <notebooks/production-model.html>`_
| |github-production-model| |colab-production-model| |kaggle-production-model| |gradient-production-model| |sagemaker-production-model|
| Description: generic model for production problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-industry`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-production-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: production_model.ipynb
    
.. |colab-production-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Colab
    
.. |kaggle-production-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Kaggle
    
.. |gradient-production-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Gradient
    
.. |sagemaker-production-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In SageMaker Studio Lab
    


Quick Start using Pandas dataframes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Quick Start using Pandas dataframes <notebooks/quick-start-using-pandas-dataframes.html>`_
| |github-quick-start-using-pandas-dataframes| |colab-quick-start-using-pandas-dataframes| |kaggle-quick-start-using-pandas-dataframes| |gradient-quick-start-using-pandas-dataframes| |sagemaker-quick-start-using-pandas-dataframes|
| Description: Quick Start using Pandas dataframes to load and retrieve data
| Tags: :ref:`tag-amplpy`, :ref:`tag-quick-start`, :ref:`tag-pandas`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-quick-start-using-pandas-dataframes|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: pandasdiet.ipynb
    
.. |colab-quick-start-using-pandas-dataframes| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In Colab
    
.. |kaggle-quick-start-using-pandas-dataframes| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Kaggle
    
.. |gradient-quick-start-using-pandas-dataframes| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Gradient
    
.. |sagemaker-quick-start-using-pandas-dataframes| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Quick Start using lists and dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Quick Start using lists and dictionaries <notebooks/quick-start-using-lists-and-dictionaries.html>`_
| |github-quick-start-using-lists-and-dictionaries| |colab-quick-start-using-lists-and-dictionaries| |kaggle-quick-start-using-lists-and-dictionaries| |gradient-quick-start-using-lists-and-dictionaries| |sagemaker-quick-start-using-lists-and-dictionaries|
| Description: Quick Start using lists and dictionaries to load and retrieve data
| Tags: :ref:`tag-amplpy`, :ref:`tag-quick-start`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-quick-start-using-lists-and-dictionaries|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: nativediet.ipynb
    
.. |colab-quick-start-using-lists-and-dictionaries| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In Colab
    
.. |kaggle-quick-start-using-lists-and-dictionaries| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Kaggle
    
.. |gradient-quick-start-using-lists-and-dictionaries| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Gradient
    
.. |sagemaker-quick-start-using-lists-and-dictionaries| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Robust Linear Programming with Ellipsoidal Uncertainty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Robust Linear Programming with Ellipsoidal Uncertainty <notebooks/robust-linear-programming-with-ellipsoidal-uncertainty.html>`_
| |github-robust-linear-programming-with-ellipsoidal-uncertainty| |colab-robust-linear-programming-with-ellipsoidal-uncertainty| |kaggle-robust-linear-programming-with-ellipsoidal-uncertainty| |gradient-robust-linear-programming-with-ellipsoidal-uncertainty| |sagemaker-robust-linear-programming-with-ellipsoidal-uncertainty|
| Description: AMPL Modeling Tips #6: Robust Linear Programming
| Tags: :ref:`tag-highlights`, :ref:`tag-modeling-tips`, :ref:`tag-conic`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-robust-linear-programming-with-ellipsoidal-uncertainty|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: tip6_robust_linear_programming.ipynb
    
.. |colab-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In Colab
    
.. |kaggle-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Kaggle
    
.. |gradient-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Gradient
    
.. |sagemaker-robust-linear-programming-with-ellipsoidal-uncertainty| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip6_robust_linear_programming.ipynb
    :alt: Open In SageMaker Studio Lab
    


Roll Cutting - Revision 1 & 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Roll Cutting - Revision 1 & 2 <notebooks/roll-cutting-revision-1-and-2.html>`_
| |github-roll-cutting-revision-1-and-2| |colab-roll-cutting-revision-1-and-2| |kaggle-roll-cutting-revision-1-and-2| |gradient-roll-cutting-revision-1-and-2| |sagemaker-roll-cutting-revision-1-and-2|
| Description: Pattern tradeoff example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-roll-cutting-revision-1-and-2|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: pattern_tradeoff.ipynb
    
.. |colab-roll-cutting-revision-1-and-2| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In Colab
    
.. |kaggle-roll-cutting-revision-1-and-2| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Kaggle
    
.. |gradient-roll-cutting-revision-1-and-2| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Gradient
    
.. |sagemaker-roll-cutting-revision-1-and-2| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In SageMaker Studio Lab
    


Scheduling Multipurpose Batch Processes using State-Task Networks in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Scheduling Multipurpose Batch Processes using State-Task Networks in Python <notebooks/scheduling-multipurpose-batch-processes-using-state-task-networks-in-python.html>`_
| |github-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |colab-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |kaggle-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |gradient-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |sagemaker-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python|
| Description: The State-Task Network (STN) is an approach to modeling multipurpose batch process for the purpose of short term scheduling. It was first developed by Kondili, et al., in 1993, and subsequently developed and extended by others.
| Tags: :ref:`tag-state-task-networks`, :ref:`tag-gdp`, :ref:`tag-disjunctive-programming`, :ref:`tag-batch-processes`, :ref:`tag-batch-processing`
| Author: Jeffrey C. Kantor, :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: batch_processessing.ipynb
    
.. |colab-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In Colab
    
.. |kaggle-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Kaggle
    
.. |gradient-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Gradient
    
.. |sagemaker-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In SageMaker Studio Lab
    


Simple sudoku solver using logical constraints (with GUI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Simple sudoku solver using logical constraints (with GUI) <notebooks/simple-sudoku-solver-using-logical-constraints-with-gui.html>`_
| |github-simple-sudoku-solver-using-logical-constraints-with-gui| |colab-simple-sudoku-solver-using-logical-constraints-with-gui| |kaggle-simple-sudoku-solver-using-logical-constraints-with-gui| |gradient-simple-sudoku-solver-using-logical-constraints-with-gui| |sagemaker-simple-sudoku-solver-using-logical-constraints-with-gui|
| Description: Simple sudoku model with two formulations: as a Constraint Programming problem using the *alldiff* operator and as a MIP. Note that the CP formulation is more natural but it needs a solver supporting logical constraints or a MIP solver with automatic reformulation support (see [here](https://mp.ampl.com/) for more information).
| Tags: :ref:`tag-amplpy`, :ref:`tag-constraint-programming`, :ref:`tag-gui`, :ref:`tag-highlights`
| Author: :ref:`email-christian.valente_at_gmail.com` <christian.valente@gmail.com>

.. |github-simple-sudoku-solver-using-logical-constraints-with-gui|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: sudoku.ipynb
    
.. |colab-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In Colab
    
.. |kaggle-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Kaggle
    
.. |gradient-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Gradient
    
.. |sagemaker-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solution check: discontinuous objective function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solution check: discontinuous objective function <notebooks/solution-check-discontinuous-objective-function.html>`_
| |github-solution-check-discontinuous-objective-function| |colab-solution-check-discontinuous-objective-function| |kaggle-solution-check-discontinuous-objective-function| |gradient-solution-check-discontinuous-objective-function| |sagemaker-solution-check-discontinuous-objective-function|
| Description: Pathological examples to illustrate MP solution checker and settings
| Tags: :ref:`tag-mp-library`, :ref:`tag-solution-check`, :ref:`tag-non-continuous-objective`, :ref:`tag-strict-comparison`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-solution-check-discontinuous-objective-function|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: sol-check.ipynb
    
.. |colab-solution-check-discontinuous-objective-function| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In Colab
    
.. |kaggle-solution-check-discontinuous-objective-function| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Kaggle
    
.. |gradient-solution-check-discontinuous-objective-function| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Gradient
    
.. |sagemaker-solution-check-discontinuous-objective-function| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solving a nonogram puzzle
^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solving a nonogram puzzle <notebooks/solving-a-nonogram-puzzle.html>`_
| |github-solving-a-nonogram-puzzle| |colab-solving-a-nonogram-puzzle| |kaggle-solving-a-nonogram-puzzle| |gradient-solving-a-nonogram-puzzle| |sagemaker-solving-a-nonogram-puzzle|
| Description: Model for solving nonogram puzzles autogenerated using **nonogram.mod**, **nonogram.dat** and **nonogram.run**.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-mip`
| Author: :ref:`email-juanjesus.losada_at_gmail.com` <juanjesus.losada@gmail.com>

.. |github-solving-a-nonogram-puzzle|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: nonogram.ipynb
    
.. |colab-solving-a-nonogram-puzzle| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In Colab
    
.. |kaggle-solving-a-nonogram-puzzle| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Kaggle
    
.. |gradient-solving-a-nonogram-puzzle| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Gradient
    
.. |sagemaker-solving-a-nonogram-puzzle| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solving simple stochastic optimization problems with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solving simple stochastic optimization problems with AMPL <notebooks/solving-simple-stochastic-optimization-problems-with-ampl.html>`_
| |github-solving-simple-stochastic-optimization-problems-with-ampl| |colab-solving-simple-stochastic-optimization-problems-with-ampl| |kaggle-solving-simple-stochastic-optimization-problems-with-ampl| |gradient-solving-simple-stochastic-optimization-problems-with-ampl| |sagemaker-solving-simple-stochastic-optimization-problems-with-ampl|
| Description: Examples of the Sample Average Approximation method and risk measures in AMPL
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-stochastic-optimization`, :ref:`tag-sample-average-approximation`, :ref:`tag-risk-measures`
| Author: :ref:`email-nfbvs_at_ampl.com` <nfbvs@ampl.com>

.. |github-solving-simple-stochastic-optimization-problems-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: newsvendor.ipynb
    
.. |colab-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In Colab
    
.. |kaggle-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Kaggle
    
.. |gradient-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Gradient
    
.. |sagemaker-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In SageMaker Studio Lab
    


Steel industry problem
^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Steel industry problem <notebooks/steel-industry-problem.html>`_
| |github-steel-industry-problem| |colab-steel-industry-problem| |kaggle-steel-industry-problem| |gradient-steel-industry-problem| |sagemaker-steel-industry-problem|
| Description: model for steel production problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`, :ref:`tag-industry`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-steel-industry-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: steel_lecture.ipynb
    
.. |colab-steel-industry-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Colab
    
.. |kaggle-steel-industry-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Kaggle
    
.. |gradient-steel-industry-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Gradient
    
.. |sagemaker-steel-industry-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Sudoku Generator
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Sudoku Generator <notebooks/sudoku-generator.html>`_
| |github-sudoku-generator| |colab-sudoku-generator| |kaggle-sudoku-generator| |gradient-sudoku-generator| |sagemaker-sudoku-generator|
| Description: Generate Sudoku boards with unique solution via iterative method and mip formulation.
| Tags: :ref:`tag-mip`, :ref:`tag-heuristics`, :ref:`tag-puzzles`, :ref:`tag-amplpy`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-sudoku-generator|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: sudoku_gen.ipynb
    
.. |colab-sudoku-generator| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In Colab
    
.. |kaggle-sudoku-generator| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Kaggle
    
.. |gradient-sudoku-generator| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Gradient
    
.. |sagemaker-sudoku-generator| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In SageMaker Studio Lab
    


Supply chain network
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Supply chain network <notebooks/supply-chain-network.html>`_
| |github-supply-chain-network| |colab-supply-chain-network| |kaggle-supply-chain-network| |gradient-supply-chain-network| |sagemaker-supply-chain-network|
| Description: Compute optimal routes to connect suppliers/demanding nodes in a network. Routes have an associated fixed and variable cost. There are different products to ship. The problem is formulated as a MIP with binary variables. Python data structures are used to load the data into the model.
| Tags: :ref:`tag-mixed-integer-linear`, :ref:`tag-supply_chain`, :ref:`tag-network`, :ref:`tag-transportation`, :ref:`tag-graphs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-supply-chain-network|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: supply_chain_simple_routes.ipynb
    
.. |colab-supply-chain-network| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In Colab
    
.. |kaggle-supply-chain-network| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Kaggle
    
.. |gradient-supply-chain-network| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Gradient
    
.. |sagemaker-supply-chain-network| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In SageMaker Studio Lab
    


Transportation problem
^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Transportation problem <notebooks/transportation-problem.html>`_
| |github-transportation-problem| |colab-transportation-problem| |kaggle-transportation-problem| |gradient-transportation-problem| |sagemaker-transportation-problem|
| Description: an AMPL model for the transportation problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-transportation-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: transp_lecture.ipynb
    
.. |colab-transportation-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Colab
    
.. |kaggle-transportation-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Kaggle
    
.. |gradient-transportation-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Gradient
    
.. |sagemaker-transportation-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Travelling Salesman Problem with subtour elimination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Travelling Salesman Problem with subtour elimination <notebooks/travelling-salesman-problem-with-subtour-elimination.html>`_
| |github-travelling-salesman-problem-with-subtour-elimination| |colab-travelling-salesman-problem-with-subtour-elimination| |kaggle-travelling-salesman-problem-with-subtour-elimination| |gradient-travelling-salesman-problem-with-subtour-elimination| |sagemaker-travelling-salesman-problem-with-subtour-elimination|
| Description: this example shows how to solve a TSP  by eliminating subtours using amplpy and ampls
| Tags: :ref:`tag-callbacks`, :ref:`tag-tsp`
| Author: :ref:`email-christian.valente_at_gmail.com` <christian.valente@gmail.com>

.. |github-travelling-salesman-problem-with-subtour-elimination|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: tsp_simple_cuts_generic.ipynb
    
.. |colab-travelling-salesman-problem-with-subtour-elimination| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In Colab
    
.. |kaggle-travelling-salesman-problem-with-subtour-elimination| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Kaggle
    
.. |gradient-travelling-salesman-problem-with-subtour-elimination| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Gradient
    
.. |sagemaker-travelling-salesman-problem-with-subtour-elimination| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In SageMaker Studio Lab
    


Unit Commitment for Electrical Power Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Unit Commitment for Electrical Power Generation <notebooks/unit-commitment-for-electrical-power-generation.html>`_
| |github-unit-commitment-for-electrical-power-generation| |colab-unit-commitment-for-electrical-power-generation| |kaggle-unit-commitment-for-electrical-power-generation| |gradient-unit-commitment-for-electrical-power-generation| |sagemaker-unit-commitment-for-electrical-power-generation|
| Description: This notebook illustrates the power generation problem using AMPL. The original version featured the Gurobi solver. By default, this notebook uses the HiGHS and CBC solvers.
| Tags: :ref:`tag-amplpy`, :ref:`tag-energy`, :ref:`tag-power-generation`, :ref:`tag-unit-commitment`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-unit-commitment-for-electrical-power-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: unit_commitment.ipynb
    
.. |colab-unit-commitment-for-electrical-power-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In Colab
    
.. |kaggle-unit-commitment-for-electrical-power-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Kaggle
    
.. |gradient-unit-commitment-for-electrical-power-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Gradient
    
.. |sagemaker-unit-commitment-for-electrical-power-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In SageMaker Studio Lab
    


VPSolver: Cutting & Packing Problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `VPSolver: Cutting & Packing Problems <notebooks/vpsolver-cutting-and-packing-problems.html>`_
| |github-vpsolver-cutting-and-packing-problems| |colab-vpsolver-cutting-and-packing-problems| |kaggle-vpsolver-cutting-and-packing-problems| |gradient-vpsolver-cutting-and-packing-problems| |sagemaker-vpsolver-cutting-and-packing-problems|
| Description: Solving cutting & packing problems using arc-flow formulations
| Tags: :ref:`tag-industry`, :ref:`tag-cutting-stock`, :ref:`tag-bin-packing`, :ref:`tag-vector-packing`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-vpsolver-cutting-and-packing-problems|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: vpsolver.ipynb
    
.. |colab-vpsolver-cutting-and-packing-problems| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In Colab
    
.. |kaggle-vpsolver-cutting-and-packing-problems| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Kaggle
    
.. |gradient-vpsolver-cutting-and-packing-problems| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Gradient
    
.. |sagemaker-vpsolver-cutting-and-packing-problems| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In SageMaker Studio Lab
    


amplpy setup & Quick Start
^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `amplpy setup & Quick Start <notebooks/amplpy-setup-and-quick-start.html>`_
| |github-amplpy-setup-and-quick-start| |colab-amplpy-setup-and-quick-start| |kaggle-amplpy-setup-and-quick-start| |gradient-amplpy-setup-and-quick-start| |sagemaker-amplpy-setup-and-quick-start|
| Description: amplpy setup and quick start
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-amplpy-setup-and-quick-start|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: quickstart.ipynb
    
.. |colab-amplpy-setup-and-quick-start| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In Colab
    
.. |kaggle-amplpy-setup-and-quick-start| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Kaggle
    
.. |gradient-amplpy-setup-and-quick-start| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Gradient
    
.. |sagemaker-amplpy-setup-and-quick-start| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In SageMaker Studio Lab
    


