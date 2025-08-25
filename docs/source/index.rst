
AMPL Model Colaboratory
=======================

AMPL Model Colaboratory is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as **Google Colab**, **Deepnote**, **Kaggle**, **Gradient**, and **AWS SageMaker**.
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

        .. image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
            :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In Deepnote

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open in Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open in Gradient

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
| |github-ampl-solve-multiple-models-in-parallel| |colab-ampl-solve-multiple-models-in-parallel| |deepnote-ampl-solve-multiple-models-in-parallel| |kaggle-ampl-solve-multiple-models-in-parallel| |gradient-ampl-solve-multiple-models-in-parallel| |sagemaker-ampl-solve-multiple-models-in-parallel|
| Description: Solve multiple AMPL models in parallel in Python with amplpy and the multiprocessing modules.
| Tags: :ref:`tag-ampl`, :ref:`tag-python`, :ref:`tag-amplpy`, :ref:`tag-multiprocess`, :ref:`tag-parallel-computing`, :ref:`tag-stochastic-programming`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-ampl-solve-multiple-models-in-parallel|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: multiproc.ipynb
    
.. |colab-ampl-solve-multiple-models-in-parallel| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-solve-multiple-models-in-parallel| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-solve-multiple-models-in-parallel| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-solve-multiple-models-in-parallel| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-solve-multiple-models-in-parallel| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/multiprocessing/multiproc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL - spreadsheet handling with amplxl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL - spreadsheet handling with amplxl <notebooks/ampl-spreadsheet-handling-with-amplxl.html>`_
| |github-ampl-spreadsheet-handling-with-amplxl| |colab-ampl-spreadsheet-handling-with-amplxl| |deepnote-ampl-spreadsheet-handling-with-amplxl| |kaggle-ampl-spreadsheet-handling-with-amplxl| |gradient-ampl-spreadsheet-handling-with-amplxl| |sagemaker-ampl-spreadsheet-handling-with-amplxl|
| Description: Basic example of reading/writing data into/from a .xlsx spreadsheet with amplxl
| Tags: :ref:`tag-ampl`, :ref:`tag-amplxl`, :ref:`tag-spreadsheet`, :ref:`tag-excel`, :ref:`tag-xlsx`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-ampl-spreadsheet-handling-with-amplxl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: amplxl.ipynb
    
.. |colab-ampl-spreadsheet-handling-with-amplxl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-spreadsheet-handling-with-amplxl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-spreadsheet-handling-with-amplxl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-spreadsheet-handling-with-amplxl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-spreadsheet-handling-with-amplxl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/amplxl/amplxl.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Bin Packing Problem with GCG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Bin Packing Problem with GCG <notebooks/ampl-bin-packing-problem-with-gcg.html>`_
| |github-ampl-bin-packing-problem-with-gcg| |colab-ampl-bin-packing-problem-with-gcg| |deepnote-ampl-bin-packing-problem-with-gcg| |kaggle-ampl-bin-packing-problem-with-gcg| |gradient-ampl-bin-packing-problem-with-gcg| |sagemaker-ampl-bin-packing-problem-with-gcg|
| Description: Dantzig-Wolfe decomposition for Bin Packing Problem with GCG
| Tags: :ref:`tag-gcg`, :ref:`tag-bpp`, :ref:`tag-amplpy`, :ref:`tag-dantzig-wolfe-decomposition`, :ref:`tag-branch-price-and-cut`, :ref:`tag-highlights`
| Author: :ref:`email-jurgenlentz26_at_gmail.com` <jurgenlentz26@gmail.com>

.. |github-ampl-bin-packing-problem-with-gcg|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: bpp.ipynb
    
.. |colab-ampl-bin-packing-problem-with-gcg| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-bin-packing-problem-with-gcg| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-bin-packing-problem-with-gcg| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-bin-packing-problem-with-gcg| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-bin-packing-problem-with-gcg| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/bpp.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Capacitated p-Median Problem with GCG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Capacitated p-Median Problem with GCG <notebooks/ampl-capacitated-p-median-problem-with-gcg.html>`_
| |github-ampl-capacitated-p-median-problem-with-gcg| |colab-ampl-capacitated-p-median-problem-with-gcg| |deepnote-ampl-capacitated-p-median-problem-with-gcg| |kaggle-ampl-capacitated-p-median-problem-with-gcg| |gradient-ampl-capacitated-p-median-problem-with-gcg| |sagemaker-ampl-capacitated-p-median-problem-with-gcg|
| Description: Dantzig-Wolfe decomposition for Capacitated p-Median Problem with GCG
| Tags: :ref:`tag-gcg`, :ref:`tag-cpmp`, :ref:`tag-amplpy`, :ref:`tag-dantzig-wolfe-decomposition`, :ref:`tag-branch-price-and-cut`, :ref:`tag-highlights`
| Author: :ref:`email-jurgenlentz26_at_gmail.com` <jurgenlentz26@gmail.com>

.. |github-ampl-capacitated-p-median-problem-with-gcg|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: cpmp.ipynb
    
.. |colab-ampl-capacitated-p-median-problem-with-gcg| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-capacitated-p-median-problem-with-gcg| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-capacitated-p-median-problem-with-gcg| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-capacitated-p-median-problem-with-gcg| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-capacitated-p-median-problem-with-gcg| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/lentz/gcg/cpmp.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Christmas Model created by ChatGPT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Christmas Model created by ChatGPT <notebooks/ampl-christmas-model-created-by-chatgpt.html>`_
| |github-ampl-christmas-model-created-by-chatgpt| |colab-ampl-christmas-model-created-by-chatgpt| |deepnote-ampl-christmas-model-created-by-chatgpt| |kaggle-ampl-christmas-model-created-by-chatgpt| |gradient-ampl-christmas-model-created-by-chatgpt| |sagemaker-ampl-christmas-model-created-by-chatgpt|
| Description: Christmas model generated by ChatGPT
| Tags: :ref:`tag-christmas`, :ref:`tag-chatgpt`, :ref:`tag-amplpy`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-ampl-christmas-model-created-by-chatgpt|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: christmas.ipynb
    
.. |colab-ampl-christmas-model-created-by-chatgpt| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-christmas-model-created-by-chatgpt| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-christmas-model-created-by-chatgpt| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-christmas-model-created-by-chatgpt| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-christmas-model-created-by-chatgpt| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 1/6 -- Capacitated Facility Location Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 1/6 -- Capacitated Facility Location Problem <notebooks/ampl-development-tutorial-16-capacitated-facility-location-problem.html>`_
| |github-ampl-development-tutorial-16-capacitated-facility-location-problem| |colab-ampl-development-tutorial-16-capacitated-facility-location-problem| |deepnote-ampl-development-tutorial-16-capacitated-facility-location-problem| |kaggle-ampl-development-tutorial-16-capacitated-facility-location-problem| |gradient-ampl-development-tutorial-16-capacitated-facility-location-problem| |sagemaker-ampl-development-tutorial-16-capacitated-facility-location-problem|
| Description: This notebook marks the beginning of a six-part series.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-facility-location`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-16-capacitated-facility-location-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: 1_floc.ipynb
    
.. |colab-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-16-capacitated-facility-location-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/1_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 2/6 -- Stochastic Capacitated Facility Location Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 2/6 -- Stochastic Capacitated Facility Location Problem <notebooks/ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem.html>`_
| |github-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |colab-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |deepnote-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |kaggle-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |gradient-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| |sagemaker-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem|
| Description: This notebook continues our six-part series as the second installment.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: 2_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-26-stochastic-capacitated-facility-location-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/2_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 3/6 -- Benders Decomposition via AMPL scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 3/6 -- Benders Decomposition via AMPL scripting <notebooks/ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting.html>`_
| |github-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |colab-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |deepnote-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |kaggle-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |gradient-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| |sagemaker-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting|
| Description: In this third installment of our six-part series, we continue our exploration by addressing the complexities introduced by the stochastic programming formulation presented in part two.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: 3_benders_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-36-benders-decomposition-via-ampl-scripting| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/3_benders_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 4/6 -- Benders Decomposition via PYTHON scripting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 4/6 -- Benders Decomposition via PYTHON scripting <notebooks/ampl-development-tutorial-46-benders-decomposition-via-python-scripting.html>`_
| |github-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |colab-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |deepnote-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |kaggle-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |gradient-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| |sagemaker-ampl-development-tutorial-46-benders-decomposition-via-python-scripting|
| Description: In this fourth installment of our six-part series, we advance our exploration by demonstrating how to adapt our AMPL script for use with AMPL's Python API.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-46-benders-decomposition-via-python-scripting|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: 4_benders_in_python_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-46-benders-decomposition-via-python-scripting| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/4_benders_in_python_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 5/6 -- Parallelizing Subproblem Solves in Benders Decomposition <notebooks/ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition.html>`_
| |github-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |colab-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |deepnote-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |kaggle-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |gradient-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| |sagemaker-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition|
| Description: In the fifth installment of our six-part series, we delve deeper by showing how to evolve our Benders decomposition Python script from a serial execution to one that solves subproblems in parallel.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`, :ref:`tag-decomposition`, :ref:`tag-parallel-solves`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: 5_benders_parallel_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-56-parallelizing-subproblem-solves-in-benders-decomposition| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/5_benders_parallel_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Development Tutorial 6/6 -- Implementing Benders Decomposition with *ampls*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Development Tutorial 6/6 -- Implementing Benders Decomposition with *ampls* <notebooks/ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls.html>`_
| |github-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |colab-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |deepnote-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |kaggle-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |gradient-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| |sagemaker-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls|
| Description: This concluding notebook in our six-part series delves into enhancing the efficiency of our decomposition algorithm by utilizing **AMPL Solver Libraries** (*ampls*).
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-ampls`, :ref:`tag-mip`, :ref:`tag-stochastic`, :ref:`tag-facility-location`, :ref:`tag-benders`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>, :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: 6_benders_ampls_stoch_floc.ipynb
    
.. |colab-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-development-tutorial-66-implementing-benders-decomposition-with-ampls| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/6_benders_ampls_stoch_floc.ipynb
    :alt: Open In SageMaker Studio Lab
    


AMPL Model Colaboratory Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `AMPL Model Colaboratory Template <notebooks/ampl-model-colaboratory-template.html>`_
| |github-ampl-model-colaboratory-template| |colab-ampl-model-colaboratory-template| |deepnote-ampl-model-colaboratory-template| |kaggle-ampl-model-colaboratory-template| |gradient-ampl-model-colaboratory-template| |sagemaker-ampl-model-colaboratory-template|
| Description: Basic notebook template for the AMPL Colab repository
| Tags: :ref:`tag-amplpy`, :ref:`tag-template`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-ampl-model-colaboratory-template|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: colab.ipynb
    
.. |colab-ampl-model-colaboratory-template| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In Colab
    
.. |deepnote-ampl-model-colaboratory-template| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-ampl-model-colaboratory-template| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In Kaggle
    
.. |gradient-ampl-model-colaboratory-template| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-ampl-model-colaboratory-template| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/template/colab.ipynb
    :alt: Open In SageMaker Studio Lab
    


Aircrew trainee scheduling with seniority constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Aircrew trainee scheduling with seniority constraints <notebooks/aircrew-trainee-scheduling-with-seniority-constraints.html>`_
| |github-aircrew-trainee-scheduling-with-seniority-constraints| |colab-aircrew-trainee-scheduling-with-seniority-constraints| |deepnote-aircrew-trainee-scheduling-with-seniority-constraints| |kaggle-aircrew-trainee-scheduling-with-seniority-constraints| |gradient-aircrew-trainee-scheduling-with-seniority-constraints| |sagemaker-aircrew-trainee-scheduling-with-seniority-constraints|
| Description: Aircrew trainee scheduling with simpler seniority modeling
| Tags: :ref:`tag-trainee-scheduling`, :ref:`tag-aircrew-scheduling`, :ref:`tag-employee-scheduling`, :ref:`tag-seniority-constraints`, :ref:`tag-seniority-ranking`, :ref:`tag-preferential-bidding-system`, :ref:`tag-multi-objective`, :ref:`tag-lexicographic-objectives`, :ref:`tag-amplpy`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-aircrew-trainee-scheduling-with-seniority-constraints|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: tip8_aircrew_trainees_seniority.ipynb
    
.. |colab-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In Colab
    
.. |deepnote-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In Kaggle
    
.. |gradient-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-aircrew-trainee-scheduling-with-seniority-constraints| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/modeling-tips/tip8_aircrew_trainees_seniority.ipynb
    :alt: Open In SageMaker Studio Lab
    


Balanced Task Assignment with Inverse Cost Scaling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Balanced Task Assignment with Inverse Cost Scaling <notebooks/balanced-task-assignment-with-inverse-cost-scaling.html>`_
| |github-balanced-task-assignment-with-inverse-cost-scaling| |colab-balanced-task-assignment-with-inverse-cost-scaling| |deepnote-balanced-task-assignment-with-inverse-cost-scaling| |kaggle-balanced-task-assignment-with-inverse-cost-scaling| |gradient-balanced-task-assignment-with-inverse-cost-scaling| |sagemaker-balanced-task-assignment-with-inverse-cost-scaling|
| Tags: :ref:`tag-amplpy`, :ref:`tag-nonlinear`, :ref:`tag-worker-task-assignment`, :ref:`tag-cost-minimization`, :ref:`tag-inverse-cost-scaling`, :ref:`tag-task-scheduling`, :ref:`tag-gurobi`, :ref:`tag-global-optimization`, :ref:`tag-assignment`, :ref:`tag-scheduling`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-balanced-task-assignment-with-inverse-cost-scaling|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Inverse_cost.ipynb
    
.. |colab-balanced-task-assignment-with-inverse-cost-scaling| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Open In Colab
    
.. |deepnote-balanced-task-assignment-with-inverse-cost-scaling| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-balanced-task-assignment-with-inverse-cost-scaling| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Open In Kaggle
    
.. |gradient-balanced-task-assignment-with-inverse-cost-scaling| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-balanced-task-assignment-with-inverse-cost-scaling| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Inverse_cost/Inverse_cost.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: Economic equilibria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: Economic equilibria <notebooks/book-example-economic-equilibria.html>`_
| |github-book-example-economic-equilibria| |colab-book-example-economic-equilibria| |deepnote-book-example-economic-equilibria| |kaggle-book-example-economic-equilibria| |gradient-book-example-economic-equilibria| |sagemaker-book-example-economic-equilibria|
| Description: economic model using complementarity conditions from Chapter 19 AMPL book
| Tags: :ref:`tag-ampl-book`, :ref:`tag-finance`, :ref:`tag-complementarity-problem`, :ref:`tag-cbc`, :ref:`tag-gurobi`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-economic-equilibria|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: economic_eq_lecture.ipynb
    
.. |colab-book-example-economic-equilibria| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-economic-equilibria| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-economic-equilibria| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-economic-equilibria| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-economic-equilibria| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/economic_eq_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: Transshipment problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: Transshipment problem <notebooks/book-example-transshipment-problem.html>`_
| |github-book-example-transshipment-problem| |colab-book-example-transshipment-problem| |deepnote-book-example-transshipment-problem| |kaggle-book-example-transshipment-problem| |gradient-book-example-transshipment-problem| |sagemaker-book-example-transshipment-problem|
| Description: Basic book example with general transshipment model (net1.mod)
| Tags: :ref:`tag-ampl-book`, :ref:`tag-cbc`, :ref:`tag-transportation`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-transshipment-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: net1.ipynb
    
.. |colab-book-example-transshipment-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-transshipment-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-transshipment-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-transshipment-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-transshipment-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/net1.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: diet
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: diet <notebooks/book-example-diet.html>`_
| |github-book-example-diet| |colab-book-example-diet| |deepnote-book-example-diet| |kaggle-book-example-diet| |gradient-book-example-diet| |sagemaker-book-example-diet|
| Description: book example autogenerated using diet.mod, diet.dat, and diet.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-book-example-diet|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: diet.ipynb
    
.. |colab-book-example-diet| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-diet| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-diet| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-diet| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-diet| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/diet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: prod
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: prod <notebooks/book-example-prod.html>`_
| |github-book-example-prod| |colab-book-example-prod| |deepnote-book-example-prod| |kaggle-book-example-prod| |gradient-book-example-prod| |sagemaker-book-example-prod|
| Description: book example autogenerated using prod.mod, prod.dat, and prod.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-prod|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: prod.ipynb
    
.. |colab-book-example-prod| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-prod| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-prod| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-prod| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-prod| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/prod.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: steel
^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: steel <notebooks/book-example-steel.html>`_
| |github-book-example-steel| |colab-book-example-steel| |deepnote-book-example-steel| |kaggle-book-example-steel| |gradient-book-example-steel| |sagemaker-book-example-steel|
| Description: book example autogenerated using steel.mod, steel.dat, and steel.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-steel|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: steel.ipynb
    
.. |colab-book-example-steel| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-steel| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-steel| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-steel| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-steel| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/steel.ipynb
    :alt: Open In SageMaker Studio Lab
    


Book Example: transp
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Book Example: transp <notebooks/book-example-transp.html>`_
| |github-book-example-transp| |colab-book-example-transp| |deepnote-book-example-transp| |kaggle-book-example-transp| |gradient-book-example-transp| |sagemaker-book-example-transp|
| Description: book example autogenerated using transp.mod, transp.dat, and transp.run
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`
| Author: N/A

.. |github-book-example-transp|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: transp.ipynb
    
.. |colab-book-example-transp| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In Colab
    
.. |deepnote-book-example-transp| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-book-example-transp| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In Kaggle
    
.. |gradient-book-example-transp| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-book-example-transp| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/transp.ipynb
    :alt: Open In SageMaker Studio Lab
    


CP-style scheduling model with the *numberof* operator, solved by a MIP solver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `CP-style scheduling model with the *numberof* operator, solved by a MIP solver <notebooks/cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver.html>`_
| |github-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |colab-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |deepnote-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |kaggle-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |gradient-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| |sagemaker-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver|
| Description: Scheduling model with the Constraint Programming *numberof* operator, solved with a MIP solver. New MIP solver drivers based on the [MP library](https://amplmp.readthedocs.io/) enable CP-style modeling.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-constraint-programming`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: sched_numberof.ipynb
    
.. |colab-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In Colab
    
.. |deepnote-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In Kaggle
    
.. |gradient-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-cp-style-scheduling-model-with-the-numberof-operator-solved-by-a-mip-solver| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sched_numberof.ipynb
    :alt: Open In SageMaker Studio Lab
    


Capacity expansion of power generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Capacity expansion of power generation <notebooks/capacity-expansion-of-power-generation.html>`_
| |github-capacity-expansion-of-power-generation| |colab-capacity-expansion-of-power-generation| |deepnote-capacity-expansion-of-power-generation| |kaggle-capacity-expansion-of-power-generation| |gradient-capacity-expansion-of-power-generation| |sagemaker-capacity-expansion-of-power-generation|
| Description: Models the extensive form of a deterministic multi-stage capacity expansion problem. In this model we can have multiple resources of the same type which have identical properties. The model can be further developed into a stochastic one.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-energy`, :ref:`tag-planning`, :ref:`tag-mip`, :ref:`tag-power-generation`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-capacity-expansion-of-power-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: capacity_expansion.ipynb
    
.. |colab-capacity-expansion-of-power-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In Colab
    
.. |deepnote-capacity-expansion-of-power-generation| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-capacity-expansion-of-power-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In Kaggle
    
.. |gradient-capacity-expansion-of-power-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-capacity-expansion-of-power-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/capacity_expansion.ipynb
    :alt: Open In SageMaker Studio Lab
    


Containers scheduling
^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Containers scheduling <notebooks/containers-scheduling.html>`_
| |github-containers-scheduling| |colab-containers-scheduling| |deepnote-containers-scheduling| |kaggle-containers-scheduling| |gradient-containers-scheduling| |sagemaker-containers-scheduling|
| Description: Scheduling model for harbor operations. It is a problem with dependences between containers, which should be dispatch the fastest possible. We are using the MP solver interfaces to model a complex system using techniques from Constraint Programming, such as indicator constraints, and logical or and forall operators. After the model is written, a couple instances are presented and Highs/Gurobi MIP solvers are used to tackle the problem.
| Tags: :ref:`tag-amplpy`, :ref:`tag-scheduling`, :ref:`tag-industry`, :ref:`tag-mip`, :ref:`tag-constraint-programming`, :ref:`tag-mp`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-containers-scheduling|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: containers_scheduling.ipynb
    
.. |colab-containers-scheduling| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In Colab
    
.. |deepnote-containers-scheduling| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-containers-scheduling| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In Kaggle
    
.. |gradient-containers-scheduling| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-containers-scheduling| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/containers_scheduling.ipynb
    :alt: Open In SageMaker Studio Lab
    


Debugging Model Infeasibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Debugging Model Infeasibility <notebooks/debugging-model-infeasibility.html>`_
| |github-debugging-model-infeasibility| |colab-debugging-model-infeasibility| |deepnote-debugging-model-infeasibility| |kaggle-debugging-model-infeasibility| |gradient-debugging-model-infeasibility| |sagemaker-debugging-model-infeasibility|
| Description: This notebook offers a concise guide on troubleshooting model infeasibility using AMPL's presolve feature and other language capabilities.
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-debug`, :ref:`tag-infeasibility`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-debugging-model-infeasibility|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: debug_infeas.ipynb
    
.. |colab-debugging-model-infeasibility| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In Colab
    
.. |deepnote-debugging-model-infeasibility| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-debugging-model-infeasibility| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In Kaggle
    
.. |gradient-debugging-model-infeasibility| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-debugging-model-infeasibility| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/dev/debug_infeas.ipynb
    :alt: Open In SageMaker Studio Lab
    


Demand prediction and Optimization with scikit-learn & Amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Demand prediction and Optimization with scikit-learn & Amplpy <notebooks/demand-prediction-and-optimization-with-scikit-learn-and-amplpy.html>`_
| |github-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| |colab-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| |deepnote-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| |kaggle-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| |gradient-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| |sagemaker-demand-prediction-and-optimization-with-scikit-learn-and-amplpy|
| Description: In this notebook, we will:
| Tags: :ref:`tag-amplpy`, :ref:`tag-machine-learning`, :ref:`tag-scikit-learn`, :ref:`tag-gurobi`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-demand-prediction-and-optimization-with-scikit-learn-and-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: predict_demand_simple.ipynb
    
.. |colab-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: Open In Colab
    
.. |deepnote-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: Open In Kaggle
    
.. |gradient-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-demand-prediction-and-optimization-with-scikit-learn-and-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_demand_simple.ipynb
    :alt: Open In SageMaker Studio Lab
    


Diagnose infeasibility
^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Diagnose infeasibility <notebooks/diagnose-infeasibility.html>`_
| |github-diagnose-infeasibility| |colab-diagnose-infeasibility| |deepnote-diagnose-infeasibility| |kaggle-diagnose-infeasibility| |gradient-diagnose-infeasibility| |sagemaker-diagnose-infeasibility|
| Description: This notebook demonstrates how to deal with infeasible models.
| Tags: :ref:`tag-tutorials`, :ref:`tag-infeasibility`, :ref:`tag-mp`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-diagnose-infeasibility|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: diagnose_infeasibility.ipynb
    
.. |colab-diagnose-infeasibility| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: Open In Colab
    
.. |deepnote-diagnose-infeasibility| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-diagnose-infeasibility| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: Open In Kaggle
    
.. |gradient-diagnose-infeasibility| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-diagnose-infeasibility| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/diagnose_infeasibility.ipynb
    :alt: Open In SageMaker Studio Lab
    


Diet and Other Input Models: Minimizing Costs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Diet and Other Input Models: Minimizing Costs <notebooks/diet-and-other-input-models-minimizing-costs.html>`_
| |github-diet-and-other-input-models-minimizing-costs| |colab-diet-and-other-input-models-minimizing-costs| |deepnote-diet-and-other-input-models-minimizing-costs| |kaggle-diet-and-other-input-models-minimizing-costs| |gradient-diet-and-other-input-models-minimizing-costs| |sagemaker-diet-and-other-input-models-minimizing-costs|
| Description: Diet case study, Chapter 2 from the AMPL book adapted to Python
| Tags: :ref:`tag-amplpy`, :ref:`tag-ampl-lecture`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-diet-and-other-input-models-minimizing-costs|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: diet_case_study.ipynb
    
.. |colab-diet-and-other-input-models-minimizing-costs| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Colab
    
.. |deepnote-diet-and-other-input-models-minimizing-costs| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-diet-and-other-input-models-minimizing-costs| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Kaggle
    
.. |gradient-diet-and-other-input-models-minimizing-costs| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/diet_case_study.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-diet-and-other-input-models-minimizing-costs| image:: https://studiolab.sagemaker.aws/studiolab.svg
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
| |github-dual-donor-organ-exchange-problem| |colab-dual-donor-organ-exchange-problem| |deepnote-dual-donor-organ-exchange-problem| |kaggle-dual-donor-organ-exchange-problem| |gradient-dual-donor-organ-exchange-problem| |sagemaker-dual-donor-organ-exchange-problem|
| Description: Most transplants from living donors require only one donor for each procedure. There are, however, exceptions, including dual-graft liver transplantation, bilateral living-donor lobar lung transplantation, and simultaneous liver-kidney transplantation. For each of these procedures, grafts from two compatible living donors are transplanted. As such, these procedures are more involved from an organizational perspective than those with only one donor. Unfortunately, one or both of the donors can often be biologically incompatible with the intended recipient, precluding the transplantation.
| Tags: :ref:`tag-medicine`, :ref:`tag-organ-exchange`, :ref:`tag-mip`, :ref:`tag-ampl-only`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-dual-donor-organ-exchange-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Dual-Donor_Organ_Exchange.ipynb
    
.. |colab-dual-donor-organ-exchange-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In Colab
    
.. |deepnote-dual-donor-organ-exchange-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-dual-donor-organ-exchange-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In Kaggle
    
.. |gradient-dual-donor-organ-exchange-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-dual-donor-organ-exchange-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Medicine/Dual-Donor_Organ_Exchange.ipynb
    :alt: Open In SageMaker Studio Lab
    


Dynamic routing example
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Dynamic routing example <notebooks/dynamic-routing-example.html>`_
| |github-dynamic-routing-example| |colab-dynamic-routing-example| |deepnote-dynamic-routing-example| |kaggle-dynamic-routing-example| |gradient-dynamic-routing-example| |sagemaker-dynamic-routing-example|
| Description: Example of interactive optimization with GUI using AMPL and Google Maps
| Tags: :ref:`tag-amplpy`, :ref:`tag-gui`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. |github-dynamic-routing-example|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Dynamic_routing_example.ipynb
    
.. |colab-dynamic-routing-example| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In Colab
    
.. |deepnote-dynamic-routing-example| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-dynamic-routing-example| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In Kaggle
    
.. |gradient-dynamic-routing-example| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-dynamic-routing-example| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/Dynamic_routing_example.ipynb
    :alt: Open In SageMaker Studio Lab
    


Efficient Frontier with Google Sheets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Efficient Frontier with Google Sheets <notebooks/efficient-frontier-with-google-sheets.html>`_
| |github-efficient-frontier-with-google-sheets| |colab-efficient-frontier-with-google-sheets|
| Description: Efficient Frontier example using Google Sheets
| Tags: :ref:`tag-amplpy`, :ref:`tag-google-sheets`, :ref:`tag-finance`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. |github-efficient-frontier-with-google-sheets|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/finance/efficient_frontier.ipynb
    :alt: efficient_frontier.ipynb
    
.. |colab-efficient-frontier-with-google-sheets| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/finance/efficient_frontier.ipynb
    :alt: Open In Colab
    


Employee Scheduling Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Employee Scheduling Optimization <notebooks/employee-scheduling-optimization.html>`_
| |github-employee-scheduling-optimization| |colab-employee-scheduling-optimization| |deepnote-employee-scheduling-optimization| |kaggle-employee-scheduling-optimization| |gradient-employee-scheduling-optimization| |sagemaker-employee-scheduling-optimization|
| Description: Employee scheduling model from the Analytical Decision Modeling course at the Arizona State University.
| Tags: :ref:`tag-educational`, :ref:`tag-mip`, :ref:`tag-scheduling`, :ref:`tag-amplpy`, :ref:`tag-gurobi`, :ref:`tag-highs`
| Author: :ref:`email-yimin_wang_at_asu.edu` <yimin_wang@asu.edu>, :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-employee-scheduling-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Employee_Scheduling.ipynb
    
.. |colab-employee-scheduling-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In Colab
    
.. |deepnote-employee-scheduling-optimization| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-employee-scheduling-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In Kaggle
    
.. |gradient-employee-scheduling-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-employee-scheduling-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/Employee_Scheduling.ipynb
    :alt: Open In SageMaker Studio Lab
    


Enhanced Sector ETF Portfolio Optimization with Multiple Strategies in Python with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Enhanced Sector ETF Portfolio Optimization with Multiple Strategies in Python with AMPL <notebooks/enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl.html>`_
| |github-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| |colab-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| |deepnote-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| |kaggle-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| |gradient-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| |sagemaker-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl|
| Description: This notebook compares multiple portfolio optimization strategies for invesment in Sector ETFs
| Tags: :ref:`tag-finance`, :ref:`tag-portfolio-optimization`
| Author: :ref:`email-mukesh96official_at_gmail.com` <mukesh96official@gmail.com>

.. |github-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    
.. |colab-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Open In Colab
    
.. |deepnote-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Open In Kaggle
    
.. |gradient-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-enhanced-sector-etf-portfolio-optimization-with-multiple-strategies-in-python-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_3_Porfolio_Optimization_Sector_ETF.ipynb
    :alt: Open In SageMaker Studio Lab
    


Financial Portfolio Optimization with amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Financial Portfolio Optimization with amplpy <notebooks/financial-portfolio-optimization-with-amplpy.html>`_
| |github-financial-portfolio-optimization-with-amplpy| |colab-financial-portfolio-optimization-with-amplpy| |deepnote-financial-portfolio-optimization-with-amplpy| |kaggle-financial-portfolio-optimization-with-amplpy| |gradient-financial-portfolio-optimization-with-amplpy| |sagemaker-financial-portfolio-optimization-with-amplpy|
| Description: Financial Portfolio Optimization with amplpy and amplpyfinance
| Tags: :ref:`tag-amplpy`, :ref:`tag-amplpyfinance`, :ref:`tag-finance`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-financial-portfolio-optimization-with-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: amplpyfinance_vs_amplpy.ipynb
    
.. |colab-financial-portfolio-optimization-with-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Colab
    
.. |deepnote-financial-portfolio-optimization-with-amplpy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-financial-portfolio-optimization-with-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Kaggle
    
.. |gradient-financial-portfolio-optimization-with-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-financial-portfolio-optimization-with-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/amplpyfinance/amplpyfinance_vs_amplpy.ipynb
    :alt: Open In SageMaker Studio Lab
    


Google Hashcode 2022
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Google Hashcode 2022 <notebooks/google-hashcode-2022.html>`_
| |github-google-hashcode-2022| |colab-google-hashcode-2022| |deepnote-google-hashcode-2022| |kaggle-google-hashcode-2022| |gradient-google-hashcode-2022| |sagemaker-google-hashcode-2022|
| Description: Google Hashcode 2022 Practice Problem
| Tags: :ref:`tag-amplpy`, :ref:`tag-heuristics`, :ref:`tag-engineering`, :ref:`tag-scheduling`, :ref:`tag-complexity`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-google-hashcode-2022|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: practice_problem.ipynb
    
.. |colab-google-hashcode-2022| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In Colab
    
.. |deepnote-google-hashcode-2022| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-google-hashcode-2022| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In Kaggle
    
.. |gradient-google-hashcode-2022| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-google-hashcode-2022| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/hashcode/practice_problem.ipynb
    :alt: Open In SageMaker Studio Lab
    


Hospitals-Residents MIP
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Hospitals-Residents MIP <notebooks/hospitals-residents-mip.html>`_
| |github-hospitals-residents-mip| |colab-hospitals-residents-mip| |deepnote-hospitals-residents-mip| |kaggle-hospitals-residents-mip| |gradient-hospitals-residents-mip| |sagemaker-hospitals-residents-mip|
| Description: hospitals-residents problem with ties problem solved with ampl and highs
| Tags: :ref:`tag-amplpy`, :ref:`tag-assignment`, :ref:`tag-mip`, :ref:`tag-data-structures`, :ref:`tag-graphs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-hospitals-residents-mip|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: hospitals_residents.ipynb
    
.. |colab-hospitals-residents-mip| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Colab
    
.. |deepnote-hospitals-residents-mip| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-hospitals-residents-mip| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Kaggle
    
.. |gradient-hospitals-residents-mip| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-hospitals-residents-mip| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/hospitals_residents.ipynb
    :alt: Open In SageMaker Studio Lab
    


Hydrothermal Scheduling Problem with Conic Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Hydrothermal Scheduling Problem with Conic Programming <notebooks/hydrothermal-scheduling-problem-with-conic-programming.html>`_
| |github-hydrothermal-scheduling-problem-with-conic-programming| |colab-hydrothermal-scheduling-problem-with-conic-programming| |deepnote-hydrothermal-scheduling-problem-with-conic-programming| |kaggle-hydrothermal-scheduling-problem-with-conic-programming| |gradient-hydrothermal-scheduling-problem-with-conic-programming| |sagemaker-hydrothermal-scheduling-problem-with-conic-programming|
| Description: Hydrothermal Scheduling Problem using Second-Order Cones
| Tags: :ref:`tag-amplpy`, :ref:`tag-conic`, :ref:`tag-second-order-cone`, :ref:`tag-quadratic-cone`, :ref:`tag-nonlinear-programming`, :ref:`tag-scheduling`, :ref:`tag-engineering`, :ref:`tag-power-generation`, :ref:`tag-geothermal-energy`, :ref:`tag-hydropower`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-hydrothermal-scheduling-problem-with-conic-programming|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: hydrothermal.ipynb
    
.. |colab-hydrothermal-scheduling-problem-with-conic-programming| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In Colab
    
.. |deepnote-hydrothermal-scheduling-problem-with-conic-programming| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-hydrothermal-scheduling-problem-with-conic-programming| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In Kaggle
    
.. |gradient-hydrothermal-scheduling-problem-with-conic-programming| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-hydrothermal-scheduling-problem-with-conic-programming| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/hydrothermal.ipynb
    :alt: Open In SageMaker Studio Lab
    


Identifying active constraints with Ampl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Identifying active constraints with Ampl <notebooks/identifying-active-constraints-with-ampl.html>`_
| |github-identifying-active-constraints-with-ampl| |colab-identifying-active-constraints-with-ampl| |deepnote-identifying-active-constraints-with-ampl| |kaggle-identifying-active-constraints-with-ampl| |gradient-identifying-active-constraints-with-ampl| |sagemaker-identifying-active-constraints-with-ampl|
| Description: This notebook demonstrates how to inspect the status of constraints in an AMPL model using the astatus() method provided by amplpy. It shows how to identify which constraints are currently active (i.e., participating in the optimization) and filter out those that have been dropped, presolved, or otherwise excluded
| Tags: :ref:`tag-tutorials`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-identifying-active-constraints-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: identify_active_constraints.ipynb
    
.. |colab-identifying-active-constraints-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: Open In Colab
    
.. |deepnote-identifying-active-constraints-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-identifying-active-constraints-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: Open In Kaggle
    
.. |gradient-identifying-active-constraints-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-identifying-active-constraints-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/identify_active_constraints.ipynb
    :alt: Open In SageMaker Studio Lab
    


Introduction to Linear and Integer Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Introduction to Linear and Integer Programming <notebooks/introduction-to-linear-and-integer-programming.html>`_
| |github-introduction-to-linear-and-integer-programming| |colab-introduction-to-linear-and-integer-programming| |deepnote-introduction-to-linear-and-integer-programming| |kaggle-introduction-to-linear-and-integer-programming| |gradient-introduction-to-linear-and-integer-programming| |sagemaker-introduction-to-linear-and-integer-programming|
| Description: Basic introduction to linear programming and AMPL via a lemonade stand example
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-lemonade-stand`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-introduction-to-linear-and-integer-programming|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: intro_to_linear_programming.ipynb
    
.. |colab-introduction-to-linear-and-integer-programming| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: Open In Colab
    
.. |deepnote-introduction-to-linear-and-integer-programming| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-introduction-to-linear-and-integer-programming| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: Open In Kaggle
    
.. |gradient-introduction-to-linear-and-integer-programming| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-introduction-to-linear-and-integer-programming| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_linear_programming.ipynb
    :alt: Open In SageMaker Studio Lab
    


Introduction to Mathematical Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Introduction to Mathematical Optimization <notebooks/introduction-to-mathematical-optimization.html>`_
| |github-introduction-to-mathematical-optimization| |colab-introduction-to-mathematical-optimization| |deepnote-introduction-to-mathematical-optimization| |kaggle-introduction-to-mathematical-optimization| |gradient-introduction-to-mathematical-optimization| |sagemaker-introduction-to-mathematical-optimization|
| Description: Basic introduction to optimization and AMPL via unconstrained optimization
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-optimization`, :ref:`tag-convexity`, :ref:`tag-unconstrained`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-introduction-to-mathematical-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: intro_to_optimization.ipynb
    
.. |colab-introduction-to-mathematical-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In Colab
    
.. |deepnote-introduction-to-mathematical-optimization| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-introduction-to-mathematical-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In Kaggle
    
.. |gradient-introduction-to-mathematical-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-introduction-to-mathematical-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/intro_to_optimization.ipynb
    :alt: Open In SageMaker Studio Lab
    


Jupyter Notebook Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Jupyter Notebook Integration <notebooks/jupyter-notebook-integration.html>`_
| |github-jupyter-notebook-integration| |colab-jupyter-notebook-integration| |deepnote-jupyter-notebook-integration| |kaggle-jupyter-notebook-integration| |gradient-jupyter-notebook-integration| |sagemaker-jupyter-notebook-integration|
| Description: Jupyter Notebook Integration with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-jupyter-notebook-integration|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: magics.ipynb
    
.. |colab-jupyter-notebook-integration| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In Colab
    
.. |deepnote-jupyter-notebook-integration| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-jupyter-notebook-integration| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In Kaggle
    
.. |gradient-jupyter-notebook-integration| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-jupyter-notebook-integration| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/magics.ipynb
    :alt: Open In SageMaker Studio Lab
    


Labs scheduling
^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Labs scheduling <notebooks/labs-scheduling.html>`_
| |github-labs-scheduling| |colab-labs-scheduling| |deepnote-labs-scheduling| |kaggle-labs-scheduling| |gradient-labs-scheduling| |sagemaker-labs-scheduling|
| Description: Model for laboratories scheduling. Some labs are needed to handle requests from researchers, and departments have to assign labs and locations to the requests.
| Tags: :ref:`tag-facility-location`, :ref:`tag-highs`, :ref:`tag-mip`, :ref:`tag-mixed-integer-linear`, :ref:`tag-scheduling`, :ref:`tag-multi-objective`, :ref:`tag-lexicographic-objectives`, :ref:`tag-mp`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-labs-scheduling|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: labs_scheduling.ipynb
    
.. |colab-labs-scheduling| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: Open In Colab
    
.. |deepnote-labs-scheduling| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-labs-scheduling| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: Open In Kaggle
    
.. |gradient-labs-scheduling| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-labs-scheduling| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/scheduling/labs_scheduling.ipynb
    :alt: Open In SageMaker Studio Lab
    


Largest small polygon
^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Largest small polygon <notebooks/largest-small-polygon.html>`_
| |github-largest-small-polygon| |colab-largest-small-polygon| |deepnote-largest-small-polygon| |kaggle-largest-small-polygon| |gradient-largest-small-polygon| |sagemaker-largest-small-polygon|
| Description: lecture about models for the Largest Small Polygon Problem
| Tags: :ref:`tag-geometry`, :ref:`tag-non-linear`, :ref:`tag-amplpy`, :ref:`tag-ipopt`, :ref:`tag-educational`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-largest-small-polygon|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: largest_small_polygon.ipynb
    
.. |colab-largest-small-polygon| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In Colab
    
.. |deepnote-largest-small-polygon| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-largest-small-polygon| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In Kaggle
    
.. |gradient-largest-small-polygon| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-largest-small-polygon| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/geometry/largest_small_polygon.ipynb
    :alt: Open In SageMaker Studio Lab
    


Logistic Regression with amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Logistic Regression with amplpy <notebooks/logistic-regression-with-amplpy.html>`_
| |github-logistic-regression-with-amplpy| |colab-logistic-regression-with-amplpy| |deepnote-logistic-regression-with-amplpy| |kaggle-logistic-regression-with-amplpy| |gradient-logistic-regression-with-amplpy| |sagemaker-logistic-regression-with-amplpy|
| Description: Logistic regression with amplpy using exponential cones
| Tags: :ref:`tag-highlights`, :ref:`tag-amplpy`, :ref:`tag-regression`, :ref:`tag-sigmoid`, :ref:`tag-softplus`, :ref:`tag-log-sum-exp`, :ref:`tag-classifier`, :ref:`tag-regularization`, :ref:`tag-machine-learning`, :ref:`tag-conic`, :ref:`tag-exponential-cone`, :ref:`tag-second-order-cone`, :ref:`tag-quadratic-cone`, :ref:`tag-formulation-comparison`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>, :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-logistic-regression-with-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: logistic_regression.ipynb
    
.. |colab-logistic-regression-with-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In Colab
    
.. |deepnote-logistic-regression-with-amplpy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-logistic-regression-with-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In Kaggle
    
.. |gradient-logistic-regression-with-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-logistic-regression-with-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/conic/logistic_regression.ipynb
    :alt: Open In SageMaker Studio Lab
    


Magic sequences
^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Magic sequences <notebooks/magic-sequences.html>`_
| |github-magic-sequences| |colab-magic-sequences| |deepnote-magic-sequences| |kaggle-magic-sequences| |gradient-magic-sequences| |sagemaker-magic-sequences|
| Description: Solving magic sequences through reinforced formulations and constrained programming. Some comparison between models and solvers is done, and we look into the "Another solution" problem for these sequences.
| Tags: :ref:`tag-constraint-programming`, :ref:`tag-educational`, :ref:`tag-mp`, :ref:`tag-sequences`, :ref:`tag-arithmetic`, :ref:`tag-reinforced-formulations`, :ref:`tag-highs`, :ref:`tag-gecode`, :ref:`tag-cbc`, :ref:`tag-mip`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-magic-sequences|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: magic_sequences.ipynb
    
.. |colab-magic-sequences| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In Colab
    
.. |deepnote-magic-sequences| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-magic-sequences| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In Kaggle
    
.. |gradient-magic-sequences| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-magic-sequences| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/magic_sequences.ipynb
    :alt: Open In SageMaker Studio Lab
    


Multi-Objective Knapsack Problem with AMPLPY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Multi-Objective Knapsack Problem with AMPLPY <notebooks/multi-objective-knapsack-problem-with-amplpy.html>`_
| |github-multi-objective-knapsack-problem-with-amplpy| |colab-multi-objective-knapsack-problem-with-amplpy| |deepnote-multi-objective-knapsack-problem-with-amplpy| |kaggle-multi-objective-knapsack-problem-with-amplpy| |gradient-multi-objective-knapsack-problem-with-amplpy| |sagemaker-multi-objective-knapsack-problem-with-amplpy|
| Description: knapsack problem using multiple objectives, setting objective-specific options
| Tags: :ref:`tag-multi-objective`, :ref:`tag-multi-objective-options`, :ref:`tag-lexicographic-objectives`, :ref:`tag-knapsack`, :ref:`tag-amplpy`, :ref:`tag-highlights`
| Author: :ref:`email-jurgenlentz26_at_gmail.com` <jurgenlentz26@gmail.com>

.. |github-multi-objective-knapsack-problem-with-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: knapsack.ipynb
    
.. |colab-multi-objective-knapsack-problem-with-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: Open In Colab
    
.. |deepnote-multi-objective-knapsack-problem-with-amplpy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-multi-objective-knapsack-problem-with-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: Open In Kaggle
    
.. |gradient-multi-objective-knapsack-problem-with-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-multi-objective-knapsack-problem-with-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/lentz/multiobj/knapsack.ipynb
    :alt: Open In SageMaker Studio Lab
    


Multicommodity transportation problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Multicommodity transportation problem <notebooks/multicommodity-transportation-problem.html>`_
| |github-multicommodity-transportation-problem| |colab-multicommodity-transportation-problem| |deepnote-multicommodity-transportation-problem| |kaggle-multicommodity-transportation-problem| |gradient-multicommodity-transportation-problem| |sagemaker-multicommodity-transportation-problem|
| Description: Multicommodity transportation model with binary variables
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-mixed-integer-linear`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-multicommodity-transportation-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: multmip1.ipynb
    
.. |colab-multicommodity-transportation-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Colab
    
.. |deepnote-multicommodity-transportation-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-multicommodity-transportation-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Kaggle
    
.. |gradient-multicommodity-transportation-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-multicommodity-transportation-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/multmip1.ipynb
    :alt: Open In SageMaker Studio Lab
    


N-Queens
^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `N-Queens <notebooks/n-queens.html>`_
| |github-n-queens| |colab-n-queens| |deepnote-n-queens| |kaggle-n-queens| |gradient-n-queens| |sagemaker-n-queens|
| Description: How can N queens be placed on an NxN chessboard so that no two of them attack each other?
| Tags: :ref:`tag-amplpy`, :ref:`tag-constraint-programming`, :ref:`tag-highlights`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-n-queens|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: nqueens.ipynb
    
.. |colab-n-queens| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In Colab
    
.. |deepnote-n-queens| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-n-queens| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In Kaggle
    
.. |gradient-n-queens| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-n-queens| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb
    :alt: Open In SageMaker Studio Lab
    


NFL Team Rating
^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `NFL Team Rating <notebooks/nfl-team-rating.html>`_
| |github-nfl-team-rating| |colab-nfl-team-rating| |deepnote-nfl-team-rating| |kaggle-nfl-team-rating| |gradient-nfl-team-rating| |sagemaker-nfl-team-rating|
| Description: NFL Team Rating problem from the Analytical Decision Modeling course at the Arizona State University.
| Tags: :ref:`tag-educational`, :ref:`tag-quadratic`, :ref:`tag-amplpy`, :ref:`tag-gurobi`
| Author: :ref:`email-yimin_wang_at_asu.edu` <yimin_wang@asu.edu>, :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nfl-team-rating|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: NFL_Team_Rating.ipynb
    
.. |colab-nfl-team-rating| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In Colab
    
.. |deepnote-nfl-team-rating| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-nfl-team-rating| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In Kaggle
    
.. |gradient-nfl-team-rating| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-nfl-team-rating| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/educational/NFL_Team_Rating.ipynb
    :alt: Open In SageMaker Studio Lab
    


Network Linear Programs
^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Network Linear Programs <notebooks/network-linear-programs.html>`_
| |github-network-linear-programs| |colab-network-linear-programs| |deepnote-network-linear-programs| |kaggle-network-linear-programs| |gradient-network-linear-programs| |sagemaker-network-linear-programs|
| Description: Basic introduction to network linear programms and AMPL via max flow and shortest path problems
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-max-flow`, :ref:`tag-shortest-path`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-network-linear-programs|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: network.ipynb
    
.. |colab-network-linear-programs| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In Colab
    
.. |deepnote-network-linear-programs| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-network-linear-programs| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In Kaggle
    
.. |gradient-network-linear-programs| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-network-linear-programs| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/network.ipynb
    :alt: Open In SageMaker Studio Lab
    


Network design with redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Network design with redundancy <notebooks/network-design-with-redundancy.html>`_
| |github-network-design-with-redundancy| |colab-network-design-with-redundancy| |deepnote-network-design-with-redundancy| |kaggle-network-design-with-redundancy| |gradient-network-design-with-redundancy| |sagemaker-network-design-with-redundancy|
| Description: Design of an electricity transportation network provides enough redundancy, so that a break of one component does not prevent any user from receiving electricity. The approach also works for similar distribution networks and can potentially be used in the design of military logistic networks.
| Tags: :ref:`tag-electric-grid`, :ref:`tag-military`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-network-design-with-redundancy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: electric_grid_with_redundancy.ipynb
    
.. |colab-network-design-with-redundancy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Colab
    
.. |deepnote-network-design-with-redundancy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-network-design-with-redundancy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Kaggle
    
.. |gradient-network-design-with-redundancy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-network-design-with-redundancy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/military/electric_grid_with_redundancy.ipynb
    :alt: Open In SageMaker Studio Lab
    


Nonlinear transportation model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Nonlinear transportation model <notebooks/nonlinear-transportation-model.html>`_
| |github-nonlinear-transportation-model| |colab-nonlinear-transportation-model| |deepnote-nonlinear-transportation-model| |kaggle-nonlinear-transportation-model| |gradient-nonlinear-transportation-model| |sagemaker-nonlinear-transportation-model|
| Description: Nonlinear transportation problem with Amplpy nltransd.mod, nltrans.dat, and nltrans.run
| Tags: :ref:`tag-ampl-book`, :ref:`tag-nonlinear`, :ref:`tag-ipopt`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nonlinear-transportation-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: nltrans_lecture.ipynb
    
.. |colab-nonlinear-transportation-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Colab
    
.. |deepnote-nonlinear-transportation-model| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-nonlinear-transportation-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Kaggle
    
.. |gradient-nonlinear-transportation-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-nonlinear-transportation-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/nltrans_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Nonlinear transportation problem example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Nonlinear transportation problem example <notebooks/nonlinear-transportation-problem-example.html>`_
| |github-nonlinear-transportation-problem-example| |colab-nonlinear-transportation-problem-example| |deepnote-nonlinear-transportation-problem-example| |kaggle-nonlinear-transportation-problem-example| |gradient-nonlinear-transportation-problem-example| |sagemaker-nonlinear-transportation-problem-example|
| Description: book example autogenerated using nltransd.mod, nltrans.dat, and nltrans.run
| Tags: :ref:`tag-ampl-book`, :ref:`tag-nonlinear`, :ref:`tag-ipopt`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-nonlinear-transportation-problem-example|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: nltrans.ipynb
    
.. |colab-nonlinear-transportation-problem-example| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Colab
    
.. |deepnote-nonlinear-transportation-problem-example| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-nonlinear-transportation-problem-example| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Kaggle
    
.. |gradient-nonlinear-transportation-problem-example| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-nonlinear-transportation-problem-example| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/nltrans.ipynb
    :alt: Open In SageMaker Studio Lab
    


Oil refinery production optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Oil refinery production optimization <notebooks/oil-refinery-production-optimization.html>`_
| |github-oil-refinery-production-optimization| |colab-oil-refinery-production-optimization| |deepnote-oil-refinery-production-optimization| |kaggle-oil-refinery-production-optimization| |gradient-oil-refinery-production-optimization| |sagemaker-oil-refinery-production-optimization|
| Description: In this document, we present an enhanced approach to oil refining optimization for improved decision-making.
| Tags: :ref:`tag-oil-production`, :ref:`tag-production-optimization`, :ref:`tag-profitability`, :ref:`tag-refinery`, :ref:`tag-mip`, :ref:`tag-highs`, :ref:`tag-industry`, :ref:`tag-json`, :ref:`tag-spreadsheet`, :ref:`tag-excel`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-oil-refinery-production-optimization|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: oil_refining.ipynb
    
.. |colab-oil-refinery-production-optimization| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In Colab
    
.. |deepnote-oil-refinery-production-optimization| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-oil-refinery-production-optimization| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In Kaggle
    
.. |gradient-oil-refinery-production-optimization| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-oil-refinery-production-optimization| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb
    :alt: Open In SageMaker Studio Lab
    


Oil refinery production optimization (+PowerBI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Oil refinery production optimization (+PowerBI) <notebooks/oil-refinery-production-optimization-powerbi.html>`_
| |github-oil-refinery-production-optimization-powerbi| |colab-oil-refinery-production-optimization-powerbi|
| Description: In this document, we present an enhanced approach to oil refining optimization by integrating Power BI for improved decision-making and data visualization. For a full description of the model, you can read more about it [here](https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining.ipynb).
| Tags: :ref:`tag-oil-production`, :ref:`tag-production-optimization`, :ref:`tag-profitability`, :ref:`tag-refinery`, :ref:`tag-mip`, :ref:`tag-highs`, :ref:`tag-powerbi`, :ref:`tag-industry`, :ref:`tag-scheduling`, :ref:`tag-data-science`, :ref:`tag-data-analysis`, :ref:`tag-decision-making`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-oil-refinery-production-optimization-powerbi|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_powerbi.ipynb
    :alt: oil_refining_powerbi.ipynb
    
.. |colab-oil-refinery-production-optimization-powerbi| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_powerbi.ipynb
    :alt: Open In Colab
    


Oil refinery production optimization (ampl-only version)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Oil refinery production optimization (ampl-only version) <notebooks/oil-refinery-production-optimization-ampl-only-version.html>`_
| |github-oil-refinery-production-optimization-ampl-only-version| |colab-oil-refinery-production-optimization-ampl-only-version| |deepnote-oil-refinery-production-optimization-ampl-only-version| |kaggle-oil-refinery-production-optimization-ampl-only-version| |gradient-oil-refinery-production-optimization-ampl-only-version| |sagemaker-oil-refinery-production-optimization-ampl-only-version|
| Description: In this document, we present an enhanced approach to oil refining optimization for improved decision-making.
| Tags: :ref:`tag-oil-production`, :ref:`tag-production-optimization`, :ref:`tag-profitability`, :ref:`tag-refinery`, :ref:`tag-mip`, :ref:`tag-ampl-only`, :ref:`tag-highs`, :ref:`tag-industry`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-oil-refinery-production-optimization-ampl-only-version|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: oil_refining_ampl_only.ipynb
    
.. |colab-oil-refinery-production-optimization-ampl-only-version| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: Open In Colab
    
.. |deepnote-oil-refinery-production-optimization-ampl-only-version| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-oil-refinery-production-optimization-ampl-only-version| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: Open In Kaggle
    
.. |gradient-oil-refinery-production-optimization-ampl-only-version| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-oil-refinery-production-optimization-ampl-only-version| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Petroleum_refining/oil_refining_ampl_only.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimal Power Flow with AMPL and Python - Bus Injection Model (BIM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimal Power Flow with AMPL and Python - Bus Injection Model (BIM) <notebooks/optimal-power-flow-with-ampl-and-python-bus-injection-model-bim.html>`_
| |github-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| |colab-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| |deepnote-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| |kaggle-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| |gradient-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| |sagemaker-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim|
| Description: Optimal Power Flow
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-optimal-power-flow`, :ref:`tag-python`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: opf2.ipynb
    
.. |colab-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf2.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimal Power Flow with AMPL and Python - Bus Injection Model (BIM) with controllable-phase shifting transformers and tap-changing transformers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimal Power Flow with AMPL and Python - Bus Injection Model (BIM) with controllable-phase shifting transformers and tap-changing transformers <notebooks/optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers.html>`_
| |github-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| |colab-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| |deepnote-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| |kaggle-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| |gradient-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| |sagemaker-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers|
| Description: Optimal Power Flow
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-optimal-power-flow`, :ref:`tag-python`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: opf4.ipynb
    
.. |colab-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimal-power-flow-with-ampl-and-python-bus-injection-model-bim-with-controllable-phase-shifting-transformers-and-tap-changing-transformers| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf4.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimal Power Flow with AMPL and Python - DC Power Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimal Power Flow with AMPL and Python - DC Power Flow <notebooks/optimal-power-flow-with-ampl-and-python-dc-power-flow.html>`_
| |github-optimal-power-flow-with-ampl-and-python-dc-power-flow| |colab-optimal-power-flow-with-ampl-and-python-dc-power-flow| |deepnote-optimal-power-flow-with-ampl-and-python-dc-power-flow| |kaggle-optimal-power-flow-with-ampl-and-python-dc-power-flow| |gradient-optimal-power-flow-with-ampl-and-python-dc-power-flow| |sagemaker-optimal-power-flow-with-ampl-and-python-dc-power-flow|
| Description: Optimal Power Flow
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-optimal-power-flow`, :ref:`tag-python`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-optimal-power-flow-with-ampl-and-python-dc-power-flow|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: opf3.ipynb
    
.. |colab-optimal-power-flow-with-ampl-and-python-dc-power-flow| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimal-power-flow-with-ampl-and-python-dc-power-flow| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimal-power-flow-with-ampl-and-python-dc-power-flow| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimal-power-flow-with-ampl-and-python-dc-power-flow| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimal-power-flow-with-ampl-and-python-dc-power-flow| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf3.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimal Power Flow with AMPL and Python - conventional Power Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimal Power Flow with AMPL and Python - conventional Power Flow <notebooks/optimal-power-flow-with-ampl-and-python-conventional-power-flow.html>`_
| |github-optimal-power-flow-with-ampl-and-python-conventional-power-flow| |colab-optimal-power-flow-with-ampl-and-python-conventional-power-flow| |deepnote-optimal-power-flow-with-ampl-and-python-conventional-power-flow| |kaggle-optimal-power-flow-with-ampl-and-python-conventional-power-flow| |gradient-optimal-power-flow-with-ampl-and-python-conventional-power-flow| |sagemaker-optimal-power-flow-with-ampl-and-python-conventional-power-flow|
| Description: Optimal Power Flow
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-optimal-power-flow`, :ref:`tag-python`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-optimal-power-flow-with-ampl-and-python-conventional-power-flow|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: opf1.ipynb
    
.. |colab-optimal-power-flow-with-ampl-and-python-conventional-power-flow| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimal-power-flow-with-ampl-and-python-conventional-power-flow| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimal-power-flow-with-ampl-and-python-conventional-power-flow| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimal-power-flow-with-ampl-and-python-conventional-power-flow| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimal-power-flow-with-ampl-and-python-conventional-power-flow| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf1.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimal Power Flow with AMPL and Python - data management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimal Power Flow with AMPL and Python - data management <notebooks/optimal-power-flow-with-ampl-and-python-data-management.html>`_
| |github-optimal-power-flow-with-ampl-and-python-data-management| |colab-optimal-power-flow-with-ampl-and-python-data-management| |deepnote-optimal-power-flow-with-ampl-and-python-data-management| |kaggle-optimal-power-flow-with-ampl-and-python-data-management| |gradient-optimal-power-flow-with-ampl-and-python-data-management| |sagemaker-optimal-power-flow-with-ampl-and-python-data-management|
| Description: Optimal Power Flow with AMPL, Python and amplpy
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-optimal-power-flow`, :ref:`tag-python`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-optimal-power-flow-with-ampl-and-python-data-management|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: opf0.ipynb
    
.. |colab-optimal-power-flow-with-ampl-and-python-data-management| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimal-power-flow-with-ampl-and-python-data-management| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimal-power-flow-with-ampl-and-python-data-management| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimal-power-flow-with-ampl-and-python-data-management| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimal-power-flow-with-ampl-and-python-data-management| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/opf/opf0.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization Methods in Finance: Chapter 3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization Methods in Finance: Chapter 3 <notebooks/optimization-methods-in-finance-chapter-3.html>`_
| |github-optimization-methods-in-finance-chapter-3| |colab-optimization-methods-in-finance-chapter-3| |deepnote-optimization-methods-in-finance-chapter-3| |kaggle-optimization-methods-in-finance-chapter-3| |gradient-optimization-methods-in-finance-chapter-3| |sagemaker-optimization-methods-in-finance-chapter-3|
| Description: Optimization Methods in Finance: Bond Dedication Problem.
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`, :ref:`tag-finance`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-optimization-methods-in-finance-chapter-3|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: finance_opt_example_3_1.ipynb
    
.. |colab-optimization-methods-in-finance-chapter-3| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimization-methods-in-finance-chapter-3| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimization-methods-in-finance-chapter-3| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimization-methods-in-finance-chapter-3| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimization-methods-in-finance-chapter-3| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/finance/finance_opt_example_3_1.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization of Reinforced Concrete Production and Shipment: A Conveyor-Based Manufacturing and Curing Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization of Reinforced Concrete Production and Shipment: A Conveyor-Based Manufacturing and Curing Model <notebooks/optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model.html>`_
| |github-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| |colab-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| |deepnote-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| |kaggle-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| |gradient-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| |sagemaker-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model|
| Tags: :ref:`tag-conveyor-based-manufacturing`, :ref:`tag-concrete-production`, :ref:`tag-mip`, :ref:`tag-ampl`, :ref:`tag-gilmore-gomory`, :ref:`tag-cbc`, :ref:`tag-cutting-stock`, :ref:`tag-decomposition`, :ref:`tag-industry`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Conveyor_curing.ipynb
    
.. |colab-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimization-of-reinforced-concrete-production-and-shipment-a-conveyor-based-manufacturing-and-curing-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Concrete_plant/Conveyor_curing.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization of an TV advertising campaign based on TRP, GRP indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization of an TV advertising campaign based on TRP, GRP indicators <notebooks/optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators.html>`_
| |github-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |colab-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |deepnote-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |kaggle-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |gradient-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| |sagemaker-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators|
| Description: The modern world is unthinkable without advertising. Advertising is the engine of progress.
| Tags: :ref:`tag-marketing`, :ref:`tag-advertisement`, :ref:`tag-deterministic-model`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: TV_Advertisement_campaign_GRP_TRP.ipynb
    
.. |colab-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimization-of-an-tv-advertising-campaign-based-on-trp-grp-indicators| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/TV_Advertisement_campaign_GRP_TRP.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimization of an advertising campaign for launching a new product on the market
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimization of an advertising campaign for launching a new product on the market <notebooks/optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market.html>`_
| |github-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |colab-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |deepnote-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |kaggle-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |gradient-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| |sagemaker-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market|
| Description: The modern world is unthinkable without advertising. Advertising is the engine of progress.
| Tags: :ref:`tag-marketing`, :ref:`tag-advertisement`, :ref:`tag-deterministic-model`, :ref:`tag-piecewise-linear`, :ref:`tag-mip`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Advertising_campaign_colab.ipynb
    
.. |colab-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimization-of-an-advertising-campaign-for-launching-a-new-product-on-the-market| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Advertisement/Advertising_campaign_colab.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimize your Christmas Tree to Global Optimality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimize your Christmas Tree to Global Optimality <notebooks/optimize-your-christmas-tree-to-global-optimality.html>`_
| |github-optimize-your-christmas-tree-to-global-optimality| |colab-optimize-your-christmas-tree-to-global-optimality| |deepnote-optimize-your-christmas-tree-to-global-optimality| |kaggle-optimize-your-christmas-tree-to-global-optimality| |gradient-optimize-your-christmas-tree-to-global-optimality| |sagemaker-optimize-your-christmas-tree-to-global-optimality|
| Description: Optimize the placement of ornaments on a christmas tree.
| Tags: :ref:`tag-christmas`, :ref:`tag-amplpy`, :ref:`tag-global-optimization`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-optimize-your-christmas-tree-to-global-optimality|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: christmas_tree.ipynb
    
.. |colab-optimize-your-christmas-tree-to-global-optimality| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimize-your-christmas-tree-to-global-optimality| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimize-your-christmas-tree-to-global-optimality| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimize-your-christmas-tree-to-global-optimality| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimize-your-christmas-tree-to-global-optimality| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/global/christmas_tree.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimized Portfolio Optimization using EIA Data in Python with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimized Portfolio Optimization using EIA Data in Python with AMPL <notebooks/optimized-portfolio-optimization-using-eia-data-in-python-with-ampl.html>`_
| |github-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| |colab-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| |deepnote-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| |kaggle-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| |gradient-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| |sagemaker-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl|
| Description: Portfolio Optimization across Crude Oil, Gold, Natural Gas, Silver, and the S&P 500.
| Tags: :ref:`tag-finance`, :ref:`tag-portfolio-optimization`, :ref:`tag-mean-variance`
| Author: :ref:`email-mukesh96official_at_gmail.com` <mukesh96official@gmail.com>

.. |github-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Notebook_1_Portfolio_Optimization_Commodities.ipynb
    
.. |colab-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimized-portfolio-optimization-using-eia-data-in-python-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_1_Portfolio_Optimization_Commodities.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimizing Procurement and Sales Strategies for a Retail Chain with Supplier Payment Schemes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimizing Procurement and Sales Strategies for a Retail Chain with Supplier Payment Schemes <notebooks/optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes.html>`_
| |github-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| |colab-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| |deepnote-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| |kaggle-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| |gradient-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| |sagemaker-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes|
| Tags: :ref:`tag-amplpy`, :ref:`tag-mip`, :ref:`tag-inventory-management`, :ref:`tag-cash-flow-management`, :ref:`tag-payment-schemes`, :ref:`tag-discounting`, :ref:`tag-multi-period-planning`, :ref:`tag-cost-minimization`, :ref:`tag-cbc`, :ref:`tag-open-source`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: supplier_payment_schemes.ipynb
    
.. |colab-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimizing-procurement-and-sales-strategies-for-a-retail-chain-with-supplier-payment-schemes| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Retail/supplier_payment_schemes.ipynb
    :alt: Open In SageMaker Studio Lab
    


Optimizing the number of staff in a chain of stores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Optimizing the number of staff in a chain of stores <notebooks/optimizing-the-number-of-staff-in-a-chain-of-stores.html>`_
| |github-optimizing-the-number-of-staff-in-a-chain-of-stores| |colab-optimizing-the-number-of-staff-in-a-chain-of-stores| |deepnote-optimizing-the-number-of-staff-in-a-chain-of-stores| |kaggle-optimizing-the-number-of-staff-in-a-chain-of-stores| |gradient-optimizing-the-number-of-staff-in-a-chain-of-stores| |sagemaker-optimizing-the-number-of-staff-in-a-chain-of-stores|
| Tags: :ref:`tag-mip`, :ref:`tag-scheduling`, :ref:`tag-data-driven-model`, :ref:`tag-amplpy`, :ref:`tag-cbc`, :ref:`tag-highs`, :ref:`tag-gurobi`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-optimizing-the-number-of-staff-in-a-chain-of-stores|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: staff_schedule.ipynb
    
.. |colab-optimizing-the-number-of-staff-in-a-chain-of-stores| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: Open In Colab
    
.. |deepnote-optimizing-the-number-of-staff-in-a-chain-of-stores| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-optimizing-the-number-of-staff-in-a-chain-of-stores| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: Open In Kaggle
    
.. |gradient-optimizing-the-number-of-staff-in-a-chain-of-stores| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-optimizing-the-number-of-staff-in-a-chain-of-stores| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/StaffChain/staff_schedule.ipynb
    :alt: Open In SageMaker Studio Lab
    


P-Median problem
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `P-Median problem <notebooks/p-median-problem.html>`_
| |github-p-median-problem| |colab-p-median-problem| |deepnote-p-median-problem| |kaggle-p-median-problem| |gradient-p-median-problem| |sagemaker-p-median-problem|
| Description: this notebook states the p-median problem with a simple example, and a MIP formulation in amplpy. The problem is parametrized with a class, so it is easier to sample and replicate experiments. A graphical solution is plotted.
| Tags: :ref:`tag-amplpy`, :ref:`tag-mip`, :ref:`tag-facility-location`, :ref:`tag-bin-packing`, :ref:`tag-graphs`, :ref:`tag-highs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-p-median-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: p_median.ipynb
    
.. |colab-p-median-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In Colab
    
.. |deepnote-p-median-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-p-median-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In Kaggle
    
.. |gradient-p-median-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-p-median-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/location/p_median.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pairs Trading Strategy Optimization in Python with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pairs Trading Strategy Optimization in Python with AMPL <notebooks/pairs-trading-strategy-optimization-in-python-with-ampl.html>`_
| |github-pairs-trading-strategy-optimization-in-python-with-ampl| |colab-pairs-trading-strategy-optimization-in-python-with-ampl| |deepnote-pairs-trading-strategy-optimization-in-python-with-ampl| |kaggle-pairs-trading-strategy-optimization-in-python-with-ampl| |gradient-pairs-trading-strategy-optimization-in-python-with-ampl| |sagemaker-pairs-trading-strategy-optimization-in-python-with-ampl|
| Description: Optimize pairs trading strategy by optimizing entry and exit thresholds for each pair based on training data. This approach uses interpolation to find optimal parameters within the range tested.
| Tags: :ref:`tag-finance`, :ref:`tag-pairs-trading`
| Author: :ref:`email-mukesh96official_at_gmail.com` <mukesh96official@gmail.com>

.. |github-pairs-trading-strategy-optimization-in-python-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    
.. |colab-pairs-trading-strategy-optimization-in-python-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Open In Colab
    
.. |deepnote-pairs-trading-strategy-optimization-in-python-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-pairs-trading-strategy-optimization-in-python-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Open In Kaggle
    
.. |gradient-pairs-trading-strategy-optimization-in-python-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-pairs-trading-strategy-optimization-in-python-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_2_Pairs_Trading_Strategy_Optimization.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pattern Enumeration
^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pattern Enumeration <notebooks/pattern-enumeration.html>`_
| |github-pattern-enumeration| |colab-pattern-enumeration| |deepnote-pattern-enumeration| |kaggle-pattern-enumeration| |gradient-pattern-enumeration| |sagemaker-pattern-enumeration|
| Description: Pattern enumeration example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-pattern-enumeration|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: pattern_enumeration.ipynb
    
.. |colab-pattern-enumeration| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In Colab
    
.. |deepnote-pattern-enumeration| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-pattern-enumeration| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In Kaggle
    
.. |gradient-pattern-enumeration| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-pattern-enumeration| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_enumeration.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pattern Generation
^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pattern Generation <notebooks/pattern-generation.html>`_
| |github-pattern-generation| |colab-pattern-generation| |deepnote-pattern-generation| |kaggle-pattern-generation| |gradient-pattern-generation| |sagemaker-pattern-generation|
| Description: Pattern generation example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-pattern-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: pattern_generation.ipynb
    
.. |colab-pattern-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In Colab
    
.. |deepnote-pattern-generation| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-pattern-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In Kaggle
    
.. |gradient-pattern-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-pattern-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_generation.ipynb
    :alt: Open In SageMaker Studio Lab
    


Plot feasible region
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Plot feasible region <notebooks/plot-feasible-region.html>`_
| |github-plot-feasible-region| |colab-plot-feasible-region| |deepnote-plot-feasible-region| |kaggle-plot-feasible-region| |gradient-plot-feasible-region| |sagemaker-plot-feasible-region|
| Description: Plot the feasible region and optimal solution for a simple two variable model using AMPL's Python API.
| Tags: :ref:`tag-lecture`, :ref:`tag-lp`, :ref:`tag-simple`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>, :ref:`email-sarah_at_ampl.com` <sarah@ampl.com>

.. |github-plot-feasible-region|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: plot_feasible_region.ipynb
    
.. |colab-plot-feasible-region| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In Colab
    
.. |deepnote-plot-feasible-region| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-plot-feasible-region| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In Kaggle
    
.. |gradient-plot-feasible-region| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-plot-feasible-region| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/plot_feasible_region.ipynb
    :alt: Open In SageMaker Studio Lab
    


Porfolio Optimization with Multiple Risk Strategies in Python with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Porfolio Optimization with Multiple Risk Strategies in Python with AMPL <notebooks/porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl.html>`_
| |github-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| |colab-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| |deepnote-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| |kaggle-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| |gradient-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| |sagemaker-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl|
| Description: This notebook evaluates three distinct risk-based portfolio strategies: Semivariance Optimization, Conditional Value-at-Risk (CVaR) Optimization, and Conditional Drawdown-at-Risk (CDaR) Optimization.
| Tags: :ref:`tag-finance`, :ref:`tag-portfolio-optimization`, :ref:`tag-cvar`, :ref:`tag-cdar`, :ref:`tag-semivariance`
| Author: :ref:`email-mukesh96official_at_gmail.com` <mukesh96official@gmail.com>

.. |github-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    
.. |colab-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Open In Colab
    
.. |deepnote-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Open In Kaggle
    
.. |gradient-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-porfolio-optimization-with-multiple-risk-strategies-in-python-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb
    :alt: Open In SageMaker Studio Lab
    


Power System Optimization with Amplpower package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Power System Optimization with Amplpower package <notebooks/power-system-optimization-with-amplpower-package.html>`_
| |github-power-system-optimization-with-amplpower-package| |colab-power-system-optimization-with-amplpower-package| |deepnote-power-system-optimization-with-amplpower-package| |kaggle-power-system-optimization-with-amplpower-package| |gradient-power-system-optimization-with-amplpower-package| |sagemaker-power-system-optimization-with-amplpower-package|
| Description: this notebook uses amplpower package to solver opf problems
| Tags: :ref:`tag-amplpower`, :ref:`tag-amplpy`, :ref:`tag-energy`, :ref:`tag-opf`, :ref:`tag-matpower`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-power-system-optimization-with-amplpower-package|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: ampl_power.ipynb
    
.. |colab-power-system-optimization-with-amplpower-package| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: Open In Colab
    
.. |deepnote-power-system-optimization-with-amplpower-package| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-power-system-optimization-with-amplpower-package| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: Open In Kaggle
    
.. |gradient-power-system-optimization-with-amplpower-package| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-power-system-optimization-with-amplpower-package| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/energy/ampl_power.ipynb
    :alt: Open In SageMaker Studio Lab
    


Predicting and Optimizing Avocado Sales with Python + Amplpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Predicting and Optimizing Avocado Sales with Python + Amplpy <notebooks/predicting-and-optimizing-avocado-sales-with-python-amplpy.html>`_
| |github-predicting-and-optimizing-avocado-sales-with-python-amplpy| |colab-predicting-and-optimizing-avocado-sales-with-python-amplpy| |deepnote-predicting-and-optimizing-avocado-sales-with-python-amplpy| |kaggle-predicting-and-optimizing-avocado-sales-with-python-amplpy| |gradient-predicting-and-optimizing-avocado-sales-with-python-amplpy| |sagemaker-predicting-and-optimizing-avocado-sales-with-python-amplpy|
| Description: In this notebook, we explore a real-world example of demand estimation and supply optimization using a Kaggle dataset on avocado sales. We start by training a machine learning model to estimate demand and then formulate and solve an optimization model in AMPL to maximize revenue while minimizing waste and transportation costs.
| Tags: :ref:`tag-scikit-learn`, :ref:`tag-machine-learning`, :ref:`tag-price-prediction`, :ref:`tag-forecast`, :ref:`tag-gurobi`, :ref:`tag-amplpy`, :ref:`tag-kaggle`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-predicting-and-optimizing-avocado-sales-with-python-amplpy|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: predict_avocado.ipynb
    
.. |colab-predicting-and-optimizing-avocado-sales-with-python-amplpy| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: Open In Colab
    
.. |deepnote-predicting-and-optimizing-avocado-sales-with-python-amplpy| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-predicting-and-optimizing-avocado-sales-with-python-amplpy| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: Open In Kaggle
    
.. |gradient-predicting-and-optimizing-avocado-sales-with-python-amplpy| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-predicting-and-optimizing-avocado-sales-with-python-amplpy| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/miscellaneous/predict_avocado.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pricing Optimization (Price Elasticity of Demand)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pricing Optimization (Price Elasticity of Demand) <notebooks/pricing-optimization-price-elasticity-of-demand.html>`_
| |github-pricing-optimization-price-elasticity-of-demand| |colab-pricing-optimization-price-elasticity-of-demand| |deepnote-pricing-optimization-price-elasticity-of-demand| |kaggle-pricing-optimization-price-elasticity-of-demand| |gradient-pricing-optimization-price-elasticity-of-demand| |sagemaker-pricing-optimization-price-elasticity-of-demand|
| Tags: :ref:`tag-amplpy`, :ref:`tag-mip`, :ref:`tag-pricing-optimization`, :ref:`tag-demand-elasticity`, :ref:`tag-profit-maximization`, :ref:`tag-economic-modeling`, :ref:`tag-piecewise-linear`, :ref:`tag-cplex`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-pricing-optimization-price-elasticity-of-demand|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: demand_elasticity.ipynb
    
.. |colab-pricing-optimization-price-elasticity-of-demand| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: Open In Colab
    
.. |deepnote-pricing-optimization-price-elasticity-of-demand| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-pricing-optimization-price-elasticity-of-demand| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: Open In Kaggle
    
.. |gradient-pricing-optimization-price-elasticity-of-demand| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-pricing-optimization-price-elasticity-of-demand| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Demand_elasticity/demand_elasticity.ipynb
    :alt: Open In SageMaker Studio Lab
    


Pricing and target-market
^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Pricing and target-market <notebooks/pricing-and-target-market.html>`_
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
    


Production Model: lemonade stand example 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Production Model: lemonade stand example  <notebooks/production-model-lemonade-stand-example.html>`_
| |github-production-model-lemonade-stand-example| |colab-production-model-lemonade-stand-example| |deepnote-production-model-lemonade-stand-example| |kaggle-production-model-lemonade-stand-example| |gradient-production-model-lemonade-stand-example| |sagemaker-production-model-lemonade-stand-example|
| Description: Basic introduction to AMPL's indexed entities and the Pygwalker Python package via a lemonade stand example
| Tags: :ref:`tag-ampl-lecture`, :ref:`tag-amplpy`, :ref:`tag-ampl`, :ref:`tag-introduction`, :ref:`tag-linear-programming`, :ref:`tag-sets`, :ref:`tag-indexing`, :ref:`tag-lemonade-stand`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-production-model-lemonade-stand-example|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: production_model.ipynb
    
.. |colab-production-model-lemonade-stand-example| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In Colab
    
.. |deepnote-production-model-lemonade-stand-example| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-production-model-lemonade-stand-example| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In Kaggle
    
.. |gradient-production-model-lemonade-stand-example| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-production-model-lemonade-stand-example| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/ampl-lecture/production_model.ipynb
    :alt: Open In SageMaker Studio Lab
    


Production model
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Production model <notebooks/production-model.html>`_
| |github-production-model| |colab-production-model| |deepnote-production-model| |kaggle-production-model| |gradient-production-model| |sagemaker-production-model|
| Description: generic model for production problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-book`, :ref:`tag-industry`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-production-model|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: production_model.ipynb
    
.. |colab-production-model| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Colab
    
.. |deepnote-production-model| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-production-model| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Kaggle
    
.. |gradient-production-model| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-production-model| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-book/production_model.ipynb
    :alt: Open In SageMaker Studio Lab
    


Profit Maximization for Developers: Optimizing Pricing, Marketing, and Investment Strategies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Profit Maximization for Developers: Optimizing Pricing, Marketing, and Investment Strategies <notebooks/profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies.html>`_
| |github-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| |colab-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| |deepnote-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| |kaggle-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| |gradient-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| |sagemaker-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies|
| Tags: :ref:`tag-marketing`, :ref:`tag-price-optimization`, :ref:`tag-profitability`, :ref:`tag-residential-developer`, :ref:`tag-piecewise-linear`, :ref:`tag-mip`, :ref:`tag-ampl-only`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: building_developer.ipynb
    
.. |colab-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: Open In Colab
    
.. |deepnote-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: Open In Kaggle
    
.. |gradient-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-profit-maximization-for-developers-optimizing-pricing-marketing-and-investment-strategies| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Building_developer/building_developer.ipynb
    :alt: Open In SageMaker Studio Lab
    


Project management: Minimize project costs by balancing task costs, risks, and late penalties.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Project management: Minimize project costs by balancing task costs, risks, and late penalties. <notebooks/project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties.html>`_
| |github-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| |colab-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| |deepnote-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| |kaggle-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| |gradient-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| |sagemaker-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties|
| Tags: :ref:`tag-construction-management`, :ref:`tag-project-management`, :ref:`tag-risk-management`, :ref:`tag-mip`, :ref:`tag-ampl`, :ref:`tag-cbc`, :ref:`tag-scheduling`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Investment_project.ipynb
    
.. |colab-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Open In Colab
    
.. |deepnote-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Open In Kaggle
    
.. |gradient-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-project-management-minimize-project-costs-by-balancing-task-costs-risks-and-late-penalties| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Project_management/Investment_project.ipynb
    :alt: Open In SageMaker Studio Lab
    


Quick Start using Pandas dataframes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Quick Start using Pandas dataframes <notebooks/quick-start-using-pandas-dataframes.html>`_
| |github-quick-start-using-pandas-dataframes| |colab-quick-start-using-pandas-dataframes| |deepnote-quick-start-using-pandas-dataframes| |kaggle-quick-start-using-pandas-dataframes| |gradient-quick-start-using-pandas-dataframes| |sagemaker-quick-start-using-pandas-dataframes|
| Description: Quick Start using Pandas dataframes to load and retrieve data
| Tags: :ref:`tag-amplpy`, :ref:`tag-quick-start`, :ref:`tag-pandas`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-quick-start-using-pandas-dataframes|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: pandasdiet.ipynb
    
.. |colab-quick-start-using-pandas-dataframes| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In Colab
    
.. |deepnote-quick-start-using-pandas-dataframes| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-quick-start-using-pandas-dataframes| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In Kaggle
    
.. |gradient-quick-start-using-pandas-dataframes| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-quick-start-using-pandas-dataframes| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Quick Start using lists and dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Quick Start using lists and dictionaries <notebooks/quick-start-using-lists-and-dictionaries.html>`_
| |github-quick-start-using-lists-and-dictionaries| |colab-quick-start-using-lists-and-dictionaries| |deepnote-quick-start-using-lists-and-dictionaries| |kaggle-quick-start-using-lists-and-dictionaries| |gradient-quick-start-using-lists-and-dictionaries| |sagemaker-quick-start-using-lists-and-dictionaries|
| Description: Quick Start using lists and dictionaries to load and retrieve data
| Tags: :ref:`tag-amplpy`, :ref:`tag-quick-start`, :ref:`tag-highlights`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-quick-start-using-lists-and-dictionaries|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: nativediet.ipynb
    
.. |colab-quick-start-using-lists-and-dictionaries| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In Colab
    
.. |deepnote-quick-start-using-lists-and-dictionaries| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-quick-start-using-lists-and-dictionaries| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In Kaggle
    
.. |gradient-quick-start-using-lists-and-dictionaries| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-quick-start-using-lists-and-dictionaries| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
    :alt: Open In SageMaker Studio Lab
    


Retrieve Solution pool with AMPL and Gurobi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Retrieve Solution pool with AMPL and Gurobi <notebooks/retrieve-solution-pool-with-ampl-and-gurobi.html>`_
| |github-retrieve-solution-pool-with-ampl-and-gurobi| |colab-retrieve-solution-pool-with-ampl-and-gurobi| |deepnote-retrieve-solution-pool-with-ampl-and-gurobi| |kaggle-retrieve-solution-pool-with-ampl-and-gurobi| |gradient-retrieve-solution-pool-with-ampl-and-gurobi| |sagemaker-retrieve-solution-pool-with-ampl-and-gurobi|
| Description: This notebook describes how to retrieve multiple solutions from the solver's solution pool. Optimization problems usually have several optimal solutions, one is returned by the solver but the others are discarded. These alternative solutions can also be retrieved by AMPL.
| Tags: :ref:`tag-solution-pool`, :ref:`tag-gurobi`, :ref:`tag-cplex`, :ref:`tag-xpress`, :ref:`tag-mip`, :ref:`tag-mixed-integer-linear`, :ref:`tag-mp`, :ref:`tag-tutorials`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>, :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-retrieve-solution-pool-with-ampl-and-gurobi|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: solution_pool.ipynb
    
.. |colab-retrieve-solution-pool-with-ampl-and-gurobi| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: Open In Colab
    
.. |deepnote-retrieve-solution-pool-with-ampl-and-gurobi| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-retrieve-solution-pool-with-ampl-and-gurobi| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: Open In Kaggle
    
.. |gradient-retrieve-solution-pool-with-ampl-and-gurobi| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-retrieve-solution-pool-with-ampl-and-gurobi| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/tutorials/solution_pool.ipynb
    :alt: Open In SageMaker Studio Lab
    


Robust Linear Programming with Ellipsoidal Uncertainty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Robust Linear Programming with Ellipsoidal Uncertainty <notebooks/robust-linear-programming-with-ellipsoidal-uncertainty.html>`_
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
    


Roll Cutting - Revision 1 & 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Roll Cutting - Revision 1 & 2 <notebooks/roll-cutting-revision-1-and-2.html>`_
| |github-roll-cutting-revision-1-and-2| |colab-roll-cutting-revision-1-and-2| |deepnote-roll-cutting-revision-1-and-2| |kaggle-roll-cutting-revision-1-and-2| |gradient-roll-cutting-revision-1-and-2| |sagemaker-roll-cutting-revision-1-and-2|
| Description: Pattern tradeoff example with amplpy
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-roll-cutting-revision-1-and-2|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: pattern_tradeoff.ipynb
    
.. |colab-roll-cutting-revision-1-and-2| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In Colab
    
.. |deepnote-roll-cutting-revision-1-and-2| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-roll-cutting-revision-1-and-2| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In Kaggle
    
.. |gradient-roll-cutting-revision-1-and-2| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-roll-cutting-revision-1-and-2| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/pattern_tradeoff.ipynb
    :alt: Open In SageMaker Studio Lab
    


Scheduling Multipurpose Batch Processes using State-Task Networks in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Scheduling Multipurpose Batch Processes using State-Task Networks in Python <notebooks/scheduling-multipurpose-batch-processes-using-state-task-networks-in-python.html>`_
| |github-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |colab-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |deepnote-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |kaggle-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |gradient-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| |sagemaker-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python|
| Description: The State-Task Network (STN) is an approach to modeling multipurpose batch process for the purpose of short term scheduling. It was first developed by Kondili, et al., in 1993, and subsequently developed and extended by others.
| Tags: :ref:`tag-state-task-networks`, :ref:`tag-gdp`, :ref:`tag-disjunctive-programming`, :ref:`tag-batch-processes`, :ref:`tag-batch-processing`
| Author: Jeffrey C. Kantor, :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: batch_processessing.ipynb
    
.. |colab-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In Colab
    
.. |deepnote-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In Kaggle
    
.. |gradient-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-scheduling-multipurpose-batch-processes-using-state-task-networks-in-python| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/cookbook/batch_processessing.ipynb
    :alt: Open In SageMaker Studio Lab
    


Simple sudoku solver using logical constraints (with GUI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Simple sudoku solver using logical constraints (with GUI) <notebooks/simple-sudoku-solver-using-logical-constraints-with-gui.html>`_
| |github-simple-sudoku-solver-using-logical-constraints-with-gui| |colab-simple-sudoku-solver-using-logical-constraints-with-gui| |deepnote-simple-sudoku-solver-using-logical-constraints-with-gui| |kaggle-simple-sudoku-solver-using-logical-constraints-with-gui| |gradient-simple-sudoku-solver-using-logical-constraints-with-gui| |sagemaker-simple-sudoku-solver-using-logical-constraints-with-gui|
| Description: Simple sudoku model with two formulations: as a Constraint Programming problem using the *alldiff* operator and as a MIP. Note that the CP formulation is more natural but it needs a solver supporting logical constraints or a MIP solver with automatic reformulation support (see [here](https://mp.ampl.com/) for more information).
| Tags: :ref:`tag-amplpy`, :ref:`tag-constraint-programming`, :ref:`tag-gui`, :ref:`tag-highlights`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. |github-simple-sudoku-solver-using-logical-constraints-with-gui|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: sudoku.ipynb
    
.. |colab-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In Colab
    
.. |deepnote-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In Kaggle
    
.. |gradient-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-simple-sudoku-solver-using-logical-constraints-with-gui| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/miscellaneous/sudoku.ipynb
    :alt: Open In SageMaker Studio Lab
    


Smart Pipeline Diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Smart Pipeline Diagnostics <notebooks/smart-pipeline-diagnostics.html>`_
| |github-smart-pipeline-diagnostics| |colab-smart-pipeline-diagnostics| |deepnote-smart-pipeline-diagnostics| |kaggle-smart-pipeline-diagnostics| |gradient-smart-pipeline-diagnostics| |sagemaker-smart-pipeline-diagnostics|
| Tags: :ref:`tag-pipeline-diagnostics`, :ref:`tag-risk-management`, :ref:`tag-mip`, :ref:`tag-ampl`, :ref:`tag-cbc`
| Author: :ref:`email-mail_at_solverytic.com` <mail@solverytic.com>

.. |github-smart-pipeline-diagnostics|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Smart_pipeline_diagnostics.ipynb
    
.. |colab-smart-pipeline-diagnostics| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Open In Colab
    
.. |deepnote-smart-pipeline-diagnostics| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-smart-pipeline-diagnostics| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Open In Kaggle
    
.. |gradient-smart-pipeline-diagnostics| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-smart-pipeline-diagnostics| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mikhail/Utilities_networks/Smart_pipeline_diagnostics.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solution check: discontinuous objective function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solution check: discontinuous objective function <notebooks/solution-check-discontinuous-objective-function.html>`_
| |github-solution-check-discontinuous-objective-function| |colab-solution-check-discontinuous-objective-function| |deepnote-solution-check-discontinuous-objective-function| |kaggle-solution-check-discontinuous-objective-function| |gradient-solution-check-discontinuous-objective-function| |sagemaker-solution-check-discontinuous-objective-function|
| Description: Pathological examples to illustrate MP solution checker and settings
| Tags: :ref:`tag-mp-library`, :ref:`tag-solution-check`, :ref:`tag-non-continuous-objective`, :ref:`tag-strict-comparison`
| Author: :ref:`email-gleb_at_ampl.com` <gleb@ampl.com>

.. |github-solution-check-discontinuous-objective-function|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: sol-check.ipynb
    
.. |colab-solution-check-discontinuous-objective-function| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In Colab
    
.. |deepnote-solution-check-discontinuous-objective-function| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-solution-check-discontinuous-objective-function| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In Kaggle
    
.. |gradient-solution-check-discontinuous-objective-function| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-solution-check-discontinuous-objective-function| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/sol-check.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solving a nonogram puzzle
^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solving a nonogram puzzle <notebooks/solving-a-nonogram-puzzle.html>`_
| |github-solving-a-nonogram-puzzle| |colab-solving-a-nonogram-puzzle| |deepnote-solving-a-nonogram-puzzle| |kaggle-solving-a-nonogram-puzzle| |gradient-solving-a-nonogram-puzzle| |sagemaker-solving-a-nonogram-puzzle|
| Description: Model for solving nonogram puzzles autogenerated using **nonogram.mod**, **nonogram.dat** and **nonogram.run**.
| Tags: :ref:`tag-ampl-only`, :ref:`tag-mip`
| Author: :ref:`email-juanjesus.losada_at_gmail.com` <juanjesus.losada@gmail.com>

.. |github-solving-a-nonogram-puzzle|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: nonogram.ipynb
    
.. |colab-solving-a-nonogram-puzzle| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In Colab
    
.. |deepnote-solving-a-nonogram-puzzle| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-solving-a-nonogram-puzzle| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In Kaggle
    
.. |gradient-solving-a-nonogram-puzzle| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-solving-a-nonogram-puzzle| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/juanjesuslosada/miscellaneous/nonogram.ipynb
    :alt: Open In SageMaker Studio Lab
    


Solving simple stochastic optimization problems with AMPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Solving simple stochastic optimization problems with AMPL <notebooks/solving-simple-stochastic-optimization-problems-with-ampl.html>`_
| |github-solving-simple-stochastic-optimization-problems-with-ampl| |colab-solving-simple-stochastic-optimization-problems-with-ampl| |deepnote-solving-simple-stochastic-optimization-problems-with-ampl| |kaggle-solving-simple-stochastic-optimization-problems-with-ampl| |gradient-solving-simple-stochastic-optimization-problems-with-ampl| |sagemaker-solving-simple-stochastic-optimization-problems-with-ampl|
| Description: Examples of the Sample Average Approximation method and risk measures in AMPL
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-stochastic-optimization`, :ref:`tag-sample-average-approximation`, :ref:`tag-risk-measures`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-solving-simple-stochastic-optimization-problems-with-ampl|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: newsvendor.ipynb
    
.. |colab-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In Colab
    
.. |deepnote-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In Kaggle
    
.. |gradient-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-solving-simple-stochastic-optimization-problems-with-ampl| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/newsvendor/newsvendor.ipynb
    :alt: Open In SageMaker Studio Lab
    


Steel industry problem
^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Steel industry problem <notebooks/steel-industry-problem.html>`_
| |github-steel-industry-problem| |colab-steel-industry-problem| |deepnote-steel-industry-problem| |kaggle-steel-industry-problem| |gradient-steel-industry-problem| |sagemaker-steel-industry-problem|
| Description: model for steel production problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`, :ref:`tag-industry`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-steel-industry-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: steel_lecture.ipynb
    
.. |colab-steel-industry-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Colab
    
.. |deepnote-steel-industry-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-steel-industry-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Kaggle
    
.. |gradient-steel-industry-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-steel-industry-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/steel_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Sudoku Generator
^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Sudoku Generator <notebooks/sudoku-generator.html>`_
| |github-sudoku-generator| |colab-sudoku-generator| |deepnote-sudoku-generator| |kaggle-sudoku-generator| |gradient-sudoku-generator| |sagemaker-sudoku-generator|
| Description: Generate Sudoku boards with unique solution via iterative method and mip formulation.
| Tags: :ref:`tag-mip`, :ref:`tag-heuristics`, :ref:`tag-puzzles`, :ref:`tag-amplpy`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-sudoku-generator|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: sudoku_gen.ipynb
    
.. |colab-sudoku-generator| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In Colab
    
.. |deepnote-sudoku-generator| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-sudoku-generator| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In Kaggle
    
.. |gradient-sudoku-generator| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-sudoku-generator| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/puzzles/sudoku_gen.ipynb
    :alt: Open In SageMaker Studio Lab
    


Supply chain network
^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Supply chain network <notebooks/supply-chain-network.html>`_
| |github-supply-chain-network| |colab-supply-chain-network| |deepnote-supply-chain-network| |kaggle-supply-chain-network| |gradient-supply-chain-network| |sagemaker-supply-chain-network|
| Description: Compute optimal routes to connect suppliers/demanding nodes in a network. Routes have an associated fixed and variable cost. There are different products to ship. The problem is formulated as a MIP with binary variables. Python data structures are used to load the data into the model.
| Tags: :ref:`tag-mixed-integer-linear`, :ref:`tag-supply_chain`, :ref:`tag-network`, :ref:`tag-transportation`, :ref:`tag-graphs`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-supply-chain-network|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: supply_chain_simple_routes.ipynb
    
.. |colab-supply-chain-network| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In Colab
    
.. |deepnote-supply-chain-network| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-supply-chain-network| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In Kaggle
    
.. |gradient-supply-chain-network| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-supply-chain-network| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/supply_chain_simple_routes.ipynb
    :alt: Open In SageMaker Studio Lab
    


Transportation problem
^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Transportation problem <notebooks/transportation-problem.html>`_
| |github-transportation-problem| |colab-transportation-problem| |deepnote-transportation-problem| |kaggle-transportation-problem| |gradient-transportation-problem| |sagemaker-transportation-problem|
| Description: an AMPL model for the transportation problem
| Tags: :ref:`tag-ampl-only`, :ref:`tag-ampl-lecture`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-transportation-problem|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: transp_lecture.ipynb
    
.. |colab-transportation-problem| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Colab
    
.. |deepnote-transportation-problem| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-transportation-problem| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Kaggle
    
.. |gradient-transportation-problem| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-transportation-problem| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/ampl-lecture/transp_lecture.ipynb
    :alt: Open In SageMaker Studio Lab
    


Travelling Salesman Problem with subtour elimination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Travelling Salesman Problem with subtour elimination <notebooks/travelling-salesman-problem-with-subtour-elimination.html>`_
| |github-travelling-salesman-problem-with-subtour-elimination| |colab-travelling-salesman-problem-with-subtour-elimination| |deepnote-travelling-salesman-problem-with-subtour-elimination| |kaggle-travelling-salesman-problem-with-subtour-elimination| |gradient-travelling-salesman-problem-with-subtour-elimination| |sagemaker-travelling-salesman-problem-with-subtour-elimination|
| Description: this example shows how to solve a TSP  by eliminating subtours using amplpy and ampls
| Tags: :ref:`tag-callbacks`, :ref:`tag-tsp`
| Author: :ref:`email-ccv_at_ampl.com` <ccv@ampl.com>

.. |github-travelling-salesman-problem-with-subtour-elimination|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: tsp_simple_cuts_generic.ipynb
    
.. |colab-travelling-salesman-problem-with-subtour-elimination| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In Colab
    
.. |deepnote-travelling-salesman-problem-with-subtour-elimination| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-travelling-salesman-problem-with-subtour-elimination| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In Kaggle
    
.. |gradient-travelling-salesman-problem-with-subtour-elimination| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-travelling-salesman-problem-with-subtour-elimination| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/mapgccv/callbacks/tsp_simple_cuts_generic.ipynb
    :alt: Open In SageMaker Studio Lab
    


Unit Commitment Problem with AMPL and Python - Power Grid Lib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Unit Commitment Problem with AMPL and Python - Power Grid Lib <notebooks/unit-commitment-problem-with-ampl-and-python-power-grid-lib.html>`_
| |github-unit-commitment-problem-with-ampl-and-python-power-grid-lib| |colab-unit-commitment-problem-with-ampl-and-python-power-grid-lib| |deepnote-unit-commitment-problem-with-ampl-and-python-power-grid-lib| |kaggle-unit-commitment-problem-with-ampl-and-python-power-grid-lib| |gradient-unit-commitment-problem-with-ampl-and-python-power-grid-lib| |sagemaker-unit-commitment-problem-with-ampl-and-python-power-grid-lib|
| Description: Generic notebook to solve Unit Commitment problems with AMPL and Python using the Power Grid Lib model and test instances.
| Tags: :ref:`tag-ampl`, :ref:`tag-amplpy`, :ref:`tag-python`, :ref:`tag-power-grid-lib`, :ref:`tag-unit-commitment-problem`
| Author: :ref:`email-nicolau_at_ampl.com` <nicolau@ampl.com>

.. |github-unit-commitment-problem-with-ampl-and-python-power-grid-lib|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: pglib_uc.ipynb
    
.. |colab-unit-commitment-problem-with-ampl-and-python-power-grid-lib| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: Open In Colab
    
.. |deepnote-unit-commitment-problem-with-ampl-and-python-power-grid-lib| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-unit-commitment-problem-with-ampl-and-python-power-grid-lib| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: Open In Kaggle
    
.. |gradient-unit-commitment-problem-with-ampl-and-python-power-grid-lib| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-unit-commitment-problem-with-ampl-and-python-power-grid-lib| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/nfbvs/pglib_uc/pglib_uc.ipynb
    :alt: Open In SageMaker Studio Lab
    


Unit Commitment for Electrical Power Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Unit Commitment for Electrical Power Generation <notebooks/unit-commitment-for-electrical-power-generation.html>`_
| |github-unit-commitment-for-electrical-power-generation| |colab-unit-commitment-for-electrical-power-generation| |deepnote-unit-commitment-for-electrical-power-generation| |kaggle-unit-commitment-for-electrical-power-generation| |gradient-unit-commitment-for-electrical-power-generation| |sagemaker-unit-commitment-for-electrical-power-generation|
| Description: This notebook illustrates the power generation problem using AMPL. The original version featured the Gurobi solver. By default, this notebook uses the HiGHS and CBC solvers.
| Tags: :ref:`tag-amplpy`, :ref:`tag-energy`, :ref:`tag-power-generation`, :ref:`tag-unit-commitment`
| Author: :ref:`email-gyorgy_at_ampl.com` <gyorgy@ampl.com>

.. |github-unit-commitment-for-electrical-power-generation|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: unit_commitment.ipynb
    
.. |colab-unit-commitment-for-electrical-power-generation| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In Colab
    
.. |deepnote-unit-commitment-for-electrical-power-generation| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-unit-commitment-for-electrical-power-generation| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In Kaggle
    
.. |gradient-unit-commitment-for-electrical-power-generation| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-unit-commitment-for-electrical-power-generation| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/gomfy/energy/unit_commitment.ipynb
    :alt: Open In SageMaker Studio Lab
    


VPSolver: Cutting & Packing Problems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `VPSolver: Cutting & Packing Problems <notebooks/vpsolver-cutting-and-packing-problems.html>`_
| |github-vpsolver-cutting-and-packing-problems| |colab-vpsolver-cutting-and-packing-problems| |deepnote-vpsolver-cutting-and-packing-problems| |kaggle-vpsolver-cutting-and-packing-problems| |gradient-vpsolver-cutting-and-packing-problems| |sagemaker-vpsolver-cutting-and-packing-problems|
| Description: Solving cutting & packing problems using arc-flow formulations
| Tags: :ref:`tag-industry`, :ref:`tag-cutting-stock`, :ref:`tag-bin-packing`, :ref:`tag-vector-packing`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-vpsolver-cutting-and-packing-problems|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: vpsolver.ipynb
    
.. |colab-vpsolver-cutting-and-packing-problems| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In Colab
    
.. |deepnote-vpsolver-cutting-and-packing-problems| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-vpsolver-cutting-and-packing-problems| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In Kaggle
    
.. |gradient-vpsolver-cutting-and-packing-problems| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-vpsolver-cutting-and-packing-problems| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/vpsolver/vpsolver.ipynb
    :alt: Open In SageMaker Studio Lab
    


Vehicle Routing Problem with Fair Profits and Time Windows (VRP-FPTW)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Vehicle Routing Problem with Fair Profits and Time Windows (VRP-FPTW) <notebooks/vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw.html>`_
| |github-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| |colab-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| |deepnote-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| |kaggle-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| |gradient-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| |sagemaker-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw|
| Description: This notebook implements and solves the Vehicle Routing Problem with Fair Profits and Time Windows (VRP-FPTW), a realistic and recent extension of the classical VRP problem.
| Tags: :ref:`tag-amplpy`, :ref:`tag-routing`, :ref:`tag-vrp`, :ref:`tag-time-windows`, :ref:`tag-mp`, :ref:`tag-cuopt`, :ref:`tag-highs`, :ref:`tag-gurobi`, :ref:`tag-research`, :ref:`tag-automatic-reformulation`, :ref:`tag-benchmark`
| Author: :ref:`email-aitor.lopez_at_urjc.es` <aitor.lopez@urjc.es>, :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: vrp_fptw.ipynb
    
.. |colab-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: Open In Colab
    
.. |deepnote-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: Open In Kaggle
    
.. |gradient-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-vehicle-routing-problem-with-fair-profits-and-time-windows-vrp-fptw| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/routing/vrp_fptw.ipynb
    :alt: Open In SageMaker Studio Lab
    


Warehouse location and transport
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `Warehouse location and transport <notebooks/warehouse-location-and-transport.html>`_
| |github-warehouse-location-and-transport| |colab-warehouse-location-and-transport| |deepnote-warehouse-location-and-transport| |kaggle-warehouse-location-and-transport| |gradient-warehouse-location-and-transport| |sagemaker-warehouse-location-and-transport|
| Description: Model for warehouse allocation. Farms (suppliers) send feedstock to warehouses, and later on, those warehouses send it to a production plant. The problem involves modeling a storage facility location problem with a transportation component to the final plant.
| Tags: :ref:`tag-facility-location`, :ref:`tag-highs`, :ref:`tag-mip`, :ref:`tag-mixed-integer-linear`, :ref:`tag-supply_chain`, :ref:`tag-network`, :ref:`tag-transportation`, :ref:`tag-graphs`, :ref:`tag-networkx`, :ref:`tag-transportation`, :ref:`tag-mp`
| Author: :ref:`email-marcos_at_ampl.com` <marcos@ampl.com>

.. |github-warehouse-location-and-transport|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: warehouse_location.ipynb
    
.. |colab-warehouse-location-and-transport| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: Open In Colab
    
.. |deepnote-warehouse-location-and-transport| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-warehouse-location-and-transport| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: Open In Kaggle
    
.. |gradient-warehouse-location-and-transport| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-warehouse-location-and-transport| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/marcos-dv/supply_chain/warehouse_location.ipynb
    :alt: Open In SageMaker Studio Lab
    


amplpy setup & Quick Start
^^^^^^^^^^^^^^^^^^^^^^^^^^
| `Notebooks <notebooks/index.html>`_ > `amplpy setup & Quick Start <notebooks/amplpy-setup-and-quick-start.html>`_
| |github-amplpy-setup-and-quick-start| |colab-amplpy-setup-and-quick-start| |deepnote-amplpy-setup-and-quick-start| |kaggle-amplpy-setup-and-quick-start| |gradient-amplpy-setup-and-quick-start| |sagemaker-amplpy-setup-and-quick-start|
| Description: amplpy setup and quick start
| Tags: :ref:`tag-amplpy`, :ref:`tag-example`
| Author: :ref:`email-fdabrandao_at_gmail.com` <fdabrandao@gmail.com>

.. |github-amplpy-setup-and-quick-start|  image:: https://img.shields.io/badge/github-%23121011.svg?logo=github
    :target: https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: quickstart.ipynb
    
.. |colab-amplpy-setup-and-quick-start| image:: https://colab.research.google.com/assets/colab-badge.svg
    :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In Colab
    
.. |deepnote-amplpy-setup-and-quick-start| image:: https://deepnote.com/buttons/launch-in-deepnote-small.svg
    :target: https://deepnote.com/launch?url=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In Deepnote
    
.. |kaggle-amplpy-setup-and-quick-start| image:: https://kaggle.com/static/images/open-in-kaggle.svg
    :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In Kaggle
    
.. |gradient-amplpy-setup-and-quick-start| image:: https://assets.paperspace.io/img/gradient-badge.svg
    :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In Gradient
    
.. |sagemaker-amplpy-setup-and-quick-start| image:: https://studiolab.sagemaker.aws/studiolab.svg
    :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/examples/quickstart.ipynb
    :alt: Open In SageMaker Studio Lab
    


