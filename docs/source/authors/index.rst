
Authors
=======

The notebooks in this repository are contributed by the following authors:

.. toctree::
    :maxdepth: 1

    aitor.lopez_at_urjc.es
    ccv_at_ampl.com
    fdabrandao_at_gmail.com
    gleb_at_ampl.com
    gyorgy_at_ampl.com
    juanjesus.losada_at_gmail.com
    jurgenlentz26_at_gmail.com
    marcos_at_ampl.com
    mail_at_solverytic.com
    mukesh96official_at_gmail.com
    nicolau_at_ampl.com
    sarah_at_ampl.com
    yimin_wang_at_asu.edu


.. note::
    **Your name can be here too!** Just make a pull request to https://github.com/ampl/colab.ampl.com or
    send a link to your notebook by email to devteam@ampl.com.

Contribution Guide
------------------

1. Use the template
   `template/colab.ipynb <https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb>`__
   as base template.

2. In the header make sure you fill the following fields:

::

   Description: <required>

   Tags: <required>, <>, <>

   Notebook author: <required>

   Model author: <optional>

   License: <optional>

   References: <optional>

3. Do not modify the initial two cells that take care of setup and
   jupyter notebook integration to do anything other than installing
   packages and instantiating the ampl_notebook. You can modify the list
   of modules and add more dependencies, but if you do anything else the
   changes may be overwritten.

4. Place your notebook inside ``colab.ampl.com/authors/<github_username>/``.

5. Update the badges and the index as shown below before committing.

Note: The default license for every notebook is
`MIT <https://github.com/ampl/colab.ampl.com/blob/master/LICENSE>`__ unless
specified otherwise in the notebook.

Updating notebook headers & index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following commands update the README file and the index in the
documentation, as well as add any new automatically created files:

.. code:: bash

   $ python scripts/index.py
   $ git add docs/source/

Note that the notebook headers are patched with new badges using links
to the correct locations after the notebook is published. The first two
notebook cells are modified to ensure that requirements are installed
and that the ampl_notebook is instantiated.

