.. _sensors_to_analysis:
.. _collect_to_analysis:

===============
Data Analysis
===============


-----------------------------
Introduction to Data Analysis
-----------------------------

Being able to collect physiological data and use it in VR is wonderful, but isn't really meaningful for making any observations or conclusions without performing analysis. The last section of this tutorial will focus on basic tools to analyze the data that we've collected from the VR application.

Since we're collecting data from the user as they perform some tasks, with the sensors updating the results periodically, this is an example of **time-series** data. This is a special type of data where the sequence of observations matters, and certain models may reflect the fact that observations closer together in time should be more closely related than those further apart. We'll go through some methods of extracting relevant information, numerically and visually, from the data from each sensor.

^^^^^^^^^^^^^^^^^^^^^^^^^
Programming Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^

Throughout this section, we'll be using Python as the tool for the analysis. That doesn't take away from the concepts, as much of this could be implemented in other languages. However, Python is one of the most popular tools as it has a wide variety of open source resources available and a strong community of developers that can provide feedback to each other throughout the process. This tutorial will assume a basic understanding of programming concepts and some Python syntax.

Python can be easily downloaded for free from their `website <https://www.python.org/downloads/>`_. You'll then need to install the following packages (documentation linked), using ``pip`` (the default installer) or your favorite package manager:

* General Data Analysis
   - `Matplotlib <https://matplotlib.org/>`_
   - `Pandas <https://pandas.pydata.org/>`_
   - `NumPy <https://numpy.org/>`_
   - `SciPy <https://scipy.org/>`_   
* Working with Physiological Data 
   - `LibEMG <https://libemg.github.io/libemg/>`_ [#]_
   - `NeuroKit2 <https://neuropsychology.github.io/NeuroKit/introduction.html>`_ [#]_

::

    pip install matplotlib pandas numpy scipy libemg neurokit2

With Python ready to go, this is all we need to begin analysis. Let's dive in starting with EMG.

------------
EMG Analysis
------------

^^^^^^^^^^^^^^^^^^^^^^^
Raw Data: Load and Plot
^^^^^^^^^^^^^^^^^^^^^^^

.. cover both approaches, single and dataset

^^^^^^^^^^^^^^^^^^^^
Filtering the Signal
^^^^^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^^^^^^^^
Types of Visualizations
^^^^^^^^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^^^
Feature Extraction
^^^^^^^^^^^^^^^^^^


-------------------
Heart Rate Analysis
-------------------

.. These subsections could change, just putting them in for now.

^^^^^^^^^^^^^^^^^^^^^^^
Raw Data: Load and Plot
^^^^^^^^^^^^^^^^^^^^^^^

^^^^^^^^^^^^^
Preprocessing
^^^^^^^^^^^^^

^^^^^^^^^^^^^^^^^^
Feature Extraction
^^^^^^^^^^^^^^^^^^

------------------------------------
Overview of Data Analysis Techniques
------------------------------------

Let's recap what we've learned by analyzing the data from each of these sensors, with a focus on the overarching processes and concepts that we followed. This section will serve as a useful reference for future work.

^^^^^^^^^^^^^^^^^^^^
Data Science Process
^^^^^^^^^^^^^^^^^^^^

Going all the way back to :ref:`analysis_to_collect`, we went through a process that started by asking questions, then collected some data, and went through a variety of steps to analyze that data. This is the core of **data science**, and as you become more experienced, you'll start to notice the pattern in how this process most often proceeds. Let's outline it formally here.

.. TODO: steps from collection through conclusions (exploratory, filtering, extraction, modeling, validation, etc.) 

^^^^^^^^^^^^^^^^^^^^
Time Series Analysis
^^^^^^^^^^^^^^^^^^^^

With each of the data types we saw two overarching methods of analysis: one where we looked at how the signal changed over time, and the other where we looked at how the signal was distributed over a range of frequencies. It turns out that these have special names as the two widely accepted ways of analyzing time-series data.

.. TODO: time domain and frequency domain


--------------
Section Review
--------------


----------
References
----------

.. [#] \E. Eddy, E. Campbell, A. Phinyomark, S. Bateman, and E. Scheme. "LibEMG: An Open Source Library to Facilitate the Exploration of Myoelectric Control." *IEEE Access*, vol. 11, pp. 87380-87397, 2023, doi: 10.1109/ACCESS.2023.3304544

.. [#] \D. Makowski, T. Pham, Z.J. Lau, J.C. Brammer, F. Lespinasse, H. Pham, C. Schölzel, and S.A. Chen. "NeuroKit2: A Python toolbox for neurophysiological signal processing." *Behavior Research Methods*, vol. 53, no. 4, pp. 1689-1696, 2021, doi: 10.3758/s13428-020-01516-y