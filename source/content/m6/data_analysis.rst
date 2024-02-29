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
   - `NumPy <https://numpy.org/>`_
   - `SciPy <https://scipy.org/>`_
* Working with Physiological Data 
   - `LibEMG <https://libemg.github.io/libemg/>`_ [#]_
   - `NeuroKit2 <https://neuropsychology.github.io/NeuroKit/introduction.html>`_ [#]_

(`Pandas <https://pandas.pydata.org/>`_ is another common Python library for data analysis. However, for our purposes, NumPy will be simpler to use, and it's used natively by the other libraries we're using for physiological data.)

::

    pip install matplotlib numpy scipy libemg neurokit2

With Python ready to go, this is all we need to begin analysis. Let's dive in starting with EMG.

------------
EMG Analysis
------------

^^^^^^^^^^^^^^^^^^^^^^^
Raw Data: Load and Plot
^^^^^^^^^^^^^^^^^^^^^^^

.. cover both approaches, single and dataset

The first step to the process of analyzing the data we've collected is, of course, loading it into memory. The data is in .csv format, which is a common text-based format for two-dimensional data. Perhaps the simplest way is to use ``numpy.loadtxt`` (documented `here <https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html>`_).

There are options to access the data with column names, but this becomes slightly inconvenient to work with later when we're passing the data to other library functions. So, especially since the columns of our data are relatively simple to remember, it's better to just load it as a regular ``ndarray`` (NumPy: *n*-dimensional array). We can name the variables better by *slicing*, which is a common way to subset data in NumPy. A ``:`` grabs all rows or columns, a list with ``[]`` is used to grab only certain rows or columns by index, and a range (e.g., ``1:3``) is used to grab rows or columns within a range of indices. We'll separate the data into the time column and the EMG columns. Finally, to check the dimensionality of the raw and sliced data, we can use NumPy's ``shape`` function, which returns the number of elements in each dimension (rows, then columns).

The code below loads our data collected in :ref:`analysis_to_collect`. 

.. code-block:: python
   :linenos:

   import numpy as np

   TIME_CUTOFF = 15000

   df = np.loadtxt('raw_csv/CHANGE NAME', delimiter=',', dtype=float, skiprows=103 MAY NOT NEED, max_rows=TIME_CUTOFF MAY NOT NEED)
   emg_channels = b30_df[:,[1,2]]
   time = b30_df[:,0]
   print(df.shape, emg_channels.shape, time.shape)

.. number of rows may change later

Notice that we have 15,000 rows and 3 columns. Each row represents the signal values read from the sensor at a particular time, and the columns are time (seconds), right bicep EMG (volts), and left bicep EMG (volts). Checking the shape is always a good step to ensure there wasn't an error in the data loading process.

Another step to check the data quality and give us an idea of what the data looks like is plotting. Let's use NumPy to calculate some basic summary statistics, such as the mean and standard deviation, and plot them on the data using ``matplotlib.pyplot``. Since we're plotting data from multiple EMG channels, it's a good idea to use ``pyplot.subplots``, which puts multiple plots in a grid into the figure. You can specify the grid layout with two parameters (rows and columns), but here we'll only need one since we just want to stack two plots on top of each other.

The ``pyplot.plot`` function is perhaps the most universal: it takes ``x`` and ``y`` to be plotted, as well as some optional visual parameters like ``label``, ``color``, ``linewidth``, and more. We use ``pyplot.axhline`` to plot horizontal lines representing the mean plus and minus two standard deviations. Finally, we can set the subplot titles and axis titles, turn on the legend, and set the overall figure title.

.. code-block:: python
   :linenos:

   import matplotlib.pyplot as plt

   mean_raw = emg_channels.mean(axis=0) # 'axis=0' calculates mean of the columns
   std_raw = emg_channels.std(axis=0)
   fig1, ax1 = plt.subplots(2)

   ax1[0].plot(time, emg_channels[:,1], label = 'signal')
   ax1[0].axhline(y = mean_raw[1], color = 'red', label = 'mean')
   ax1[0].axhline(y = mean_raw[1] + 2*stddev_raw[1], color = 'green', label = 'stddev')
   ax1[0].axhline(y = mean_raw[1] - 2*stddev_raw[1], color = 'green')
   ax1[0].set_title("Left")
   ax1[0].legend()
   ax1[0].set_xlabel("Time (s)")
   ax1[0].set_ylabel("EMG (V)")

   ax1[1].plot(time, emg_channels[:,0], label = 'signal')
   ax1[1].axhline(y = mean_raw[0], color = 'red', label = 'mean')
   ax1[1].axhline(y = mean_raw[0] + 2*stddev_raw[0], color = 'green', label = 'stddev')
   ax1[1].axhline(y = mean_raw[0] - 2*stddev_raw[0], color = 'green')
   ax1[1].set_title("Right")
   ax1[1].legend()
   ax1[1].set_xlabel("Time (s)")
   ax1[1].set_ylabel("EMG (V)")

   fig1.suptitle("Raw Bicep EMG Signals")

If you want to see the plot live, you can use ``plt.show()``. This is the result:

.. TODO insert result here

Notice that the raw signal looks pretty messy: we can sort of see that where the amplitude goes up is when the greatest muscle exertion happened, but it's vague and subject to a lot of quick changes. Also, the mean isn't necessarily at 0V, but we only really care about the changes from 0, so we'll learn how to remove this offset properly when we filter the signal in the next section. Over the next several sections, we'll learn about different ways of processing the signal so that we can get more meaning out of it, visually and numerically.

^^^^^^^^^^^^^^^^^^^^
Filtering the Signal
^^^^^^^^^^^^^^^^^^^^

The first step in any processing of signal data is to apply one or more filters to remove noise from the signal. Without doing this, performance of any machine learning system using the signals will most likely be worse because there are some unwanted artifacts present. Specifically, there are two common sources of noise in a biomedical signal such as EMG: **powerline interference**, caused by unwanted communication between other nearby electronic devices, and **motion**, caused by a small and relatively constant amount of energy being produced by the body at all times.

We won't spend too much time on the math behind how different types of filters work, but know that they essentially use a process called *convolution* to modify the contents of the signal *frequency*. There are four main types of filters, described succinctly by Cheveigné and Nelken (bold inserted for clarity): "The **low-pass filter** attenuates high frequencies, the **high-pass** attenuates low frequencies, the **band-pass** attenuates out-of band frequencies, the **notch** attenuates a narrow band of frequencies" [#]_. To *attenuate* means to reduce the effect of, so these filters are targeting and removing certain frequency ranges; for more details on filtering, refer to their article.

In our case, we'll use LibEMG to filter the EMG signals: the API takes the name, cutoff frequency, and bandwidth of the filter in a dictionary format. You can also just use the default, "common" filters. Don't worry too much about the parameter values for now; cutoff frequencies are recommended by the folks at LibEMG based on the frequencies at which these sources of noise commonly occur, and bandwidths can be modified later to remove frequency more or less harshly.

Finally, we have one more parameter to pass to the filter: sampling frequency. **Sampling frequency** is the rate at which samples are received from the sensor, in Hz. The Delsys Trigno sensors have several different options for this which can be configured during data collection; for this capture, our sampling frequency was 1259.259 Hz.

.. code-block:: python
   :linenos:

   SAMPLE_FREQ = 1259.259

   fi = libemg.filtering.Filter(sampling_frequency=SAMPLE_FREQ)
   fi.install_common_filters() # installs notch at 60 Hz, bandpass from 20-450 Hz
   emg_filt = fi.filter(emg_channels)

   fi.visualize_effect(emg_channels)

.. TODO show visualization

The last line is a nice function provided by LibEMG: it takes the raw signal and produces a visualization showing the signal pre- and post- filtering in the time and frequency domains. We'll explain what that last part means later, but for now, notice how the mean of the signal is now at 0V like we wanted, and also notice on the right how the range of frequencies is much more evenly distributed. This signal definitely has more desirable qualities than the raw signal from before.

^^^^^^^^^^^^^^^^^^^^^^^
Types of Visualizations
^^^^^^^^^^^^^^^^^^^^^^^

There are some special visualizations commonly used with signal data, and we'll explore a few of them here.

**Autocorrelation** and **cross-correlation** are used to measure the relationships between signals. Specifically, autocorrelation looks at *periodicity*, or repeating behavior, by *correlating* the signal with a lagged version of itself (correlation is a technical term, but again, don't worry too much about the math here). So, lag 1 represents all samples from the signal that are 1 observation ahead of another sample (as determined by the sampling frequency), lag -5 represents all samples 5 that are 5 observations behind another sample. Cross-correlation does the same, but uses two signals instead of the same signal with itself. Higher positive values of correlation indicate high similarity between the signals; higher negative values indicate higher reciprocity (i.e., they are opposite each other), and values closer to zero indicate little relationship at all. For more information about autocorrelaton and cross-correlation with EMG signals, see [#]_.

These can be calculated using the ``scipy.correlate`` function, which takes the two signals being correlated and some other optional parameters for the mode and method (we can use the default values for now). For plotting, this is a nice opportunity to learn how to use the nifty ``pyplot.subplots_mosaic`` function. It takes a string parameter for the pattern of grid layout that you'd like, and it's especially useful for irregular patterns. the ``;`` is used for a new row, and different letters each define their own plot, with the number of letters defining the relative spacing. Here, since we have two plots for autocorrelation (left and right), but only one for cross-correlation, a clear way to display this visually is to place the autocorrelation plots next to each other but leave the cross-correlation on its own.

.. code-block:: python
   :linenos:

   from scipy import signal

   auto_corr_right = signal.correlate(in1=emg_filt[:,0], in2=emg_filt[:,0])
   auto_corr_left = signal.correlate(in1=emg_filt[:,1], in2=emg_filt[:,1])
   cross_corr = signal.correlate(in1=emg_filt[:,0], in2=emg_filt[:,1])
   fig2, ax2 = plt.subplot_mosaic("AB;CC") # two plots next to each other on the top row, then one on the bottom row
   
   ax2["A"].plot(range(-TIME_CUTOFF,TIME_CUTOFF-1), auto_corr_left)
   ax2["A"].set_xlabel("Lag")
   ax2["A"].set_ylabel("Autocorrelation")
   ax2["A"].set_title("Autocorrelation, Left")

   ax2["B"].plot(range(-TIME_CUTOFF,TIME_CUTOFF-1), auto_corr_right)
   ax2["B"].set_xlabel("Lag")
   ax2["B"].set_ylabel("Autocorrelation")
   ax2["B"].set_title("Autocorrelation, Right")

   ax2["C"].plot(range(-TIME_CUTOFF,TIME_CUTOFF-1), cross_corr)
   ax2["C"].set_xlabel("Lag")
   ax2["C"].set_ylabel("Correlation")
   ax2["C"].set_title("Cross-Correlation, Left and Right")

   fig2.suptitle("Correlation in Left and Right Bicep EMG Signals")

.. TODO show the viz

.. TODO next viz: PSD then spectrogram

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

.. [#] \A. Cheveigné and I. Nelken. "Filters: When, Why, and How (Not) to Use Them." *Neuron*, vol. 102, no. 2, pp. 280-293, 2019, doi: 10.1016/j.neuron.2019.02.039.

.. [#] \E. Nelson-Wong, S. Howarth, D.A. Winter, and J.P. Callaghan. "Application of Autocorrelation and Crosscorrelation Analyses in Human Movement and Rehabilitation Research." *Journal of Orthopaedic & Sports Physical Therapy* vol. 39, no. 4, pp. 287-295, 2009, doi: 10.2519/jospt.2009.2969.